#!/home/dan/cert/scripts/Fall2018-PY210A/students/DanCornutt/session03 Python3

"""
This module experiments with slicing of a sequence.

with the first and last items exchanged.
with every other item removed.
with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
with the elements reversed (just with slicing).
with the last third, then first third, then the middle third in the new order.

"""

def exchange(seq):
    return seq[-1] + seq[1:-1] + seq[0]

def other(seq):
    return seq[::2]

def combo4(seq):
    if len(seq) < 8:
        return "This sequence is too short, please reassign to large sequence."
    else:
        return seq[:4] + seq[4:-4:2] + seq[-4:]

def rev(seq):
    return seq[::-1]

def third(seq):
    if len(seq) % 3:
        return "The squence is not divisible by 3 please redefine sequence!"
    else:
        thrd = len(seq)/3
    return seq[thrd:] + seq[:thrd]

if __name__ == "__main__":

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)
