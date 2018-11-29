"""Emulate a list in a custom class"""


class SparseArray:
    """Create array objects that act as lists"""

    def __init__(self, seq):
        """Establish variable for sequence argument"""
        self.seq = seq

    def __str__(self):
        """Return list in string form when instance is printed"""
        return str(self.seq)

    def __len__(self):
        """Return length of array"""
        return len(self.seq)

    def __getitem__(self, pos):
        """Allow for accessing list by index and slicing"""
        return self.seq[pos]

    def append(self, value):
        """Append to end of array"""
        self.seq.append(value)
        return self.seq

    def delete(self, pos):
        """Delete item at given index"""
        del self.seq[pos]
        return self.seq
 
    def insert(self, pos, value):
        """Insert value at particular index.
        If index is out of range, insert to
        either beginning or end of array"""
        if pos > len(self.seq):
            self.seq[-1] = value
        elif pos < -len(self.seq):
            self.seq[0] = value
        else:
            self.seq[pos] = value


sa = SparseArray([1, 2, 3, 4, 5, 6])
sa.insert(-800, "more")
