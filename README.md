# CV Converter

Converts CVs in PDF format into Markdown format for providing to LLMs.

## Setup

As we're parsing CVs in PDF format into Markdown for token efficiency, there is some environment setup required.

### Python Environment

Use [pyenv](https://github.com/pyenv/pyenv) to install version 3.14.4 (or later) of Python:

```bash
pyenv install -v 3.14.4
```

Create a virtual environment with this version of Python and activate it:

```bash
pyenv virtualenv 3.14.4 cv-optimiser
pyenv activate cv-optimiser
```

To streamline VSCode usage, create a `.venv` virtual environment in the root of the repository, so that this will be activated and used whenever the project is active in VSCode.

In the root of the repository, with the above environment active:

```bash
python -m venv .venv
```

Finally, install the project dependencies:

```bash
pip install -r requirements.txt
```

## Usage

There are two Python scripts in the `src` folder:

- `cv-parser.py` uses the [Nanonets PDF to Markdown API](https://tools.nanonets.com/pdf-to-markdown) to convert all PDF files specified in `CV_PDF_FOLDER` into structured Markdown documents, outputted to the folder specified in `CV_MD_FOLDER`. Note that the parser isn't fool-proof; I recommend checking each converted file.
- `markdown-concatanator.py` concatanates all Markdown documents found in `CV_MD_FOLDER` into a single Markdown document. The source filename is included with each document in the concatanated file. This provides an efficient single document to provide to an LLM.
