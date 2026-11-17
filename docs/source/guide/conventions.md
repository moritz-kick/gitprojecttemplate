# Development conventions

## Style guide

This template is based on the [Google Python Style Guide](
https://google.github.io/styleguide/pyguide.html). It is recommended to at least
take a look at the table of contents; the style guide can also be used as a
reference. This template does not use some tools recommended by the guide, but
gets the same functionality from other tools (e.g. Ruff instead of Black).

Docstrings use the Google style (`convention = "google"` in
`[tool.ruff.lint.pydocstyle]`), they are rendered by Sphinx with
[napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html).
An example of all docstring sections is in the [docstring example](../example/example_google.rst).

## Git workflow

The recommended workflow for small teams is the [GitHub Flow](
https://docs.github.com/en/get-started/using-github/github-flow).

TL;DR: Branch from `main`, open a pull request, and merge it once the CI is
green. Branches should be squashed to be clean and short before they are merged
into `main`. Stable releases are tagged with a version number.

## Versioning

[setuptools-scm](https://setuptools-scm.readthedocs.io/) derives the version
from git tags (e.g. `git tag v1.2.0`), so it is never written by hand. Between
two tags the version contains the distance to the last tag and the commit, e.g.
`1.2.0.post1.dev3+g1a2b3c4` for the third commit after `v1.2.0`
(`version_scheme = "no-guess-dev"`: no guessing of the next version). The
package reads it at runtime:

``` python
import template

template.__version__
```

## Dependencies

The project dependencies are managed in `pyproject.toml` in the `[project]`
table. Dependencies that *only* the package depends on should be added into the
`dependencies` list. That would be all packages that a user of the project
would need, so that the package can be run.

Under the `[project.optional-dependencies]` table there are three more
dependency entries (extras). They are necessary, since this template uses tools.

dev
: Packages that are necessary for development (type checking, linting,
  formatting, Tox).

test
: All the packages for testing (pytest and its plugins).

docs
: Sphinx can be extended heavily, so that the dev dependencies blow up really
  fast. To not run into this issue, the dependencies used for building the docs
  are placed here (mostly [Sphinx extensions](
  https://www.sphinx-doc.org/en/master/usage/extensions/index.html), parsers,
  etc.). Also Tox builds faster if the docs dependencies are separate and only
  installed if really needed.

**If the project adds separate dev or docs dependencies, it should be
highlighted with a comment, added in the [tools overview](tools.md#tools-overview)
and explained why it was added.**

There would be another way to separate the specific dependencies: putting them
into the `tox.ini` within the Tox environments. This would make the template
depend more on Tox and take some flexibility to change tools if wanted.

```{note}
[Dependency groups (PEP 735)](https://packaging.python.org/en/latest/specifications/dependency-groups/)
in a `[dependency-groups]` table are the newer standard for development-only
dependencies, since they are not published with the package. Tox supports them
with `dependency_groups`. The extras are kept for now, because pinning them is
supported by more tools.
```

## Building and distributing

### Building

The template uses [setuptools](https://setuptools.pypa.io/en/latest/) as build
backend with the `src` layout, so the packages in `src/` are found
automatically. A wheel and a source distribution are built with:

``` shell
uv build            # or: python -m build
```

To install the package for development, see
[installing an environment with Tox](tools.md#installing-an-environment-with-tox).

### Distribution

At the moment access to the repository or a manually built wheel are the only
ways to share the package.
