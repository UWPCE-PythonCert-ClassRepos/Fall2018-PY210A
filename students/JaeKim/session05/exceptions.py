def safe_input():
    try:
        get_input = input ("=> give an input")
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
    return get_input

safe_input()
