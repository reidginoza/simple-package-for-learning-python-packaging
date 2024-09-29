import json

from splpp import demo


def test_myoutput(capsys):
    # Arrange
    # =======
    # Values hard-coded in demo
    n = 10
    low = 0
    high = 100

    demo.main()
    captured = capsys.readouterr()
    assert "[" in captured.out
    assert "]" in captured.out
    assert "," in captured.out

    res = json.loads(captured.out)
    assert isinstance(res, list)

    assert len(res) == n
    assert min(res) >= low
    assert max(res) <= high
    for i in res:
        assert isinstance(i, int)
