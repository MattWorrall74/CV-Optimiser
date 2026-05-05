# CV Optimiser

Uses Gemini CLI to compare a job description from a vacancy to a supplied set of CVs, then determine the best CV to use as a base, with exact revisions to align it to the vacancy.

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
