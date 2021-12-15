import numpy as np

class LocHandler:
    def __init__(self, obj) -> None:
        self.obj = obj
    
    def __getitem__(self, key):
        return self.obj._loc(key)

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
        self.index = {k: i for i, k in enumerate(obj)}
        self.reverse_index = list(obj)
        self.is_numeric_index = any(isinstance(v, int) for v in self.reverse_index)

    def __getitem__(self, i):
        if isinstance(i, slice):
            return Series(self.data[i], index=self.reverse_index[i])
        if self.is_numeric_index:
            return self._loc(i)
        return self.data[i]

    @property
    def loc(self):
        return LocHandler(self)

    def _loc(self, key):
        return self.data[self.index[key]]

    def __iter__(self):
        return ((k, self._loc(k)) for k in self.reverse_index)

    def __repr__(self) -> str:
        return '\n'.join(f'{idx}\t{v}' for idx, v in self) + f'\ndtype:{self.data.dtype}'
