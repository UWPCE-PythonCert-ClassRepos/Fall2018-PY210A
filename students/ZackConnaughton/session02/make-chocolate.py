def make_chocolate(small, big, goal):
    big_fit = goal // 5

    big_in_box =min(big, big_fit)
    left = goal - (big_in_box * 5)

    if small < left:
        return -1
    else:
        return left

#if run in the editor, test the assertions
if __name__ = "__main__"
    assert make_chocolate(4,1,9) == 4
    assert make_chocolate(4,1,10) == -1
    assert make_chocolate(4,1,7) == 2
    print("All assertions passed")
