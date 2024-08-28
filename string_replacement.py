# String Replacement

# Task: Given the string s, use string methods to:
# Replace "Python" with "Java": substitute "Python" with "Java".

s:str ="I love programming in Python"
print(s)
# s.replace(old, new , count)
rep = s.replace("Python","Java",-1)
print(f'Original text: {s}\n Replaced text: {rep}')