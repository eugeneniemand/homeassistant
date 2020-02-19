import modules.utils as utils

def test_hasNumbers():
    assert utils.hasNumbers("abc123abc") == True
    assert utils.hasNumbers("abcabc") == False

def test_intersect():
    listA = ["A", "B"]
    listB = ["C", "A"]
    assert utils.intersect(listA,listB) == ["A"]

