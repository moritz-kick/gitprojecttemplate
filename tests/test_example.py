import pytest

import template
from template import add


def test_version_is_set() -> None:
    assert isinstance(template.__version__, str)
    assert template.__version__


@pytest.mark.parametrize(
    ('a', 'b', 'expected'),
    [
        (1, 2, 3),
        (-1, 1, 0),
        (0.5, 0.25, 0.75),
    ],
)
def test_add(a: float, b: float, expected: float) -> None:
    assert add(a, b) == expected
