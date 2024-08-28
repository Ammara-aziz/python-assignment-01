# Calculate Powers of Numbers.

# Task: Given two integers base and exponent
# Compute base raised to the power of exponent.


def calculate_power(base:int, exponent:int) -> int:
    return base ** exponent

base:int = 3
exponent:int = 4
reso = calculate_power(base, exponent)
print(reso)
