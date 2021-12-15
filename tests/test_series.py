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