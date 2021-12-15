import numpy as np

class LocHandler:
    def __init__(self, obj) -> None:
        self.obj = obj
    
    def __getitem__(self, key):
        return self.obj._loc(key)


def wrap_numpy(name):
    def f(self, *args, **kwargs):
        result_data = getattr(self.data, name)(*args, **kwargs)
        if not hasattr(result_data, '__iter__'):
            return result_data
        return Series(result_data, index=self.index)
    return f

class Series:
    def __init__(self, data, index=None):
        if isinstance(data, dict):
            index = list(data.keys())
            data = [data[k] for k in index]
        if not hasattr(data, '__iter__'):
            if index is None:
                raise ValueError("constant series must have an index")
            data = data * np.ones(len(index))
        data = np.array(data, dtype=np.float64)
        self.data = data
        if index is None:
            index = range(len(self.data))
        if len(data) != len(index):
            raise ValueError("data and index have different sizes")
        self._build_index(index)

    def _build_index(self, obj):
        self.index_map = {k: i for i, k in enumerate(obj)}
        self.index = list(obj)
        self.is_numeric_index = any(isinstance(v, int) for v in self.index)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return Series(self.data[i], index=self.index[i])
        if self.is_numeric_index:
            return self._loc(i)
        return self.data[i]

    @property
    def loc(self):
        return LocHandler(self)

    def _loc(self, key):
        return self.data[self.index_map[key]]

    def __iter__(self):
        return ((k, self._loc(k)) for k in self.index)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        new_inputs = [x if x is not self else self.data for x in inputs]
        result_data = getattr(ufunc, method)(*new_inputs, **kwargs)
        if not hasattr(result_data, '__iter__'):
            return result_data
        return Series(result_data, index=self.index)

    for _method in ['sum', 'cumsum']:
        locals()[_method] = wrap_numpy(_method)
    # _a = numpy.ones(0)
    # for _k, _v in _a.__dict__.items():
    #     if is_ufunc(_v):
    #         name = _v.__name__
    #         locals()[name] = wrap_numpy(name)

    def __repr__(self) -> str:
        return '\n'.join(f'{idx}\t{v}' for idx, v in self) + f'\ndtype:{self.data.dtype}'

    def __eq__(self, other):
        return list(self) == list(other)

    def __hash__(self):
        raise NotImplementedError()
