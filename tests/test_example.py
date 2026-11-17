import pytest

import template
from template import RunningMean, add


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


def test_running_mean() -> None:
    running_mean = RunningMean()
    for value in (1.0, 2.0, 6.0):
        running_mean.update(value)
    assert running_mean.count == 3
    assert running_mean.mean == pytest.approx(3.0)


def test_running_mean_of_empty_stream_raises() -> None:
    with pytest.raises(ValueError, match='empty stream'):
        _ = RunningMean().mean
