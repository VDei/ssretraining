from task4 import stat


def test_stat():
    sa = (1, 1, 2, 3, 34, 4, 5, 4, 5, 4, 55, 5, 5, 5)
    assert stat(sa) == [14, 7, 4, [[5], [5]]]
