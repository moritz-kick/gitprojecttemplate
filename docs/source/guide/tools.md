# Tools

## Settings overview

As far as possible all settings are kept in a single place of truth. Since this
template uses a lot of tools for different tasks, not all settings could be put
in one place. The specific config location of a tool can be found in its
section below.

`pyproject.toml`
: The replacement for the old `setup.py`/`setup.cfg`. Project metadata,
  dependencies and the settings of most tools (pytest, coverage, Ruff, mypy,
  codespell).

`.pre-commit-config.yaml`
: The hooks run by pre-commit. Smaller tools with little or no configuration
  are configured within this file.

`tox.ini`
: The Tox environments.

`docs/source/conf.py`
: The Sphinx configuration.

`.markdownlint.yaml`
: The Markdown linter configuration.

## Tools overview

This is a list of all tools used by this template. They can be run manually, as
usual in the terminal, but most of the time they will be run via [Tox](#tox).
Tox orchestrates the tools, [pre-commit](#pre-commit) orchestrates the linters
and formatters.

<!-- markdownlint-disable -->
```text
                   ┌──Ruff
                   │
     ┌──Pre-Commit─┼──Out-Of-The-Box-Hooks
     │             │
     │             └──Others (codespell, markdownlint, nb-clean)
     ├──MyPy
     │
Tox──┼──Environments (devenv, requirements)
     │
     ├──Sphinx
     │
     └──Pytest
```
<!-- markdownlint-enable -->

**If project specific changes are made to the default config of this template,
they should be commented.**

| Tool                      | Configuration             | Run                     |
| ------------------------- | ------------------------- | ----------------------- |
| [Tox](#tox)               | `tox.ini`                 | CLI                     |
| [pre-commit](#pre-commit) | `.pre-commit-config.yaml` | git hook or Tox         |
| [Ruff](#ruff)             | `pyproject.toml`          | pre-commit (Tox) or CLI |
| [pytest](#pytest)         | `pyproject.toml`          | Tox or CLI              |
| [mypy](#mypy)             | `pyproject.toml`          | Tox or CLI              |
| [Sphinx](#sphinx)         | `docs/source/conf.py`     | Tox                     |

## Tox

[Docs](https://tox.wiki/en/stable/) / [Repository](https://github.com/tox-dev/tox)

Within the `tox.ini` *tox environments* are specified. Running `tox` runs all
environments listed in `env_list`: in this template, the tests on every
supported Python version. Interpreters that are not installed are skipped.
Other environments are run with `tox -e <env_name>` (e.g. `tox -e docs`) and
listed with `tox list`. Arguments after `--` are passed to the tool, e.g.
`tox -e py312 -- -k test_add`.

The [tox-uv](https://github.com/tox-dev/tox-uv) plugin (in `requires`) creates
the environments with [uv](https://docs.astral.sh/uv/) instead of virtualenv
and pip, which makes creating and updating them several times faster. Tox
installs the plugin automatically if it is missing.

Tox automates the following developer processes in this project:

- environment management,
- requirements generation,
- documentation with Sphinx,
- linting and formatting with pre-commit,
- running pytest with extensions like coverage.

### Installing an environment with Tox

Covers the `[testenv:dev]` section in the `tox.ini`.

The development environment is created with the built-in [tox devenv](
https://tox.wiki/en/stable/cli_interface.html#tox-devenv) command:

``` shell
tox devenv -e dev .venv
```

This creates an environment in `.venv` with all dependencies needed for
developing in this project. It installs the package editable with the
[dev, test and docs dependencies](conventions.md#dependencies). The Python
version can be chosen with e.g. `tox devenv -e dev -x testenv:dev.base_python=py312 .venv`.

### Creating a requirements.txt with Tox

Covers the `[testenv:requirements]` section in the `tox.ini`.

Sometimes a requirements file with pinned versions is needed for
reproducibility, so that bugs or errors can be reproduced and pinned down,
since developers can be working on different versions of packages (e.g.
`package>1.3` is true for version 1.4 and 1.5).

``` shell
tox -e requirements
```

This creates `requirements.txt` (runtime dependencies) and
`requirements-dev.txt` (including all extras) with
[uv pip compile](https://docs.astral.sh/uv/pip/compile/). With `--universal`
one file is valid for all supported Python versions and platforms; where they
need different packages, the lines carry environment markers
(e.g. `; python_full_version < '3.12'`).

### Running pre-commit hooks with Tox

Covers the `[testenv:pre-commit]`, `[testenv:pre-commit-update]` and
`[testenv:pre-commit-clean]` sections in the `tox.ini`.

``` shell
tox -e pre-commit
```

This sets up [pre-commit](#pre-commit) in a separate Tox environment, isolating
it from the local environment and ensuring consistency. It runs the hooks
defined in `.pre-commit-config.yaml` on all files. A single hook can be run
with e.g. `tox -e pre-commit -- ruff-check`. The hook versions are updated with
`tox -e pre-commit-update`.

### Running pytest with Tox

Covers the `[testenv]` section in the `tox.ini`.

``` shell
tox -e py312
```

This runs [pytest](#pytest) with the default flag `-n auto`, which runs the
tests in parallel.

### Building the documentation with Tox

Covers the `[testenv:docs{,-uml,-clean}]` and `[testenv:docs-serve]` sections
in the `tox.ini`.

``` shell
tox -e docs
```

This creates the HTML documentation under `reports/tools/sphinx/docs/index.html`
and a documentation coverage report. The `-uml` variant regenerates the UML
diagrams, the `-clean` variant removes old build files first (e.g.
`tox -e docs-clean`). `tox -e docs-serve` starts a local server that rebuilds
the docs on every change and reloads the browser.

## pre-commit

[Docs](https://pre-commit.com/) / [Repository](https://github.com/pre-commit/pre-commit)

pre-commit helps to maintain code quality and consistency by running various
tools as hooks before each commit. Lots of tools offer pre-commit hooks; in
general every (multi language) script can be used as a hook. Since pre-commit
"just" calls the tools as CLI tools, they respect their local settings (e.g.
Ruff uses the `pyproject.toml`) if not specified otherwise in the
`.pre-commit-config.yaml`.

To run the hooks before every commit, install them as git hook:

``` shell
pre-commit install
```

The first commit installs the hook environments, which may take some time.
Subsequent commits reuse them. To keep the hooks from blocking commits (e.g.
during rapid development phases), skip `pre-commit install` and run them
through Tox (`tox -e pre-commit`) instead. The CI runs them on every pull
request anyway.

The template provides hooks that can be used in almost every project. Each hook
has a one-line explanation in the config, for more information take a look at
the repository/documentation of the hook:

- [Out-of-the-box hooks](https://github.com/pre-commit/pre-commit-hooks)
  (trailing whitespace, YAML/TOML/JSON syntax, large files, ...),
- [Ruff](#ruff) linter and formatter,
- [codespell](https://github.com/codespell-project/codespell) for typos,
- [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) for
  Markdown files,
- [nb-clean](https://github.com/srstevenson/nb-clean) removes metadata from
  notebooks.

Developers may need to adjust the `.pre-commit-config.yaml` to include or
exclude specific files or directories for certain hooks.
**When adding new hooks, it's important to document why the hook was added.
Similarly, if removing hooks, document the reasons, although excluding specific
directories or files from hooks is often sufficient.**

## Ruff

[Docs](https://docs.astral.sh/ruff/) / [Repository](https://github.com/astral-sh/ruff)

Ruff is the linter and formatter (replacing Flake8, isort, Black, pyupgrade,
...). It is configured in the `[tool.ruff]` tables of the `pyproject.toml`: all
rules are enabled (`select = ["ALL"]`) and the ones that are not useful for
this project are ignored with a comment. Tests and notebooks have additional
per-file ignores. Ruff also lints and formats Jupyter notebooks.

## pytest

[Docs](https://docs.pytest.org/en/stable/) / [Repository](https://github.com/pytest-dev/pytest)

pytest is configured in the `[tool.pytest.ini_options]` table of the
`pyproject.toml`. Tests are placed in `tests/` and named `test_*.py`. The
`Examples:` in the docstrings of the package are run as tests as well
([doctests](https://docs.pytest.org/en/stable/how-to/doctest.html),
`--doctest-modules`), so the examples in the documentation stay correct. The
default options create:

- a coverage report in `reports/tools/coverage/html` (pytest-cov),
- a test report in `reports/tools/pytest/test_report.html` (pytest-html),
- a log file in `reports/tools/pytest/logs/`.

Unknown markers and config keys are errors (`--strict-markers`,
`--strict-config`), and tests marked with `xfail` fail if they pass
unexpectedly (`xfail_strict`).

## mypy

[Docs](https://mypy.readthedocs.io/en/stable/) / [Repository](https://github.com/python/mypy)

mypy checks the type hints of the package in strict mode (`[tool.mypy]` in the
`pyproject.toml`). Run it with `tox -e mypy`. The package ships a `py.typed`
marker, so projects that use it can type check against it.

## Sphinx

[Docs](https://www.sphinx-doc.org/en/master/index.html) / [Repository](https://github.com/sphinx-doc/sphinx)

Sphinx is configured in `docs/source/conf.py`. The configuration is documented
and has a link for every configuration or extension that is used. Name,
authors and version are read from the `pyproject.toml` and the installed
package. No system dependencies are needed: notebooks are rendered by MyST-NB
(no pandoc) and diagrams by Mermaid in the browser (no graphviz).

Warnings are errors (`-W` in the `tox.ini`), so broken references, links or
notebooks fail the build instead of piling up.

### Markdown and reStructuredText

Plain Sphinx works with [reStructuredText](
https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
(`.rst`). With [MyST](https://myst-parser.readthedocs.io/en/latest/) Markdown
(`.md`) can be used as well, which is the recommended format for new pages.
Both formats use [directives](
https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html) to
accomplish specific tasks, e.g. a table of contents:

``` rst
.. toctree::
   :maxdepth: 2
```

```` markdown
```{toctree}
:maxdepth: 2
```
````

The **Authoring** section of the [MyST website](
https://myst-parser.readthedocs.io/en/latest/index.html) explains the Markdown
syntax extensions. Some directives of extensions only work in `.rst`; they can
be used in Markdown within an `{eval-rst}` block.

Links to other pages are written as relative Markdown links
(`[Tools](tools.md#sphinx)`); MyST checks that the target exists. Files that are
not part of the documentation (e.g. `tox.ini`) are mentioned as code, not
linked, since they don't exist in the built documentation.

### Notebooks

[MyST-NB](https://myst-nb.readthedocs.io/en/latest/) renders Jupyter notebooks
(`.ipynb`) as pages, see the [notebook gallery](../notebooks/index.md).
Notebooks are executed during the build and the results are cached in
`reports/tools/sphinx/jupyter_cache`, so they only run again when their code
changes. A notebook that raises an error fails the build.

### API reference

[autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
and [autosummary](
https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html) create
the [API reference](../autosummary.rst) from the docstrings of the package,
recursively for all modules. Everything listed in `__all__` of a module is
documented. The templates in `docs/source/_templates` define how modules and
classes are rendered.

### Theme

The [Furo](https://pradyunsg.me/furo/) theme is used for the HTML docs. Its
["Kitchen Sink"](https://pradyunsg.me/furo/kitchen-sink/) shows how all
elements look.

### UML diagrams

[pyreverse](https://pylint.readthedocs.io/en/latest/additional_tools/pyreverse/index.html)
(part of pylint) creates package and class diagrams as Mermaid files in
`docs/source/uml`:

``` shell
tox -e docs-uml
```

They are rendered by [sphinxcontrib-mermaid](
https://github.com/mgaitan/sphinxcontrib-mermaid), see the
[UML page](../uml/index.md). The options of pyreverse can be adjusted in the
`tox.ini`.

```{note}
The diagrams are drawn in the browser by mermaid.js, which is loaded from a CDN
(jsDelivr). Without internet access (offline, behind a firewall, or when the
built docs are opened from a CI artifact without network) they are shown as
text. For offline docs, download `mermaid.esm.min.mjs` into
`docs/source/_static/` and set `mermaid_use_local` in `conf.py`.
```

## Continuous integration

The workflow in `.github/workflows/ci.yml` runs on every push to `main` and on
every pull request. It uses the same Tox environments as on a local machine:

- `tox -e pre-commit` (linting and formatting),
- `tox -e mypy` (type checking),
- `tox -e py` on Python 3.11 - 3.14 (tests),
- `tox -e docs` (documentation build).

[Dependabot](https://docs.github.com/en/code-security/dependabot) keeps the
versions of the GitHub Actions up to date (`.github/dependabot.yml`), the hook
versions are updated with `tox -e pre-commit-update`.

## Sources

- [Python Packaging User Guide (PyPA)](https://packaging.python.org/en/latest/)
- [pyOpenSci Python Package Guide](https://www.pyopensci.org/python-package-guide/)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Read the Docs guides](https://docs.readthedocs.io/en/stable/guides/content/index.html)
