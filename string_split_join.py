

# String Splitting and Joining

# Task: Given the string s, use string methods to:

    # - Split into a list: break the string into a list of substrings based on the delimiter ,.

s:str ="apple,banana,cherry,dates"

# * var.split(separator, maxsplit)

d:list =s.split(",")
print(d)
   # Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.

#  *  separator.join(iterable)
join_str = " ".join(d)
print(join_str)

parts = ["2024", "07", "30"]
joined_string = "-".join(parts)
print(joined_string)