
##  String Stripping and Justifying

# Task: Given the string s, use string methods to:
    # - Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
    # - Left justify with '*': left justify the string within a field of width 20, using * as the fill character.
    # - Right justify with '*': right justify the string within a field of width 20, using * as the fill character.
    
    
s:str ="   Python is fun!   "
# Remove leading and trailing spaces
print(f'Remove leading and trailing spaces:{s.strip()}')

# Remove leading spaces
print(f'Remove leading spaces:{s.lstrip()} hlo')
# Remove trailing spaces
print(f'Remove trailing spaces:{s.rstrip()}')
f = "Python is fun!"
center_aligned_string = f.center(40, '=')
print(center_aligned_string)    
right_aligned_string = f.rjust(20, '*')
print(right_aligned_string)    
l = "Python!"

left_aligned_string = l.ljust(10, '-')
print(left_aligned_string)    


