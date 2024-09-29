"""The library. Intended to be imported into __init__.py"""

import numpy as np


def rand_ints_via_np(n: int = 10, low: int = 0, high: int = 100) -> list[int]:
    """Make a `list` of random `int`s using NumPy."""
    rng = np.random.default_rng()

    return [int(n) for n in rng.integers(low, high, size=n)]
