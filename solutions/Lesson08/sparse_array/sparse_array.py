
"""
example of emulating a sequence using slices
"""

import operator

class SparseArray(object):

    def __init__(self, my_array=()):
        self.length = len(my_array)
        self.sparse_array = self._convert_to_sparse(my_array)

    def _convert_to_sparse(self, my_array):
        sparse_array = {}
        for index, number in enumerate(my_array):
            if number:
                sparse_array[index] = number
        return sparse_array

    def __len__(self):
        return self.length

    def __eq__(self, other):
        """
        only equal if they are both SparseArrays,
        and have the same length and elements.
        """
        try:
            return ((self.sparse_array == other.sparse_array) and
                    (self.length == other.length))
        except AttributeError:
            return False

    def __str__(self):

        return ('SparseArray([' +
                ", ".join((f"{self[i]}" for i in range(self.length))) +
                '])')

    __repr__ = __str__

    def __getitem__(self, index):
        # this version supports slicing -- far more complicated
        mini_array = []
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if step is None:
                step = 1
            key = start
            mini_array = []
            while key < stop:
                mini_array.append(self[key])
                key += step
            return self.__class__(mini_array)
        else:
            # makes it an int, even if it's some other
            # type that supports being used as an index
            index = operator.index(index)
            return self._get_single_value(index)

    def _get_single_value(self, key):
        if key >= self.length:
            raise IndexError('array index out of range')
        else:
            return self.sparse_array.get(key, 0)

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            if step is None:
                step = 1
            key = start
            new_values = []
            new_keys = []
            for each in value:
                if key < stop:
                    self[key] = each
                else:
                    # now instead of replacing values, we need to add (a) value(s) in the center,
                    # and move stuff over, probably want to collect all of the changes,
                    # and then make a new dictionary
                    new_values.append(each)
                    new_keys.append(key)
                key += step
            if new_keys:
                self._add_in_slice(new_keys, new_values)
        else:
            index = operator.index(index)
            self._set_single_value(index, value)

    def _set_single_value(self, key, value):
        if key > self.length:
            raise IndexError('array assignment index out of range')
        if value != 0:
            self.sparse_array[key] = value
        else:
            # if the value is being set to zero, we may need to
            # remove a key from our dictionary.
            self.sparse_array.pop(key, None)

    def _add_in_slice(self, new_keys, new_values):
        # sometimes we need to add in extra values
        # any existing values
        # greater than the last key of the new data
        # will be increased by how many
        new_dict = {}
        slice_length = len(new_keys)
        for k, v in self.sparse_array.items():
            if k >= new_keys[-1]:
                # print('change keys')
                # if greater than slice, change key
                new_dict[k + slice_length] = v
            elif k in new_keys:
                # if this is a key we are changing, change it,
                # unless we are changing to a zero...
                new_value = values[new_keys.index(k)]
                if new_value != 0:
                    new_dict[k] = new_value
            else:
                new_dict[k] = v
        # what if our new key was not previously in the dictionary?
        # stick it in now
        for k in new_keys:
            if k not in new_dict.keys():
                new_dict[k] = new_values[new_keys.index(k)]
        # note we don't want to do update, since we need to make sure we are
        # getting rid of the old keys, when we moved the value to a new key
        self.sparse_array = new_dict
        # now we need to increase the length by the amount we increased our array by
        self.length += slice_length

    def __delitem__(self, key):
        # we probably need to move the keys if we are not deleting the last
        # number, use pop in case it was a zero
        if key == self.length - 1:
            self.sparse_array.pop(key, None)
        else:
            # since we need to adjust all of the keys after the one we are
            # deleting, probably most efficient to create a new dictionary
            new_dict = {}
            for k, v in self.sparse_array.items():
                if k >= key:
                    new_dict[k - 1] = v
                else:
                    new_dict[k] = v
            # note we don't want to do update, since we need to make sure we are
            # getting rid of the old keys, when we moved the value to a new key
            self.sparse_array = new_dict
        # length is now one shorter
        self.length -= 1

    def __iter__(self):
        """
        `__iter__` should return an iterator ready to iterate over the
        elements in the array.

        This uses a generator expression to make an iterator

        Clever solution contributed by a student
        """
        return (self.sparse_array.get(index, 0) for index in range(self.length))
