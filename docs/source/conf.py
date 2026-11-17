# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import tomllib
from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as get_version
from pathlib import Path

# -- Path setup --------------------------------------------------------------

DOCS_SOURCE = Path(__file__).resolve().parent
PROJECT_ROOT = DOCS_SOURCE.parents[1]

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
sys.path.insert(0, str(PROJECT_ROOT / 'src'))
sys.path.insert(0, str(DOCS_SOURCE / 'example'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# Everything is read from the pyproject.toml, the single source of truth.

with (PROJECT_ROOT / 'pyproject.toml').open('rb') as f:
    pyproject = tomllib.load(f)['project']

project = pyproject['name']
author = ', '.join(person['name'] for person in pyproject.get('authors', []))
copyright = f'{datetime.now(tz=UTC).year}, {author}'  # noqa: A001

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# release: The full version, including alpha/beta/rc tags.
# version: The short X.Y version.
try:
    release = get_version(project)
except PackageNotFoundError:
    release = 'unknown (the package is not installed in this environment)'
version = '.'.join(release.split('.')[:2])


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

    # First Party Extensions
    'sphinx.ext.autodoc', # Creates docs from docstrings.
    'sphinx.ext.autosummary', # Creates a summary of the module.
    'sphinx.ext.coverage', # Checks how much of the code is in the documentation.
#   'sphinx.ext.doctest', # Tests docstring snippets.
    'sphinx.ext.duration', # Show the time needed to create docs.
    'sphinx.ext.graphviz', # This is useful in combination with pyreverse.
#   'sphinx.ext.intersphinx', # Used to connect with other documentations.
    'sphinx.ext.napoleon', # Used to convert NumPy or Google style docstrings to reStructuredText.
    'sphinx.ext.todo', # This can also be achieved by adding Todo within the docstring.
    'sphinx.ext.viewcode', # Creates links to source code.

    # Third Party Extensions
    'myst_parser', # Allows to include Markdown files.
    'sphinx_copybutton', # Adds copy button to documentation.
    'sphinx_inline_tabs', # Allows creating tabs does not work within docstring.
    'nbsphinx', # Allows adding Notebooks to docs (needs pandoc on the system).
#    'matplotlib.sphinxext.plot_directive', # Enables plot directive
]

templates_path = ['_templates']
exclude_patterns = ['_build', '_templates', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_show_sphinx = False
# html_logo = '_static/titelbild_01.jpg'


# -- Extensions configuration ------------------------------------------------
##############################################################################
##############################################################################


# -- Options for autodoc -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
# Autodoc adds new directives for sphinx.
# Napoleon is used to make the docstring be written in Numpy or Google style.

# -- Options for autosummary -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
autosummary_generate = True # Saves the created stub documentations.


# -- Options for coverage ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/coverage.html
# To use this you have to: sphinx-build -b coverage .\source\ .\build\

coverage_modules = [project]
coverage_show_missing_items  = True
coverage_statistics_to_stdout = True

# -- Options for doctest -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html


# -- Options for duration ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/duration.html


# -- Options for graphviz ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/graphviz.html
# This adds new directives.


# -- Options for intersphinx -------------------------------------------------
# intersphinx_mapping = {
#    "python": ("http://docs.python.org/", None),
#    "pandas": ("https://pandas.pydata.org/pandas-docs/stable", None),
#    "numpy": ("https://numpy.org/doc/stable", None)
#}


# -- Options for napoleon ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
# Is used by autodoc. Allows to use NumPy- or Google-Style docstrings.

# -- Options for todo --------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html


# -- Options for viewcode -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html
viewcode_line_numbers = True

# -- Options for MyST-Parser -------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/index.html
myst_enable_extensions = [
    'colon_fence', # Enables to separate with ::: instead ``` within Markdown.
    'dollarmath', # Enables parsing of $ and $$ syntax.
    'deflist', # Enables Definition Lists.
]
# Creates anchors for headings, so that links like `(#section)` in the README work.
myst_heading_anchors = 4

# -- Options for nbsphinx ----------------------------------------------------
# https://nbsphinx.readthedocs.io/en/latest/configuration.html
# 'auto' executes notebooks only if they are stored without outputs.
nbsphinx_execute = 'auto'

# -- Third-Party extensions configuration ------------------------------------
##############################################################################
##############################################################################


# -- TODO --------------------------------------------------------------------
