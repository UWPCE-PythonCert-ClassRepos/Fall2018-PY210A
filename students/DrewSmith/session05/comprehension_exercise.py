"""
Comprehension exercise solutions
"""
from collections import defaultdict


def count_evens(nums):
    """
    Return number of even integers in nums

    :param nums: sequence of integers
    """
    return len([num for num in nums if num % 2 == 0])


def print_dict(food_prefs):
    """
    Print a dictionary using a format string

    :param food_prefs: food pref dictionary to print
    """    
    print("{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta".format(**food_prefs))


def hex_dict():
    """
    Generate a dictionary using integers with hex version values
    """
    return {num: hex(num) for num in range(16)}


def dict_count_a(input_dict):
    """
    Create dictionary of input_dict value 'a' count

    :param dict_count_a: dictionary to read value 'a's
    """
    return {k: v.count('a') for k, v in input_dict.items()}

def set_divisors(nums, divisors):
    """
    Create a list of sets of divisors for an integer set

    :param nums: set of integers

    :param divisors: set of integers that are divisors for num list
    """
    # first attempt with dict loop
    # return_dict = {}
    # for divisor in divisors:
    #     return_dict[divisor] = {num for num in nums if num % divisor == 0}
    # return return_dict

    # Build dictionary of divisors/set values with comprehension...sort of
    # return_dict = {}
    # { return_dict.setdefault(divisor, set()).add(num) for divisor in divisors for num in nums if num % divisor == 0 }
    # return return_dict

    # One liner dictionary
    return { divisor: { num for num in nums if num % divisor == 0 } for divisor in divisors }

    # One-liner list of sets
    # return [ { num for num in nums if num % divisor == 0 } for divisor in divisors ]



if __name__ == '__main__':
    assert count_evens([2, 1, 2, 3, 4]) == 3
    assert count_evens([2, 2, 0]) == 3
    assert count_evens([1, 3, 5]) == 0
    food_prefs = {"name": "Chris",
              "city": "Seattle",
              "cake": "chocolate",
              "fruit": "mango",
              "salad": "greek",
              "pasta": "lasagna"}
    print_dict(food_prefs)
    print(hex_dict())
    print(dict_count_a(food_prefs))
    print(set_divisors(range(21), {2, 3, 4}))