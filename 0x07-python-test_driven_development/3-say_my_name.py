def say_my_name(first_name, last_name=""):
    """Prints a formatted string with the given first and last names.

    Args:
        first_name (str): The first name.
        last_name (str): The last name (optional, defaults to an empty string).

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = f"My name is {first_name} {last_name}"
    print(full_name)
