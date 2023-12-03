from task5 import convert


def test_convert():
    assert convert("123456987654", 6) == "234561876549"
    assert convert("", 8) == ""
    assert convert("123456779", 0) == ""
    assert convert("563000655734469485", 4) == "0365065073456944"
