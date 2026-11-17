"""Example module. Replace it with the actual functionality of the package."""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first summand.
        b: The second summand.

    Returns:
        The sum of ``a`` and ``b``.

    Examples:
        >>> add(1, 2)
        3
    """
    return a + b


class RunningMean:
    """Mean of a stream of values, updated one value at a time.

    Examples:
        >>> running_mean = RunningMean()
        >>> running_mean.update(1.0)
        >>> running_mean.update(3.0)
        >>> running_mean.mean
        2.0
    """

    def __init__(self) -> None:
        self.count = 0
        self._total = 0.0

    def update(self, value: float) -> None:
        """Add a value to the stream.

        Args:
            value: The new value.
        """
        self.count += 1
        self._total += value

    @property
    def mean(self) -> float:
        """The mean of all values so far.

        Raises:
            ValueError: If no value was added yet.
        """
        if self.count == 0:
            msg = 'The mean of an empty stream is undefined.'
            raise ValueError(msg)
        return self._total / self.count
