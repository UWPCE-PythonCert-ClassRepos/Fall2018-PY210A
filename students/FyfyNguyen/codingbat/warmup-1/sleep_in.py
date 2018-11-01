# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# def sleep_in(weekday, vacation):
#     if weekday == True and vacation == False:
#         return False
#     else:
#         return True


# Better Solution
# def sleep_in(weekday, vacation):
#     return not (weekday == True and vacation == False)


# Even better solution
# def sleep_in(weekday, vacation):
#     return (not weekday) or vacation