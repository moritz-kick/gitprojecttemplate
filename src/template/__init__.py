"""TEMPLATE package.

Replace this docstring with a short description of the package. Everything
listed in ``__all__`` is part of the public API and is documented by Sphinx.
"""

from importlib.metadata import PackageNotFoundError, version

from template.example import add

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover - only when running from an uninstalled checkout
    __version__ = 'unknown'

__all__ = ['__version__', 'add']
