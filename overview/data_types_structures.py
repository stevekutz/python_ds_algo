# ## None
# # Immutatable & like `null`, absence of a value
# # returned by False boolean expressions
# # objects return None when there is nothing to return

# def return_none():
#     x = 1

# # nothing to return returns None
# print(f' {return_none()}')  # None

# # Numeric Types
# int_val = 3
# float_val = 3.14
# complex_val = 2 + 6j
# bool_val = False

# num_types = [int_val, float_val, complex_val, bool_val]
# for val in num_types:
#     print(f'type of {val} is {type(val)}')
#     if isinstance(val, complex):
#         print(f' \t real part: {val.real} imag part: {val.imag}')

################################################################
## Sequences - ordered sets of obj indexed by non-negative integers
# examples are string, list, tuple, range   (only list is mutable)
# immutable seq methods do not change orig, but return a modified version

list1 = [1, 2, 3]
list2 = [10, 11, 12] 

# concatenate two lists
list3 = list1 + list2
print(f' lsit 3 is {list3}')   

list2.extend(list1)
print(f' using extend {list2}')  # using extend [10, 11, 12, 1, 2, 3]

 # the result of this is None, nothing returned, but list1 is now redefined
list4 = list1.extend(list2) 
print(f' {list4} ')  # None

# unpacks variables from list1 into v1, v2, v3
# number of variables MUST match match number of elements in list
list4 = ['a', 'b', 'c']
v1, v2, v3 = list4
print(f'va: {v1}, v2: {v2}, v3: {v3}') # va: a, v2: b, v3: c