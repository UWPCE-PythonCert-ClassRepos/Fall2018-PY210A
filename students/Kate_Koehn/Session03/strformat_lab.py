#task one - pass into a string ints in tuple using .format
n = (2, 123.4567, 10000, 12345.67)
print("file_{:03d}: {:.2f}, {:.2E}, {:.2E}".format(*n))

#task two - alternate type of formatting
n = (2, 123.4567, 10000, 12345.67)
print("file_%03d: %.2f, %.2E, %.2E" % (n))

#task three
def formatter(tup):
    return "the {} numbers are: {:*}".format(len(tup), *tup)

n = (2, 123.4567, 10000, 12345.67)
formatter(n)