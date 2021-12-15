# uPandas

A minimal partial clone of the Pandas API intended for teaching purposes.

Written during a lesson in [Aur's Dojo (he)](https://www.facebook.com/%D7%93%D7%95%D7%92%D7%95-%D7%94%D7%AA%D7%9B%D7%A0%D7%95%D7%AA-%D7%A9%D7%9C-%D7%90%D7%90%D7%95%D7%A8-111102191064164/).

## Usage

```
$ pip install numpy pytest
$ pip install -e .
$ pytest
=========================================================================================== test session starts ============================================================================================
platform darwin -- Python 3.8.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/aursaraf/dev/dojo/upandas
collected 12 items                                                                                                                                                                                         

tests/test_series.py ............                                                                                                                                                                    [100%]

============================================================================================ 12 passed in 0.12s ============================================================================================
$ python
>>> import upandas as up
>>> s = up.Series([1, 2, 3], index=['A', 'B', 'C'])
>>> s.sum()
6.0
>>> s.cumsum()
A	1.0
B	3.0
C	6.0
dtype:float64
```