"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:
"""
# with the first and last items exchanged
def exchange_first_last(seq):
    n = len(seq)
    if n <= 1:
        return seq
    first = seq[0:1]
    last = seq[n-1:n]
    mid = seq[1:-1]
    return last + mid + first
print(exchange_first_last((1,)))

# with every other item removed
# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence
# with the elements reversed (just with slicing)
# with the third, then first third, then the middle third in the new order



