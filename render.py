import jinja2
import os
from jinja2 import Template
from numpy import random
from subprocess import Popen, PIPE, STDOUT
import io
import os

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

NUM_PAGES = 8
TITLE = "Entrepreneurship"
SIZE = 4 # Must be 4 or 5
WORD_LIST = [
    "Entrepreneur",
    "Business\\\\Plan",
    "Mission",
    "Vision",
    "Product",
    "Service",
    "Customer",
    "Competitors",
    "Elevator\\\\Pitch",
    "Income",
    "Expense",
    "Profit",
    "Marketing",
    "Prototype",
    "Brand",
    "Slogan"
]

if SIZE == 4:
    template = latex_jinja_env.get_template('bingo4x4.jinja2')
else:
    template = latex_jinja_env.get_template('bingo.jinja2')


if __name__ == "__main__":

    words = []

    for n in range(NUM_PAGES):
        random_words = random.permutation(WORD_LIST).tolist()
        if len(random_words) == 24:
            random_words = random_words[0:12] + ["FREE"] + \
                random_words[12:25]

        words.append([
            [random_words[i] for i in range(SIZE*j, SIZE*(j+1))]
            for j in range(SIZE)
        ])


    tex_source = io.BytesIO(
        template.render(
            words = words,
            N_CARDS = NUM_PAGES,
            title = TITLE.upper()
        ).encode()
    )

    tex_source.seek(0)

    p = Popen(["pdflatex"], stdin = PIPE)
    p.communicate(input=tex_source.read())
    
    os.remove("texput.aux")
    os.remove("texput.log")
