# Convert an integer to its binary representation

# Task: Given an integer num
# Obtain the binary representation of num


# integer to its binary -> bin function , prefix '0b -> number is in binary format
def integer_to_binary(num:int) -> str:
    return bin(num)
num = 45
binary_rpresntation = integer_to_binary(num)
print(f'Binary Representation of {num} is {binary_rpresntation}')

