# TEMPLATE

This is a project template for Data Science Projects with Python.

## Description

Short description of project.

## Quick start

Python (>= 3.11) and [Tox] are needed. Tox orchestrates all other tools
(testing, linting, docs) in isolated environments. It uses
[tox-uv](https://github.com/tox-dev/tox-uv), so environments are created with
[uv](https://docs.astral.sh/uv/), which is much faster than virtualenv and pip.

Install [Tox] once, isolated from other projects, with uv (recommended) or
[pipx](https://pipx.pypa.io/stable/):

``` shell
uv tool install tox --with tox-uv
```

``` shell
pipx install tox && pipx inject tox tox-uv
```

Then, inside the repository:

``` shell
tox devenv -e dev .venv     # development environment with all extras
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pre-commit install          # run linters and formatters on every commit (optional)
tox                         # run the tests on all installed Python versions
```

| Command                     | What it does                                               |
| --------------------------- | ---------------------------------------------------------- |
| `tox`                       | Run the tests on all installed Python versions (3.11-3.14) |
| `tox -e py312`              | Run the tests on one Python version                        |
| `tox devenv -e dev .venv`   | Create the development environment in `.venv`              |
| `tox -e pre-commit`         | Run all linters and formatters on all files                |
| `tox -e pre-commit-update`  | Update the hook versions in `.pre-commit-config.yaml`      |
| `tox -e mypy`               | Run the static type checker                                |
| `tox -e docs`               | Build the documentation (`-uml`, `-clean` variants)        |
| `tox -e docs-serve`         | Preview the documentation with live reload                 |
| `tox -e requirements`       | Create pinned requirements files                           |

All environments are listed with `tox list`.

## Using this template

The placeholder package is called `template`. To rename it (e.g. to `my_package`),
replace `template` in the following places:

- the directory `src/template/`,
- `name = "template"` in the `[project]` table of `pyproject.toml`,
- `source_pkgs = ["template"]` in the `[tool.coverage.run]` table of `pyproject.toml`,
- the `pyreverse ... template` command in the `docs` environment of `tox.ini`,
- the module name in `docs/source/autosummary.rst`,
- the imports in `tests/test_example.py`.

Also update the general information in the `[project]` table of
`pyproject.toml` (authors, description, ...), the copyright line in `LICENSE`
and the [description](#description) above.

The version is not written anywhere: [setuptools-scm](https://setuptools-scm.readthedocs.io/)
derives it from the latest git tag, and the package reads it at runtime with
`importlib.metadata`.

## Project Organization

The following project structure was inspired by
[PyScaffold](https://pyscaffold.org/en/stable/) & [Cookiecutter](https://www.cookiecutter.io/).

<!-- markdownlint-disable -->
```text
├── configs                 <- Directory for configurations of model & application.
├── data
│   ├── external            <- Data from external sources
│   ├── interim             <- The interim data sets.
│   ├── processed           <- The final, canonical data sets for modeling.
│   └── raw                 <- The original, immutable data dump.
├── docs                    <- Sphinx documentation (Markdown, notebooks, API reference).
├── models                  <- Trained and serialized models, model predictions,
│                              or model summaries.
├── notebooks               <- Jupyter notebooks. Naming convention is a number (for
│                              ordering), the creator's initials and a description,
│                              e.g. `1.0-fw-initial-data-exploration`.
├── references              <- Data dictionaries, manuals, and all other materials.
├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── tools               <- Reports of the tools (tests, coverage, docs), not tracked.
├── src
│   └── template            <- Actual Python package where the main functionality goes.
├── tests                   <- Unit tests which can be run with `pytest`.
├── .github                 <- GitHub Actions CI workflow and Dependabot configuration.
├── .gitignore              <- Specifies files and directories to be ignored by Git.
├── .markdownlint.yaml      <- Configuration of the Markdown linter.
├── .pre-commit-config.yaml <- Configuration of pre-commit git hooks.
├── LICENSE                 <- MIT license.
├── pyproject.toml          <- Build and if possible tool configuration.
├── README.md               <- The top-level README for developers.
└── tox.ini                 <- Configuration file for Tox, specifying how to run tests,
                               check code quality, build docs and build the project in
                               isolated environments.
```
<!-- markdownlint-enable -->

## Developer guide

The detailed documentation of the template is part of the docs. Build them with
`tox -e docs` and open `reports/tools/sphinx/docs/index.html`, or read the
pages directly:

- [Development conventions](docs/source/guide/conventions.md): style guide, git
  workflow, versioning, dependencies, building.
- [Tools](docs/source/guide/tools.md): configuration and usage of Tox,
  pre-commit, Ruff, pytest, mypy, Sphinx and the CI workflow.

## License

This project is licensed under the MIT License, see the `LICENSE` file.

[Tox]: https://tox.wiki/en/stable/
