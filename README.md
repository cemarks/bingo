# Bingo board maker

The purpose of this repository is to provide a simple demonstration of the use of jinja templates to make something useful.  In this case, something useful is a set of bingo boards to support a biology class.

## Use

Jinja is essentially a template engine to produce structured text documents.  The typical use is in HTTP server workflows that produce dynamic HTML content.  However, Jinja can be used in any scenario that requires formatting a set of data into a structured text template.

This example assumes the `miktex` engine (specifically, `pdflatex`) is installed.  It is called in the `render.py` script to produce the Bingo cards in PDF output.

The shell snippet below sets up a python virtual environment and runs the render script, which will produce the Bingo cards.  The only Python dependencies outside of the standard libraries are `numpy` and `jinja2`.

```sh
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python render.py
```