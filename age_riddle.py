one:str ="hussain" 
two:str = "ahmad" 
three:str = "kamran" 

one_age:int = 21
two_age:int = 27
three_age:int = 47

print(one +  " is",  one_age)
print(two +  " is",  two_age)
print(three +  " is",  three_age)
print("\n")
# Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends.
# Their ages are as follows:
# Anton is 21 years old.
# Beth is 6 years older than Anton.
# Chen is 20 years older than Beth.
# Drew is as old as Chen's age plus Anton's age.
# Ethan is the same age as Chen.
# Your code should store each person's age to a variable and print their names and ages at the end

anton_age = 21
beth_age = anton_age + 6
chen_age = beth_age + 20
drew_age = chen_age + anton_age
ethan_age = chen_age


print(f"Anton is {anton_age}")
print(f"Beth is {beth_age}")
print(f"Drew is {drew_age}")
print(f"Ethan is {ethan_age}")



