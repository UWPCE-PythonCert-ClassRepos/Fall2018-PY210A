#!/usr/bin/env python
"""
Class that handles sparsely populated lists
"""

class SparseArray():

    def __init__(self, values, sparse_value=0):
        self.length = 0
        self._values = dict()
        self.sparse_value = sparse_value
        if values is None:
            return
        self.length = len(values)
        for i, value in enumerate(values):
            if value != self.sparse_value:
                self._values[i] = value

    def append(self, value):
        self._values[self.__len__()] = value
        self.length += 1

    def _get_index(self, index):
        if index < 0:
            return self.__len__() - abs(index)
        return index

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if isinstance(index, slice):
            start = self._get_index(index.start) if index.start is not None else 0
            end = self._get_index(index.stop) if index.stop is not None else self.__len__()
            step = index.step if index.step is not None else 1

            # Could also grab the values directly from the dict and shoe-horn a new SparseArray
            result = []
            for i in range(start, end, step):
                result.append(self._values.get(i, 0))
            return SparseArray(result)
        else:
            if abs(index) > (self.__len__() + 1):
                raise IndexError("Index greater than length")
            index = self._get_index(index)
            
            return self._values.get(index, self.sparse_value)

    def __setitem__(self, index, value):
        if abs(index) > (self.__len__() + 1):
            raise IndexError("Index greater than length")
        index = self._get_index(index)

        if value == self.sparse_value:
            if value in self._values:
                del self._values[index]
        else:
            self._values[index] = value

    def __delitem__(self, index):
        if abs(index) > (self.__len__() + 1):
            raise IndexError("Index greater than length")
        index = self._get_index(index)

        if index in self._values:
            del self._values[index]

        # Update the keys (indexes) greater than the index deleted
        update_keys = [k for k in self._values if k > index]
        for key in update_keys:
            self._values[key - 1] = self._values.pop(key)
        self.length -= 1
        
    def __str__(self):
        return "[{}]".format(", ".join((str(k) for k in self)))

    def __repr__(self):
        return f"SparseArray({self.__len__()})"

    def __iter__(self):
        return (self._values.get(index, 0) for index in range(self.__len__()))

    def __contains__(self, value):
        if value == self.sparse_value:
            return len(self._values) < self.__len__()
        
        return value in self._values.values()
