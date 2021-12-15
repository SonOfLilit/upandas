import upandas as ud

def test_happy_path():
    s = ud.Series([1, 2, 3], index=['A', 'B', 'C'])
    assert s.loc['A'] == 1
    assert s.loc['C'] == 3
