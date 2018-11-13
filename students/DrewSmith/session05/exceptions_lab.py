def safe_input(prompt):
    """
    Return user input or None if error occurs

    :param prompt: User prompt to display
    """
    try:
        return input(prompt)
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None

print(safe_input("I'll print the text you enter here => "))