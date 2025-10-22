# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

# -- Path setup --------------------------------------------------------------

__location__ = os.path.dirname(__file__)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.join(__location__, '../../src'))
sys.path.insert(0, os.path.join(__location__, '../../docs/source/example'))



# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

with open('../../pyproject.toml', 'rb') as f:
    toml = tomllib.load(f)

project = toml['project']['name']
authors_list = [f"{author['name']}, {author['email']}" for author in toml['project']['authors']]
author = ' '.join(authors_list)
copyright = toml['project']['license']['text']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# version: The short X.Y version.
# release: The full version, including alpha/beta/rc tags.
# If you don’t need the separation provided between version and release,
# just set them both to the same value.
try:
    from inverso._version import __version__ as version
except ImportError:
    version = 'UNKNOWN Version. Check if the project is installed in your env.'

release = version


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
#    'nbsphinx', # Allows adding Notebooks to docs.
#    'sphinx_gallery.load_style', # Allows creating Notebook galleries.
#    'matplotlib.sphinxext.plot_directive', # Enables plot directive
]

templates_path = ['_templates']
exclude_patterns = ['_build', '_templates']


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

coverage_modules = ["inverso"]
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

# -- Third-Party extensions configuration ------------------------------------
##############################################################################
##############################################################################


# -- TODO --------------------------------------------------------------------
