"""The library. Intended to be imported into __init__.py"""

import numpy as np


int_64_info = np.iinfo(np.int64)


def rand_ints_via_np(n: int = 10, low: int = 0, high: int = 100) -> list[int]:
    """Make a `list` of random `int`s using NumPy."""
    if not (int_64_info.min <= low <= int_64_info.max):
        raise ValueError(f"low is not valid for Numpy int64:{low}")

    if not (int_64_info.min <= high <= int_64_info.max):
        raise ValueError(f"high is not valid for Numpy int64:{high}")

    # Honestly, the limit is probably a lot lower.
    # Probably dependent on memory limits.
    if not (0 < n <= int_64_info.max):
        raise ValueError(f"n is not valid for positive Numpy int64:{n}")

    rng = np.random.default_rng()

    return [int(n) for n in rng.integers(low, high, size=n)]
