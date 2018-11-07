def make_chocolate(small, big, goal):
	big_fit = goal //5

	big_in_box = min(big, big_fit)

	in_box = big_in_box * 5
	space_left = goal - in_box

	if small < space_left:
		return -1
	else:
		return space_left

print(__name__)

if __name__ == "__main__":
	assert make_chocolate(4,1,9) == 4, "a fail message"
	assert make_chocolate(4,1,10) == -1
	assert make_chocolate(4,1,7) == 2
	print("All assertions passed")