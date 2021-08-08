from tests.unit.testdata import (
    external1,
    external2,
    indexedlib1,
    indexedlib2,
    rfkeyword1,
    rfkeyword2,
    rflibdata1,
    rflibdata2,
    rflibrary1,
    rflibrary2,
)


def test_rfkeyword_total_ordering():
    assert sorted([rfkeyword1, rfkeyword2]) == [rfkeyword1, rfkeyword2]
    assert sorted([rfkeyword2, rfkeyword1]) == [rfkeyword1, rfkeyword2]


def test_rflibrary_total_ordering():
    assert sorted([rflibrary1, rflibrary2]) == [rflibrary1, rflibrary2]
    assert sorted([rflibrary2, rflibrary1]) == [rflibrary1, rflibrary2]


def test_rflibdata_total_ordering():
    assert sorted([rflibdata1, rflibdata2]) == [rflibdata1, rflibdata2]
    assert sorted([rflibdata2, rflibdata1]) == [rflibdata1, rflibdata2]


def test_indexedlibrary_total_ordering():
    assert sorted([indexedlib1, indexedlib2]) == [indexedlib1, indexedlib2]
    assert sorted([indexedlib2, indexedlib1]) == [indexedlib1, indexedlib2]


def test_external_total_ordering():
    assert sorted([external1, external2]) == [external1, external2]
    assert sorted([external2, external1]) == [external1, external2]
