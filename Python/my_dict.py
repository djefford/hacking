code_name = {"jack": 4098, "sape": 4139, "robb": 2323}
print(type(code_name))
print(code_name)
# You can remove items in the dictionary by using the del keyword.
del code_name["sape"]
print(code_name)
"""
You can update the values of the dictionaries by overriding them.
code_name[‘jack’] = 1212
"""

# The len function returns the number of key-value pairs in the dictionary.
len(code_name)