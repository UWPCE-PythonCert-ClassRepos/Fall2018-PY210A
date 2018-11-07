# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed <= 65:
            return 0
        elif speed >= 66 and speed <= 85:
            return 1
        else:
            return 2
    else:
        if speed <= 60:
            return 0
        elif speed >= 61 and speed <= 80:
            return 1
        else:
            return 2

# # Shorter solution
# def caught_speeding(speed, is_birthday):
#     if is_birthday:
#         speed -=5
#     elif speed <= 60:
#         return 0
#     elif 60 < speed <= 80:
#         return 1
#     return 2