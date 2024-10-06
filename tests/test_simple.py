from hypothesis import assume, given, strategies as st
import numpy as np

import splpp


int_64_info = np.iinfo(np.int64)

# due to memory issues
# 2**20 items, approx. 8 MegaBytes
# max_size = 1048576

# due to memory issues
# 2**19, approx. 4 MegaBytes
max_size = 524288


def to_num_of_int64(gibs):
    return gibs * 1024 * 1024 * 1024 * 8 // 64


@given(
    low=st.integers(min_value=int_64_info.min, max_value=int_64_info.max - 1),
    high=st.integers(min_value=int_64_info.min + 1, max_value=int_64_info.max),
    n=st.integers(min_value=1, max_value=max_size),
)
def test_properties(low, high, n):
    assume(low < high)

    res = splpp.rand_ints_via_np(n=n, low=low, high=high)

    assert len(res) == n
    assert min(res) >= low
    assert max(res) <= high
    assert all(isinstance(i, int) for i in res)
