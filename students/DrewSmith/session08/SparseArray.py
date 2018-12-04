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
        self._values[self.length] = value
        self.length += 1

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if isinstance(index, slice):
            return list(self)[index]
        else:
            if abs(index) > (self.length + 1):
                raise IndexError("Index greater than length")
            if index < 0:
                index = self.length - abs(index)
            
            return self._values.get(index, self.sparse_value)

    def __setitem__(self, key, value):
        if abs(key) > (self.length + 1):
            raise IndexError("Index greater than length")
        if key < 0:
            key = self.length - abs(key)

        if value == self.sparse_value:
            if value in self._values:
                del self._values[key]
        else:
            self._values[key] = value

    def __delitem__(self, index):
        if abs(index) > (self.length + 1):
            raise IndexError("Index greater than length")
        if index < 0:
            index = self.length - abs(index)

        if index in self._values:
            del self._values[index]

        update_keys = [k for k in self._values if k > index]
        for k in update_keys:
            self._values[k - 1] = self._values.pop(k)
        self.length -= 1
        
    def __str__(self):
        return "[{}]".format(", ".join((str(k) for k in self)))

    def __repr__(self):
        return f"SparseArray({self.length})"

    def __iter__(self):
        return (self._values.get(k, 0) for k in range(self.length))

    def __contains__(self, value):
        if value == self.sparse_value:
            return len(self._values) < self.length
        
        return value in self._values.values()
