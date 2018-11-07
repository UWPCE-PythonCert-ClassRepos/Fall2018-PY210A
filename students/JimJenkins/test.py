
def thirds(seq):
    l = seq
    length = len(l) // 3
    l_first = l[:len(l) // 3]
    l_last = l[-(length):]
    l_middle = l[len(l_first):-(len(l_last))]
    l_new = l_last + l_first + l_middle
    return l_new

a_tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
a_string2 = 'aabbccddeeffgghh'

print(thirds(a_tuple2))
print(thirds(a_string2))