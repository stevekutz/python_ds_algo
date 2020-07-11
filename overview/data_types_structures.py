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

# ################################################################
# ## Sequences - ordered sets of obj indexed by non-negative integers
# # examples are string, list, tuple, range   (only list is mutable)
# # immutable seq methods do not change orig, but return a modified version

# list1 = [1, 2, 3]
# list2 = [10, 11, 12] 

# # concatenate two lists
# list3 = list1 + list2
# print(f' lsit 3 is {list3}')   

# list2.extend(list1)
# print(f' using extend {list2}')  # using extend [10, 11, 12, 1, 2, 3]

#  # the result of this is None, nothing returned, but list1 is now redefined
# list4 = list1.extend(list2) 
# print(f' {list4} ')  # None

# # unpacks variables from list1 into v1, v2, v3
# # number of variables MUST match match number of elements in list
# list4 = ['a', 'b', 'c']
# v1, v2, v3 = list4
# print(f'va: {v1}, v2: {v2}, v3: {v3}') # va: a, v2: b, v3: c


################################################################
# tuples - immutable comma seperated sequences of obj
# exclosing ( ) are optional but customary
# tuples are hashable, easy to sort and use as keys in dictionary
# are better for managing elements that are different data types
# lists are better when of same type

tupl1 = (True, False)
print(f' tupl1 = {tupl1}')

# tupl1 variable can be re-asssigned
tupl1 = (False, True)
print(f' tupl1 = {tupl1}') 

# using tuple to swap
x,y = tupl1
print(f' original x: {x}   y: {y} ')

x,y = y,x
print(f' swapped is x: {x}   y: {y} ')



# can be declared without parenthesis, called `packing`
tupl2 = 1, 2, 'A'

# unpacking a tuple
val1, val2, val3 = tupl2
print(f' val1: {val1}  val2: {val2}  val3: {val3}')  # val1: 1  val2: 2  val3: A

# concatenating a tuple
tupl3 = tupl1 + tupl2
print(f'tupl3 is {tupl3}')   # tupl3 is (False, True, 1, 2, 'A')

# concatenating a tuple with zip, use the tuple() function to read the tuple
new_tuple = zip(tupl1, tupl2)
print(f' concatenated tuple using zip {tuple(new_tuple)}')

# slicing a tuple
for val in tupl3[3:5]:
    print(f' val is {val}')
#  val is 2
#  val is A

# declaring with only 1 element, MUST USE COMMA
not_tuple = ("value")
print(f' not_tuple type is {type(not_tuple)} ')

true_tuple = ("value", )
print(f' true_tuple type is {type(true_tuple)} ')

# nested tuples
nested_tuple = (11, 200, ('a', 'b', 'c'))

for val in nested_tuple:
    print(f' not nested is: {val} ')
    if isinstance(val, tuple):
        for nested in val:
            print(f'  \t nested val is {nested}')        

#  not nested is: 11 
#  not nested is: 200 
#  not nested is: ('a', 'b', 'c') 
#          nested val is a
#          nested val is b
#          nested val is c


# accessing with index
print(f' val at index 1 is {nested_tuple[1]} of tuple length {len(nested_tuple)}')
#  val at index 1 is 200 of length 3

print(f' val at index -1 is the last item {nested_tuple[-1]}')  # val at index -1 is the last item ('a', 'b', 'c')

# finding index of tuple element value
print(f' index of tuple element 200 is {nested_tuple.count(200)}')    # 1

# verify is value is in tuple
print(f' 5 is in nested_tuple {5 in nested_tuple}')    # False

# comparing tuples

tup1 = ( 1, 14)
tup2 = ( 2, 18)
tup3 = (1, 8, 1)
tup4 = (1, 14, 1)

print(f' tup1 > tup2  {tup1 > tup2}')   # False 14 is not > 18
print(f' tup1 > tup3  {tup1 > tup3}')   # True, because 2nd elem  14 > 8, length of rest does not matter
print(f' tup1 > tup4  {tup1 > tup4}')   # False because all elements match but tup4 has more elements

for item1, item2 in tup1, tup2:
    print(f'item 1 > item2 {item1 > item2}')
  # this does not work as planned,
  # item1, item2 are unpacked from tup1 and compared   1 > 14    False
  # item1, item2 are then unpacked from tup2 and compared 2 > 18   False
