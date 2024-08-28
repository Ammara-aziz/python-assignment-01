# Formatted String Interpolation

# Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.
# name:str = "Alice"
# age:int = 30
# city:str = "New York"
# Instructions: Use an f-string to create a sentence in the format: "Alice is 30 years old and lives in New York."


# Define the variables

employee_name : str = "Joji Busri"
position : str = "Senior Developer"
department : str = "IT"

# Use f-string for interpolation
sentence = f"{employee_name} is a {position} in {department} department."

# Print the sentence
print(sentence)
