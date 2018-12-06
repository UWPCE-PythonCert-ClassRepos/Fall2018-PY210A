"""
Lesson 08 Exercise: Sparse Array
Emulate a built-in class
A sparse array is a large array of data that holds mostly zeros
It is more efficient to only store the values that are non-zero
However, you want it to look like a regular array in user code
This is a 1 dimensional sparse array, but feel free to make it 2D for an extra challenge
"""


class SparseArray:
    def __init__(self, values):
        self.size = len(values)
        # Dictionary to hold values that are not zero
        self.values = {index: value for index, value in enumerate(values) if value != 0}

    # Or, you can pass in a specified length and it will return an empty array
    @classmethod
    def from_length(cls, length):
        return cls([0 for i in range(length)])

    def __len__(self):
        return self.size

    def __str__(self):
        return str([self.values[i] if i in self.values else 0 for i in range(self.size)])

    def __eq__(self, other):
        try:
            if self.values == other.values:
                return True
        except AttributeError:
            return False

    def __add__(self, other):
        return self + other

    def __sub__(self, other):
        return self - other

    def convert_neg_index(self, index):
        return self.size + index

    def __getitem__(self, index):
        s_dict = {}
        try:
            s_length = index.stop - index.start
        except AttributeError:
            pass
        if isinstance(index, slice):
            if index.step is None:
                # Slice with start and stop only

                for i in range(index.start, index.stop):
                    if i in self.values:
                        s_dict[(i - index.start)] = self.values[i]

            else:
                s_length = s_length // index.step

                for i in range(index.start, index.stop, index.step):
                    if i in self.values:
                        s_dict[(i - index.start) / index.step] = self.values[i]

            s_array = SparseArray.from_length(s_length)
            s_array.values = s_dict
            return s_array

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
        if index >= self.size or -index > self.size:
            raise IndexError("That index is out of range.")

        if index < 0:
            index = self.convert_neg_index(index)

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
