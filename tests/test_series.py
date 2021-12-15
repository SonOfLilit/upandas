import pytest

import numpy as np
import upandas as ud

def test_happy_path():
    s = ud.Series([1, 2, 3], index=['A', 'B', 'C'])
    assert s.loc['A'] == 1
    assert s.loc['C'] == 3

def test_build_from_ndarray():
    s = ud.Series(np.arange(5), index=np.arange(5))
    assert s.loc[0] == 0
    assert s.loc[4] == 4

def test_build_from_dict():
    s = ud.Series({'A': 1, 'B': 2, 'C': 3})
    assert s.loc['A'] == 1
    assert s.loc['C'] == 3

def test_constant():
    s = ud.Series(4, index=['A', 'B', 'C'])
    assert s.loc['A'] == 4
    assert s.loc['C'] == 4

def test_same_size():
    with pytest.raises(ValueError):
        ud.Series([1, 2, 3], index=['A', 'B', 'C', 'D'])
    with pytest.raises(ValueError):
        ud.Series([1, 2, 3], index=['A', 'B'])

def test_no_index_passed():
    s = ud.Series([5, 4, 3])
    assert s.loc[0] == 5
    assert s.loc[1] == 4

def test_repr():
    s = ud.Series([1, 2, 3], index=['A', 'B', 'C'])
    assert repr(s) == """\
A\t1.0
B\t2.0
C\t3.0
dtype:float64"""

def test_access_by_numeric_index():
    s = ud.Series([1, 2, 3], index=['A', 'B', 'C'])
    assert s[0] == 1
    assert s[2] == 3

def test_access_by_numeric_index_with_numeric_index():
    s = ud.Series([1, 2, 3], index=[2, 1, 0])
    assert s[0] == 3
    assert s[2] == 1

def test_slice():
    s = ud.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
    assert list(s[1:3]) == [('B', 2), ('C', 3)]
    assert list(s[5:]) == []
    assert list(s[-1:]) == [('D', 4)]
