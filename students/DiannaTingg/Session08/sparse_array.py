"""
Lesson 08 Exercise: Sparse Array
Emulate a built-in class
A sparse array is a large array of data that holds mostly zeros
It is more efficient to only store the values that are non-zero
However, you want it to look like a regular array in user code
This is a 1 dimensional sparse array, but feel free to make it 2D for an extra challenge
"""

import operator


class SparseArray:
    def __init__(self, values):
        self.size = len(values)
        self.values = {index: value for index, value in enumerate(values) if value != 0}

    @classmethod
    def from_length(cls, length):
        return cls([0 for i in range(length)])

    def __len__(self):
        return self.size

    # Reconstruct full array
    def get_nums(self):
        return [self.values[i] if i in self.values else 0 for i in range(self.size)]

    def __str__(self):
        return str(self.get_nums())

    def __eq__(self, other):
        try:
            if self.values == other.values:
                return True
        except AttributeError:
            if self.get_nums() == other:
                return True
        else:
            return False

    def __add__(self, other):
        return self + other

    def __sub__(self, other):
        return self - other

    def convert_neg_index(self, index):
        return self.size + index

    def __getitem__(self, index):
        try:
            index = operator.index(index)

        # Error means index is a slice
        except TypeError:
            nums = self.get_nums()
            return nums[index]

        # Make sure the index position is valid
        if index >= self.size or -index > self.size:
            raise IndexError("That index number is out of range.")

        if index < 0:
            index = self.convert_neg_index(index)

        try:
            return self.values[index]

        # If the index is not in the dictionary, the value should be 0
        except KeyError:
            return 0

    def __setitem__(self, index, new_value):
        if index >= self.size or -index > self.size:
            raise IndexError("That index is out of range.")

        if index < 0:
            index = self.convert_neg_index(index)

        if new_value != 0:
            self.values[index] = new_value
        else:
            try:
                del self.values[index]
            except KeyError:
                return

    def _shrink_dict(self, index):
        new_dict = {}

        for key in self.values:
            if key < index:
                new_dict[key] = self.values[key]
            else:
                new_dict[key - 1] = self.values[key]

        return new_dict

    def __delitem__(self, index):
        if index < 0:
            index = self.convert_neg_index(index)

        if index >= self.size or -index > self.size:
            raise IndexError("That index is out of range.")

        try:
            del self.values[index]
        except KeyError:
            pass

        self.size -= 1
        self.values = self._shrink_dict(index)

    # Append method
    def append(self, value):
        self.size += 1

        if value != 0:
            self.values[self.size - 1] = value
