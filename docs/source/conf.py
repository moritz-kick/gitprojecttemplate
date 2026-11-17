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
    version = '.'.join(release.split('.')[:2])
except PackageNotFoundError:  # The package is not installed in this environment.
    release = version = 'unknown'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [

    # First Party Extensions
    'sphinx.ext.autodoc', # Creates docs from docstrings.
    'sphinx.ext.autosummary', # Creates a summary of the module.
    'sphinx.ext.coverage', # Checks how much of the code is in the documentation.
#   'sphinx.ext.doctest', # Tests docstring snippets.
    'sphinx.ext.duration', # Show the time needed to create docs.
#   'sphinx.ext.intersphinx', # Used to connect with other documentations.
    'sphinx.ext.napoleon', # Used to convert NumPy or Google style docstrings to reStructuredText.
    'sphinx.ext.todo', # This can also be achieved by adding Todo within the docstring.
    'sphinx.ext.viewcode', # Creates links to source code.

    # Third Party Extensions
    'myst_nb', # Markdown (MyST) and Jupyter notebooks. Includes myst_parser.
    'sphinx_copybutton', # Adds copy button to documentation.
    'sphinx_inline_tabs', # Allows creating tabs does not work within docstring.
    'sphinxcontrib.mermaid', # Mermaid diagrams (UML from pyreverse), rendered in the browser.
#    'matplotlib.sphinxext.plot_directive', # Enables plot directive
]

templates_path = ['_templates']
exclude_patterns = ['_build', '_templates', '**.ipynb_checkpoints']

# Markdown (.md) is the default format for new pages, reStructuredText still works.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_show_sphinx = False
html_title = f'{project} {version}' # e.g. 'template 1.2' instead of the full dev version.
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

# coverage_modules is not set: every module that appears in the docs is checked.
# The API reference (autosummary) is recursive, so it lists every module of the
# package. (Sphinx also mishandles plain, non-package modules in this setting.)
coverage_show_missing_items = True
coverage_statistics_to_stdout = True

# -- Options for doctest -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html


# -- Options for duration ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/duration.html


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
# Creates anchors for headings, so that links like `(#section)` work.
myst_heading_anchors = 4

# -- Options for MyST-NB -----------------------------------------------------
# https://myst-nb.readthedocs.io/en/latest/configuration.html
# 'cache' executes the notebooks and caches the results, so they only run
# again when their code changes.
nb_execution_mode = 'cache'
nb_execution_cache_path = str(PROJECT_ROOT / 'reports' / 'tools' / 'sphinx' / 'jupyter_cache')
nb_execution_raise_on_error = True # A failing notebook fails the build.
nb_execution_timeout = 120 # Seconds per cell.

# -- Options for sphinxcontrib-mermaid ---------------------------------------
# https://sphinxcontrib-mermaid-demo.readthedocs.io/
# The diagrams in docs/source/uml are created with `tox -e docs-uml`.

# -- Third-Party extensions configuration ------------------------------------
##############################################################################
##############################################################################


# -- TODO --------------------------------------------------------------------
