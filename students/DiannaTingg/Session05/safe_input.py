# Lesson 05 Exercise: Exceptions Lab

# The input() function can generate two exceptions: EOFError or KeyboardInterrupt on end-of-file(EOF) or canceled input.
# Create a wrapper function that returns None rather rather than raising these exceptions, when the user enters
# ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.


def safe_input(test_input):
    try:
        good_input = input(test_input)
        return good_input
    except (EOFError, KeyboardInterrupt):
        return None


if __name__ == "__main__":
    response = safe_input("Type something: ")
    if response is None:
        print("Error. You canceled input")
    else:
        print(f"You typed {response}")
