# !/usr/bin/python3


def safe_input(response):
    """
    Return None if user enters ^C or ^D instead of raising
    exceptions EOFError or KeyboardInterrupt.
    """
    try:
        return input(response)
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None


response = safe_input('Say whatever you want here >>> ')
