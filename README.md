# TEMPLATE README

This is a project template for Data Science Projects with Python.

## Description

Short description of project.

## Project Organization

The following project structure was inspired by
[PyScaffold](https://pyscaffold.org/en/stable/) & [Cookiecutter](https://www.cookiecutter.io/).

<!-- markdownlint-disable -->
```
├── configs                 <- Directory for configurations of model & application.
├── data
│   ├── external            <- Data from external sources
│   ├── interim             <- The interim data sets.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Directory for Sphinx documentation in rst or md.
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-fw-initial-data-exploration`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── vis                 <- Generated plots and figures for reports.
├── src
│   └── template            <- Actual Python package where the main functionality goes.
├── tests                   <- Unit tests which can be run with `pytest`.
├── .github                 <- GitHub Actions CI workflow and Dependabot configuration.
├── .gitignore              <- Specifies files and directories to be ignored by Git.
├── .markdownlint.yaml      <- Configuration of the Markdown linter.
├── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
├── pyproject.toml          <- Build and if possible tool configuration.
├── README.md               <- The top-level README for developers.
└── tox.ini                 <- Configuration file for Tox, specifying how to run tests,
                               check code quality, build docs and build the project in
                               isolated environments.
```
<!-- markdownlint-enable -->

## Project Information

In the [pyproject.toml] under the `[project]` table general information about the
project can be added (authors, description, license, ...). The `[project]` table
information should also be written in the [description section](#description).

The placeholder package is called `template`. To rename it (e.g. to `my_package`),
replace `template` in the following places:

- the directory `src/template/`,
- `name = "template"` in the `[project]` table of [pyproject.toml],
- `source_pkgs = ["template"]` in the `[tool.coverage.run]` table of [pyproject.toml],
- the `pyreverse ... template` command in the `docs` environment of [tox.ini],
- the module name in [./docs/source/autosummary.rst],
- the imports in `src/template/__init__.py` and `tests/test_example.py`.

The version is not written anywhere: [setuptools-scm](https://setuptools-scm.readthedocs.io/)
derives it from the latest git tag, and the package reads it at runtime with
`importlib.metadata`. The Sphinx configuration reads name, authors and version
from the [pyproject.toml] and the installed package.

## How to use this Template

Python (>= 3.11) must be installed on the system. [Tox] runs the tests against
every supported Python version (3.11 - 3.14); versions that are not installed
are skipped (`skip_missing_interpreters`).

Since this template makes heavy use of [Tox], it needs to be installed.

### Installing [Tox] with [pip]

With the following command [Tox] will be installed into the global (-U: User)
Python environment:

``` shell
pip install -U tox
```

### Installing [Tox] with [Pipx]

To keep the global environment clean [Pipx] can be used. [Pipx] will install
and run packages in isolated environments. This is most useful for Python
applications like [Tox]. To install and use [Tox] with [Pipx] install [Pipx]
with one of the following [Pipx installation instructions](
https://pipx.pypa.io/stable/installation/)

Also from the [Tox] documentation:

>"We recommend pipx to install tox into an isolated environment. This has the
>added benefit that later you’ll be able to upgrade tox without affecting other
>parts of the system."

Example:

``` shell
pip install --user pipx
pipx ensurepath
pipx install tox
```

### Testing installation

To test if installation succeeded:

``` shell
tox --version
```

## Styleguide, Gitworkflow and Versioning

### Styleguide

This template is based on the [Google-Python-Style-Guide](
https://google.github.io/styleguide/pyguide.html) it is recommended to at least
take a look at the Table of Contents. Also the style guide can be used as a
reference.
This template does not use some tools recommended by the guide, but has the
same functionality provided by other tools (e.g. Ruff instead Black).

### GitHub Workflow

The recommended workflow for small teams is the [GitHub Workflow](
https://scottchacon.com/2011/08/31/github-flow).

TL;DR:
Stable releases are tagged with a version number. Only branches from main.
Branches should be squashed to be clean and short, before merged into main.

### Versioning with SCM

For Versioning `setuptools-scm` is used. It uses Git-Tags to set a version
number.

## Project Dependencies/ Packages

The project dependencies are managed in [pyproject.toml] in the `[project]`
table. Dependencies that *only* the package depends on should be added into
the dependencies list. That would be all packages that a user of the project
would need, so that the package can be run.

Under the `[project.optional-dependencies]` table there are three more dependency
entries (extras). They are necessary, since this template uses tools.

- **dev**:  
Packages that are necessary for development, should be placed here.(Testing,
Linting, Formatting etc.)
- **test**:  
This environment contains all the packages for testing.
- **docs**:  
[Sphinx] can be extended heavily, so that the dev-dependencies blow up really
fast. To not run into this issue, the dependencies used for building the docs
are placed here (Mostly [Sphinx-Extensions](
https://www.sphinx-doc.org/en/master/usage/extensions/index.html), Parser etc).
Also [Tox] builds faster, if docs-dependencies are separate, and only installed
if really needed.

**If the project, adds separate dev or docs dependencies, it should be
highlighted with a comment, added in [tools overview](#tools-overview) and
explained why it was added.**

## Building and Distributing (BASIC SETUP)

### Building

The template has a very simple setup for the building process, it uses
[setuptools](https://setuptools.pypa.io/en/latest/) as a build backend. It
provides enough functionality so that the package can be installed in the
environment. To install the package the recommended way with this template see
in the [installing section](#installing-an-environment-with-tox))

### Distribution

Access to the repository.

At the moment manually build wheels is the only way to share without access to
the repository.

## Settings overview

It was tried as much as possible to keep all settings in a single place of
truth. Since this template leverages a lot of automation tools and tools that
complete different tasks it was not possible to keep all settings in one place.
Specific config locations for a tool can be found in the tool section.

**Configuration Files**:

- [pyproject.toml]  
  This is the replacement for the old setup.py/setup.cfg.  
  Most tools slowly shift their configuration into this file.
- [.pre-commit-config.yaml]  
  Smaller tools with little or no configuration are managed within this file.
- [tox.ini]  
  Only used for [Tox], mentioned as a reference.
- [./docs/source/conf.py]  
  Used to configure [Sphinx]

## Tools overview

This is a list of all tools used by this template. They can be run manually, as
usual in the terminal, but most of the time they will be run via [Tox]. How to
run the tools with [Tox] see in the [Tox section](#tox-docsrepository).

In general [Tox] is used to orchestrate the tools provided with this template.
That's why its mentioned and explained first. [pre-commit] orchestrates the
linters and formatters.

Where possible there will be a link to the homepage, repository, docs and
reference. Sometimes this overlaps so that there are not all links mentioned.

<!-- markdownlint-disable -->
```
                   ┌──Ruff  
                   │  
                   ├──Out-Of-The-Box-Hooks  
                   │
     ┌──Pre-Commit─┼──MyPy (WIP)
     |             |
     |             ├──Pylint (WIP)
     |             |
     │             └──Others
     ├──Environment  
Tox──┤  
     ├──Build (WIP)  
     │  
     ├──Sphinx  
     |
     └──Pytest  
```
<!-- markdownlint-enable -->

**If project specific changes are made to the default config of this template,
they should be commented**

- [Tox] ([Specific Section](#tox-docsrepository))
  - *Configuration / Settings:* [tox.ini]
  - *Run:* Manual (CLI)

- [pre-commit] ([Specific Section](#pre-commit-docsrepository))
  - *Config / Settings:* [.pre-commit-config.yaml]
  - *Run:* Manual or [Tox]
  - *Small* Hooks:
    Small Hooks are managed within the [.pre-commit-config.yaml], even some of
    them could be managed within the [pyproject.toml]. This choice was made,
    since it would bloat the [pyproject.toml] and the settings of this hooks
    are small.
    - [Out-of-the-Box Hooks](https://github.com/pre-commit/pre-commit-hooks)
    - [Codespell](https://github.com/codespell-project/codespell)
    - [Markdown-cli](https://github.com/igorshubovych/markdownlint-cli)
    - [nb-clean](https://github.com/srstevenson/nb-clean)

- [ruff] ([Specific Section](#ruff-docsrepository))  
  - *Config / Settings:* [pyproject.toml]
  - *Run:* Manual or [pre-commit](run by [Tox])

- [pytest](https://docs.pytest.org/en/stable/)
  - *Config / Settings:* [pyproject.toml]
  - *Run:* Manual or [Tox]

- [sphinx](https://www.sphinx-doc.org/en/master/) (code documentation)
  - *Configuration/ Settings:* [./docs/source/conf.py]
  - *Run:* Manual or [Tox]

- TODO: PYLINT AND MYPY
  - *Config / Settings:* [pyproject.toml]
  - *Run:* Manual or [pre-commit](run by [Tox])

## [Tox] ([Docs](https://tox.wiki/en/stable/)/[Repository](https://github.com/tox-dev/tox))

Within the [tox.ini] *tox environments* can be specified. When running `tox` in
the terminal tox will run all environments specified within the `env_list`
variable, in this template [pytest] is run against multiple Python
versions as default. Other environments can be run with `tox -e <env_name>`
(e.g. `tox -e docs`). All environments can be listed with `tox list`. The
environments will be explained below.

| Command                        | What it does                                               |
| ------------------------------ | ---------------------------------------------------------- |
| `tox`                          | Run the tests on all installed Python versions (3.11-3.14) |
| `tox -e py312`                 | Run the tests on one Python version                        |
| `tox devenv -e dev .venv`      | Create the development environment in `.venv`              |
| `tox -e pre-commit`            | Run all linters and formatters on all files                |
| `tox -e pre-commit-update`     | Update the hook versions in `.pre-commit-config.yaml`      |
| `tox -e mypy`                  | Run the static type checker                                |
| `tox -e docs`                  | Build the documentation (`-uml`, `-clean` variants)        |
| `tox -e py312-requirements`    | Create pinned requirements files                           |

[Tox] automates following developer processes, in this project:

- Environment management
- Requirements generation with pip-compile
- Documentation with [Sphinx]
- Code Quality Linting & Formatting with [pre-commit] running:
- Running [Pytest] + extensions like coverage

### Installing an environment with [Tox]

Covers the `[testenv:dev]` section in the [tox.ini].

The development environment is created with the built-in [tox devenv](
https://tox.wiki/en/stable/cli_interface.html#tox-devenv) command:

``` shell
tox devenv -e dev .venv
```

This will create an environment in `.venv` with all dependencies needed for
developing in this project. It installs the package editable with the
[dev, test and docs dependencies](#project-dependencies-packages). The Python
version can be chosen with e.g. `tox devenv -e dev -x testenv:dev.base_python=py312 .venv`.

As explained in the [dependencies section](#project-dependencies-packages) the
separation is mostly to make [Tox] build faster when running specific
environments like the test environment.

There would be another way to separate the specific dependencies. One could put
the dependencies into the [tox.ini] within the [tox] environment. This would
make the template depend more on [Tox], and take some flexibility to change
tools if wanted.  

### Creating a requirements.txt with [Tox]

Covers the `[testenv:py3{11,12,13,14}-requirements]` section in the [tox.ini]

Sometimes for reproducibility its needed to create a requirements.txt. So that
bugs or errors can be reproduced and pinned down, since developers can be
working on different versions of packages (e.g. package>1.3 is true for package
version 1.4 and 1.5).

``` shell
tox -e py312-requirements
```

This creates `requirements-py312.txt` (runtime dependencies) and
`requirements-py312-dev.txt` (including all extras) with [pip-tools](
https://pip-tools.readthedocs.io/).

### Running [pre-commit]-hooks with [Tox]

Covers the `[testenv:pre-commit]`, `[testenv:pre-commit-update]` and
`[testenv:pre-commit-clean]` sections in [tox.ini]

[Pre-commit] is used to orchestrate linter and formatter. See [Pre-commit section](#pre-commit-docsrepository)
for more details.  

``` shell
tox -e pre-commit
```

This command sets up [pre-commit] in a separate [Tox] environment, isolating it
from your local environment and ensuring consistency.

This runs the defined hooks in [.pre-commit-config.yaml] on all files. A single
hook can be run with e.g. `tox -e pre-commit -- ruff-check`. The hook versions
can be updated with `tox -e pre-commit-update`.

### Running [Pytest] with [Tox]

Covers the `[testenv]` section in the [tox.ini]

``` shell
tox -e py312
```

This runs [pytest] with the default flag `-n auto`, which runs [pytest] in
parallel mode. Other arguments can be passed after `--`, e.g.
`tox -e py312 -- -k test_add`. The options in the [pyproject.toml] create a
coverage report (`reports/tools/coverage/html`) and a test report
(`reports/tools/pytest/test_report.html`).

### Building the sphinx documentation with [Tox]

Covers the `[testenv:docs{,-uml,-clean}]` section in the [tox.ini]

``` shell
tox -e docs
```

This creates a html documentation under `reports/tools/sphinx/docs/index.html`.
The `-uml` flag can be used to create UML-diagrams for the documentation and the
`-clean` flag removes old build files first (e.g. `tox -e docs-clean`).

## [Pre-commit] ([Docs](https://pre-commit.com/)/[Repository](https://github.com/pre-commit/pre-commit))

[Pre-commit] is a powerful tool that helps maintain code quality and consistency
by running various tools as [pre-commit] hooks before each commit. This ensures
that code adheres to specified standards and passes required checks before
being committed to the repository. Lots of tools offer [pre-commit]-hooks. In
general every (multi language) script can be used as a hook. [Pre-commit] is
configured in the [.pre-commit-config.yaml].

[Pre-commit] allows you to specify a set of hooks that are executed before a
commit is finalized. These hooks can perform a variety of tasks, such as
linting code, checking for style violations and more. The hooks and the
configuration for these hooks is stored in the [.pre-commit-config.yaml] file.
Since [pre-commit] "just" calls the tools as a cli tool, the tools will respect
local settings (e.g. [Ruff] will use the [pyproject.toml]) if not specified
otherwise in the [.pre-commit-config.yaml].

To install [pre-commit] hooks locally, run the following command:

``` shell
pre-commit install
```

This installs the specified hooks and sets them up to run before every
commit, this is good practice, but annoying sometimes. The first time you
commit, [pre-commit] will install the hooks, which may take some time. Subsequent
commits will reuse the installed hooks, unless specified otherwise.

To avoid [pre-commit] hooks from blocking your commits (e.g., during rapid
development phases), you can run [pre-commit] through [Tox]. This method allows you
to manually run [pre-commit] checks and integrate them into CI pipelines (see
[Continuous Integration](#continuous-integration)).

To run [pre-commit] with [Tox], see [pre-commit hooks with Tox](#running-pre-commit-hooks-with-tox)

The template provides hooks that can be used in mostly every project. Hooks in
use can be found in the [.pre-commit-config.yaml]. A one-line explanation is
given in the config, for more information for a specific hook take a look at
the repository/documentation of that hook.

```text
           ┌──Ruff  
           │  
           ├──Out-Of-The-Box-Hooks  
           │
Pre-Commit─┼──MyPy (WIP)
           |
           ├──Pylint (WIP)
           |
           └──Others
```

Developers may need to adjust the [.pre-commit-config.yaml] file to include or
exclude specific files or directories for certain hooks.  
**When adding new hooks, it's important to document why the hook was added.
Similarly, if removing hooks, document the reasons, although excluding specific
directories or files from hooks is often sufficient.**

### Notebook Hooks

## Ruff ([Docs](https://docs.astral.sh/ruff/)/[Repository](https://github.com/astral-sh/ruff))

## Pytest ([Docs](https://docs.pytest.org/en/stable/)/[Repository](https://github.com/pytest-dev/pytest))

Can be run (see [pytest with Tox](#running-pytest-with-tox)) but documentation
is WIP

## MyPy ([Docs](https://mypy.readthedocs.io/en/stable/)/[Repository](https://github.com/python/mypy))

WIP

## PyLint ([Docs](https://pylint.readthedocs.io/en/latest/)/[Repository](https://github.com/pylint-dev/pylint))

WIP

## Sphinx ([Docs](https://www.sphinx-doc.org/en/master/index.html)/[Repository](https://github.com/sphinx-doc/sphinx))

Some dependencies can't be shipped with this template, the following needs to
be available on system.

- **pandoc**:  
  Needed by `nbsphinx` to render the notebooks.
- **graphviz**:  
  Renders the UML diagrams created by `pyreverse`.

[Sphinx] is configured in [./docs/source/conf.py]. The configuration is well
documented, also there is a link placed for every configuration or extension
that is used.  

[Sphinx] can be highly customized with [sphinx-extensions](
https://www.sphinx-doc.org/en/master/usage/extensions/), also there exist
third-party extensions. The used extensions are, as mentioned, documented in
`config.py`.  

Plain Sphinx works with [reStructuredText]. [ReStructuredText] (`.rst`) is a
markup language like Markdown (`.md`). In this documentation its also possible
to use Markdown instead of [reStructuredText], since the [MyST-Parser](
https://myst-parser.readthedocs.io/en/latest/index.html)-extension is in use.

>Some extensions do not support MyST-Parser. In this specific cases `.rst` must
be used.

How to generate the documentation with this template can be read in the [build
documentation with Tox](#building-the-sphinx-documentation-with-tox).

### How it works

Sphinx uses [directives](
https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html)
that extend the plain [reStructuredText] syntax to accomplish specific tasks.

``` shell
.. toctree::
:maxdepth: 2
```

MyST-Parser adds some more syntax to Markdown to accomplish the documentation
tasks. Under the **Authoring** section on the [MyST-Website](
https://myst-parser.readthedocs.io/en/latest/index.html) are more information
for the Markdown directives and specific syntax extensions.

``` markdown
:::{toctree}
:maxdepth: 2
:::
```

For example an example take a look at [./docs/source/index.rst]

### Extensions

Extensions add directives that then can be used.
For example [sphinx.extensions.autodoc](
https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) uses the

``` shell
.. automodule:: TEMPLATE
```

directive to create a documentation from the docstring given in a module
"TEMPLATE" that are imported by \_\_all\_\_ within the module `__init__.py`.
This is the default behavior, it can be customized.

See [./docs/source/autosummary.rst]

### Theme

Usually a [Theme](https://www.sphinx-doc.org/en/master/usage/theming.html) is
used for the HTML-Docs. In this project the [Furo](https://pradyunsg.me/furo/)
theme is used.

### Creating UML with pyreverse

As mentioned for this `graphviz` need to be on the system and on the sys path.

This is created by:

``` shell
tox -e docs-uml
```

The behavior of [pyreverse](
https://pylint.readthedocs.io/en/latest/pyreverse.html) can be adjust in the
[tox.ini].

### More Information

- The Furo website has a subsection that is called ["Kitchen Sink"](
https://pradyunsg.me/furo/kitchen-sink/) it contains a information for working
with Sphinx in general.
- Read the Docs provides more tips: <https://docs.readthedocs.io/en/stable/guides/content/index.html>

## Continuous Integration

The workflow in `.github/workflows/ci.yml` runs on every push to `main` and on
every pull request. It uses the same [Tox] environments as on a local machine:

- `tox -e pre-commit` (linting and formatting),
- `tox -e mypy` (type checking),
- `tox -e py` on Python 3.11 - 3.14 (tests),
- `tox -e docs` (documentation build).

[Dependabot](https://docs.github.com/en/code-security/dependabot) keeps the
versions of the GitHub Actions up to date (`.github/dependabot.yml`), the hook
versions are updated with `tox -e pre-commit-update`.

## Sources

A list of useful sources:

- [PyPA](https://packaging.python.org/en/latest/)
- [pyOpenSci](https://www.pyopensci.org/python-package-guide/)
- [Pro Git Book](https://git-scm.com/book/en/v2)

### Tool Links

[Tox]: https://tox.wiki/en/stable/
[Pipx]: https://pipx.pypa.io/stable/
[Sphinx]: https://www.sphinx-doc.org
[pip]: https://pip.pypa.io/en/stable/
[pre-commit]: https://pre-commit.com/
[ruff]: https://docs.astral.sh/ruff/
[pytest]: https://docs.pytest.org/en/stable/
[reStructuredText]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html

### Files

[pyproject.toml]: pyproject.toml
[.pre-commit-config.yaml]: .pre-commit-config.yaml
[tox.ini]: tox.ini
[./docs/source/conf.py]: ./docs/source/conf.py
[./docs/source/index.rst]: ./docs/source/index.rst
[./docs/source/autosummary.rst]: ./docs/source/autosummary.rst
