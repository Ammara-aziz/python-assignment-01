# Round floating-point numbers

# Task: Given a floating-point number value

def round_floating_point(value: float) -> tuple:
    """
    Args:
        value: The floating-point number to be rounded.

    Returns:
        A tuple containing the rounded integer and the rounded value to two decimal places.
    """
    # Round to the nearest integer
    rounded_integer = round(value)
    
    # Round to two decimal places
    rounded_two_decimal = round(value, 2)
    
    return rounded_integer, rounded_two_decimal

# Example usage:
value = 12.34567
rounded_integer, rounded_two_decimal = round_floating_point(value)
print(f"The value {value} rounded to the nearest integer is {rounded_integer}")
print(f"The value {value} rounded to two decimal places is {rounded_two_decimal}")
