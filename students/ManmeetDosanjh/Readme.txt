def lesser_of_two_evens(a,b):
    if (a and b) % 2 == 0:
        return min(a,b)
    else:
        return max(a,b)