class LocHandler:
    def __init__(self, obj) -> None:
        self.obj = obj
    
    def __getitem__(self, key):
        return self.obj.data[self.obj.index[key]]

class Series:
    def __init__(self, data, index):
        self.data = data
        self.index = self._build_index(index)

    @staticmethod
    def _build_index(obj):
        return {k: i for i, k in enumerate(obj)}

    @property
    def loc(self):
        return LocHandler(self)
