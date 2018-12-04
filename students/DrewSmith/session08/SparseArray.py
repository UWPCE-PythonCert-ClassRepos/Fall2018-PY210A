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

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if isinstance(index, slice):
            return list(self)[index]
        else:
            if abs(index) > (self.__len__() + 1):
                raise IndexError("Index greater than length")
            if index < 0:
                index = self.__len__() - abs(index)
            
            return self._values.get(index, self.sparse_value)

    def __setitem__(self, index, value):
        if abs(index) > (self.__len__() + 1):
            raise IndexError("Index greater than length")
        if index < 0:
            index = self.__len__() - abs(index)

        if value == self.sparse_value:
            if value in self._values:
                del self._values[index]
        else:
            self._values[index] = value

    def __delitem__(self, index):
        if abs(index) > (self.__len__() + 1):
            raise IndexError("Index greater than length")
        if index < 0:
            index = self.__len__() - abs(index)

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
