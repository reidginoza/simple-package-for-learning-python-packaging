import splpp


def test_isometric_properties():
    low = -1_000_000_000
    high = 1_000_000_000
    n = 100
    res = splpp.rand_ints_via_np(n=n, low=low, high=high)

    assert len(res) == n
    assert min(res) >= low
    assert max(res) <= high
    for i in res:
        assert isinstance(i, int)
