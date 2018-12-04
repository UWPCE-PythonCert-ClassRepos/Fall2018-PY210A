#!/usr/bin/env Python3


#Date: October 30, , 2018
#Created by: Carol Farris
#Purpose: Slicing Lab



def swapfirstlast(n):
    """
    print sequence with first and last items exchanged
    :param(n):  sequence to print
    :return: modified sequence
    """
    print (n[-1:] + n[1:-1] + n[:1])
    return (n[-1:] + n[1:-1] + n[:1])


def everyotheritem(n):
    """
    Prints every other item in sequence.
    :param(n):  Sequence to print
    :return: modified sequence
    """
    print(n[1::2])
    return(n[1::2])


def middle_every_other(n):
    print(n[3:-4:2])
    return(n[3:-4:2])


def reverseTheList(n):
    """"
    Returns the reverse of the sequence
    :param(n):  Sequence to reverse
    :return: modified sequence
    """
    print(n[::-1])
    return(n[::-1])


def mixByThirds(n):
    """
    Returns sequence mixed by thirds last, first, middle third
    :param(n): Sequence to mix
    :return: modified sequence
    """
    eachDiv = int(len(n) / 3)
    if len(n) % 3 == 0:
        return(n[(2 * eachDiv): (3 * eachDiv)] +
               n[0: eachDiv] + n[eachDiv: (2 * eachDiv)])
    elif len(n) % 3 == 2:
        return(n[(2 * eachDiv + 1): ((3 * eachDiv) + 2)] +
               n[0: eachDiv] + n[eachDiv: (2 * eachDiv + 1)])
    else:
        return(n[(2 * eachDiv): (3 * eachDiv + 1)] +
               n[0: eachDiv] + n[eachDiv: (2 * eachDiv)])


if __name__ == '__main__':

    myList = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    myString = "Python3Python3Python3Python3"
    myTest = "Together"
    myTest2 = "Python3"

    swapfirstlast(myList)
    swapfirstlast(myString)

    everyotheritem(myList)
    everyotheritem(myString)

    middle_every_other(myList)
    middle_every_other(myString)

    reverseTheList(myList)
    reverseTheList(myString)

    mixByThirds(myList)
    mixByThirds(myString)
    mixByThirds(myTest)
    mixByThirds(myTest2)

    assert swapfirstlast(tuple(myList)) == (13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1)
    assert swapfirstlast(myString) == '3ython3Python3Python3PythonP'
    assert everyotheritem(myList) == (2, 4, 6, 8, 10, 12)
    assert everyotheritem(myString) == 'yhnPto3yhnPto3'
    assert middle_every_other(myList) == (4, 6, 8)
    assert middle_every_other(myString) == 'hnPto3yhnPt'
    assert reverseTheList(tuple(myList)) == (13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    assert reverseTheList(myString) == '3nohtyP3nohtyP3nohtyP3nohtyP'
    assert mixByThirds(tuple(myList)) == (9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8)
    assert mixByThirds(myString) == 'on3Python3Python3Python3Pyth'
    assert mixByThirds(myTest) == 'herToget'
    assert mixByThirds(myTest2) == 'on3Pyth'
