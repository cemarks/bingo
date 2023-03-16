import jinja2
import os
from jinja2 import Template
from numpy import random
import subprocess

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
template = latex_jinja_env.get_template('bingo.jinja2')

num_pages = 10

word_list = [
    "Diffusion",
    "Solute",
    "Isotonic",
    "Hypotonic",
    "Hypertonic",
    "Sodium\\\\Chloride",
    "Less",
    "Distilled\\\\Water",
    "Active\\\\Transport",
    "Solvent",
    "Turgor\\\\Pressure",
    "Membrane\\\\Pumps",
    "Osmosis",
    "ADP",
    "Aquapores",
    "Concentration\\\\Gradient",
    "Crenated",
    "Electrical\\\\Gradient",
    "Permeable",
    "Random",
    "Semi-permeable",
    "Kinetic\\\\Energy",
    "0.9",
    "Skeleton"
]


if __name__ == "__main__":

    words = []

    for n in range(num_pages):
        random_words = random.permutation(word_list).tolist()
        random_words = random_words[0:12] + ["FREE"] + \
            random_words[12:25]

        words.append([
            [random_words[i] for i in range(5*j, 5*(j+1))]
            for j in range(5)
        ])

    with open("bingo.tex", "w") as f:
        f.write(template.render(words = words, N_CARDS = num_pages))

    subprocess.run(["pdflatex", "bingo.tex"])