import random

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

# tupl1 = (True, False)
# print(f' tupl1 = {tupl1}')

# # tupl1 variable can be re-asssigned
# tupl1 = (False, True)
# print(f' tupl1 = {tupl1}') 

# # using tuple to swap
# x,y = tupl1
# print(f' original x: {x}   y: {y} ')

# x,y = y,x
# print(f' swapped is x: {x}   y: {y} ')



# # can be declared without parenthesis, called `packing`
# tupl2 = 1, 2, 'A'

# # unpacking a tuple
# val1, val2, val3 = tupl2
# print(f' val1: {val1}  val2: {val2}  val3: {val3}')  # val1: 1  val2: 2  val3: A

# # concatenating a tuple
# tupl3 = tupl1 + tupl2
# print(f'tupl3 is {tupl3}')   # tupl3 is (False, True, 1, 2, 'A')

# # concatenating a tuple with zip, use the tuple() function to read the tuple
# new_tuple = zip(tupl1, tupl2)
# print(f' concatenated tuple using zip {tuple(new_tuple)}')

# # slicing a tuple
# for val in tupl3[3:5]:
#     print(f' val is {val}')
# #  val is 2
# #  val is A

# # declaring with only 1 element, MUST USE COMMA
# not_tuple = ("value")
# print(f' not_tuple type is {type(not_tuple)} ')

# true_tuple = ("value", )
# print(f' true_tuple type is {type(true_tuple)} ')

# # nested tuples
# nested_tuple = (11, 200, ('a', 'b', 'c'))

# for val in nested_tuple:
#     print(f' not nested is: {val} ')
#     if isinstance(val, tuple):
#         for nested in val:
#             print(f'  \t nested val is {nested}')        

# #  not nested is: 11 
# #  not nested is: 200 
# #  not nested is: ('a', 'b', 'c') 
# #          nested val is a
# #          nested val is b
# #          nested val is c


# # accessing with index
# print(f' val at index 1 is {nested_tuple[1]} of tuple length {len(nested_tuple)}')
# #  val at index 1 is 200 of length 3

# print(f' val at index -1 is the last item {nested_tuple[-1]}')  # val at index -1 is the last item ('a', 'b', 'c')

# # finding index of tuple element value
# print(f' index of tuple element 200 is {nested_tuple.count(200)}')    # 1

# # verify is value is in tuple
# print(f' 5 is in nested_tuple {5 in nested_tuple}')    # False

# # comparing tuples

# tup1 = ( 1, 14)
# tup2 = ( 2, 18)
# tup3 = (1, 8, 1)
# tup4 = (1, 14, 1)

# print(f' tup1 > tup2  {tup1 > tup2}')   # False 14 is not > 18
# print(f' tup1 > tup3  {tup1 > tup3}')   # True, because 2nd elem  14 > 8, length of rest does not matter
# print(f' tup1 > tup4  {tup1 > tup4}')   # False because all elements match but tup4 has more elements

# for item1, item2 in tup1, tup2:
#     print(f'item 1 > item2 {item1 > item2}')
#   # this does not work as planned,
#   # item1, item2 are unpacked from tup1 and compared   1 > 14    False
#   # item1, item2 are then unpacked from tup2 and compared 2 > 18   False


# ############################################
# # dictionaries - stoes seq of mapped key:value pairs
# # the ONLY built in mapping type
# #  `in` with dictionaries uses a hashing function and searches very quickly

# ## WAYS TO CREATE dictionary
# # using zip to create a dict
# dict1 = dict(zip('HelloWorld', range(10)))
# print(dict1)     # {'H': 0, 'e': 1, 'l': 8, 'o': 6, 'W': 5, 'r': 7, 'd': 9}

# # directly declare dict
# dict2 = {'first': '1', 'second': '2', 'third': '3', 'fourth': '4'}
# print(dict2)   # {'first': '1', 'second': '2', 'third': '3', 'fourth': '4'}

# # use the `dict` keyword
# dict3 = dict({'one': '1', 'two': '2', 'three': '3'})
# print(dict3)     # {'one': '1', 'two': '2', 'three': '3'}

# # APPEND to dict3
# dict3['four'] = 4
# print(f' Appended  dict3  {dict3} ')  # Appended  dict3  {'one': '1', 'two': '2', 'three': '3', 'four': 4}

# # use UPDATE to ADD MULTIPLE key:value pairs to dict3
# dict3.update({'five': 5, 'six': 6})
# print(f' update adds kv pairs {dict3}')  # update adds kv pairs {'one': '1', 'two': '2', 'three': '3', 'four': 4, 'five': 5, 'six': 6}

# # use UPDATE change a value in dict
# dict3.update(six = -66)
# print(f" six changed {dict3['six']}")    # six changed -66

# # Verify if key exists (does not work for values)
# #  `in` with dictionaries uses a hashing function and searches very quickly
# print(f" {'two' in dict3}   ")     # True
# print(f" {'nine' in dict3} ")      # False 

# # COPY by REFERENCE (not same memory location)
# dict5 = dict3.copy()
# print(f' id dict1: {id(dict1)} id dict5: {id(dict5)}')  # should show different mem location

# # Creates new dict from defined set of keys and initializes to new value
# keys = {'a', 'b', 'c'}

# dict6 = dict.fromkeys(keys, 0)
# print(dict6)   # {'b': 0, 'c': 0, 'a': 0}

# # get method returns the value of key if it exists, return None otherwise
# val = dict5.get('two')
# print(f' get method returns value: {val}')  # get method returns value: 2


# print(dict5)
# # returns value at key and removes k,v from dict
# dict_kv = dict5.pop('six')
# print(f' dict5 now {dict5}')  #
# print(f' removed from dict5 {dict_kv}')  # removed from dict5 -66

# # removes last inserted item from dict5 & returns as a tuple
# removed_tup = dict5.popitem()
# print(f' removed is {removed_tup} {type(removed_tup)}') # removed is ('five', 5) <class 'tuple'>
# print(f' dict5 now {dict5}') # dict5 now {'one': '1', 'two': '2', 'three': '3', 'four': 4}

# # return value of key if it exists, if not found, adds kv to dict
# ret_kv = dict5.setdefault('one')
# print(f' key is found, value is {ret_kv}')

# ret_kv2 = dict5.setdefault('five', '5')
# print(f' key not found, kv added, value is {ret_kv2}')
# print(f' dict5 is now {dict5}')

# # the items() method returns a tuples of the key value pairs
# dict5_items = (dict5.items())
# print(f' type is {type(dict5.items())}' )  #  type is <class 'dict_items'>
# print(f' {dict5.items()}')        #  dict_items([('one', '1'), ('two', '2'), ('three', '3'), ('four', 4), ('five', '5')])
# print(f' dict5_items is {dict5_items} ')    #   dict5_items is dict_items([('one', '1'), ('two', '2'), ('three', '3'), ('four', 4), ('five', '5')]

# # Verifying data structure
# for item in dict5.items():
#     print(f' item is {item} ')
#     print(f' type is {type(item)}')

# # item is ('one', '1') 
# # type is <class 'tuple'>
# # item is ('two', '2') 
# # type is <class 'tuple'>
# # item is ('three', '3') 
# # type is <class 'tuple'>
# # item is ('four', 4) 
# # type is <class 'tuple'>
# # item is ('five', '5') 
# # type is <class 'tuple'>

# ## dict6 = {'b': 0, 'c': 0, 'a': 0}
# # get all keys
# keys = dict6.keys()
# print(f' all keys {keys}  of type {type(keys)}')  # all keys dict_keys(['c', 'b', 'a'])  of type <class 'dict_keys'>

# # get all values
# vals = dict6.values()
# print(f' all values {vals} of type {type(vals)} ') # all values dict_values([0, 0, 0]) of type <class 'dict_values'> 


# # sorting
# dict7 = dict({'one': 1, 'two': 2, 'three': 3})

# # sorts by key
# sort_key = sorted(list(dict7))
# print(f' sorted  by key {sort_key}  type {type(sort_key)} ') #  sorted  by key ['one', 'three', 'two']  type <class 'list'> 

# sort_vals = sorted(list(dict7.values()))
# print(f' sort_vals {sort_vals}  type  {type(sort_vals)}')   #   sort_vals [1, 2, 3]  type  <class 'list'>

# # sorting keys by dictionary value
# sort_keys2 = sorted(list(dict7), key = dict7.__getitem__)
# print(sort_keys2)    # ['one', 'two', 'three']

# # sorting vals by dictionary key
# sort_vals2 = [value for (key,value) in sorted(dict7.items())] 
# print(sort_vals2)   # [1, 3, 2]

# sort_vals3 = [value for (key, value) in sorted(dict7.items())]
# print(sort_vals3)  # [1, 3, 2]

# dict8 = {'one': 'uno', 'two': 'deux', 'three': 'trois'}

# sort_vals4 = [dict8[i] for i in sorted(list(dict7), key = dict7.__getitem__)]
# # the numeric values from dict7 and used to sort the text values in dict8
# print(sort_vals4)   # ['uno', 'deux', 'trois']


# # Read in file and count occurrences of words
# def wordcount(fname):
#     try:
#         fhand=open(fname)
#     except:
#         print(f" Cannot open file  {fname}" )  
#         exit()

#     count = dict() 
#     for line in fhand:
#         words = line.split()
#         for word in words:
#             if word not in count:
#                 count[word] = 1
#             else:
#                 count[word] +=1
#     return (count)                

# count = wordcount("overview/text.txt")

# filtered = {key:value for key,value in count.items() if value < 50 and value > 20  } 
# print(filtered)   # {'was': 42, 'of': 33, 'and': 42, 'she': 48, 'it': 32, 'a': 40}

# filt_sort = [sorted(list(filtered.values()), reverse = True)]

# print(filt_sort)  # [[48, 42, 42, 40, 33, 32]]


# list of dictionaries, enumerate to get index
list_dict = [{"first": "one", "second": "two", "third": "three"}]
for item in list_dict:
    for index, (k,v) in enumerate(item.items()):
        print(f' at index {index:<5} key is \t {k:<15} value is \t {v:<10}')

#########################################################
## Sets - unordered collections of uniue items
# mutable, set iteslef can have items added, removed
# the items themselves MUST be immutable
# CANNOT use slicing or indexing
# `frozen set` is immutable, `set` obj is mutable
# Cannot use mutable obj like list or dictionary in set
# tuple is valid in sets

tup_set = {(1,2,3), 4, 5, ('A', 'B')}
print(tup_set)   # {(1, 2, 3), 4, 5, ('A', 'B')}

for item in tup_set:
    print(item)

# (1, 2, 3)
# 4
# 5
# ('A', 'B')

# bad_set = {{'a': 1}}  # TypeError: unhashable type: 'dict'

# bad_set = {1, 2, [3,4,5]}    # TypeError: unhashable type: 'list'



# Create an empty set
a_set = set()
b_set = set()
c_set = set()      # mutable, but not hashable
a_froz_set = frozenset()  # not mutable, but hashable


# add to a set
for item in range(1,11):
    a_set.add(item)
    if item > 5:
        b_set.add(item)
print(f' a_set: {a_set} with length {len(a_set)} & type {type(a_set)}')
print(f' b_set is {b_set}')
 # a_set: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} with length 10 & type <class 'set'>
 # b_set is {6, 7, 8, 9, 10}

# mutable sets CANNOT have sets as elem
# a_set.add(b_set)   # TypeError: unhashable type: 'set'

# Create frozen set
b_froz_set = frozenset(b_set)
print(f'b_frozen_set is {b_froz_set}')  # b_frozen_set is frozenset({6, 7, 8, 9, 10})

# adding a frozen set to a set
new_set = {0,'a'}
new_set.add(b_froz_set)
print(f'new_set is now {new_set} ')


# return what is `a_set` that is not in `b_set`
only_in_a = a_set.difference(b_set)
print(only_in_a)    # {1, 2, 3, 4, 5}

# return items that are in both sets
diff = a_set.intersection(b_set)
print(diff)         # {6, 7, 8, 9, 10}

# return True only if both ets have no elem in common
print(a_set.isdisjoint(b_set))   # False

# return True only if all `b_set` elem are also in `a_set`
print(b_set.issubset(a_set))      # True
print(a_set.issuperset(b_set))    # True

print(c_set.issubset(a_froz_set))    # True since both are empty

# return set of elem that in `d_set` or `e_set` but not in both
d_set = {1, 2, 5}
e_set = {5, 6, 7}
print(d_set.symmetric_difference(e_set))   # {1, 2, 6, 7}

# return set of elements that are either d_set or e_set
print(d_set.union(e_set))

# remove elements in d_set that are also in e_set
du = (d_set.difference_update(e_set))
print(du)    # None
print(d_set)  # {1, 2}

# remove item from set
r = d_set.remove(1)
print(r)
print(d_set)

r = d_set.discard(2)
print(r)
print(d_set)   # set()

# update `d_set` with iterable obj
d_set.update({1,2,3})
print(d_set)

# remove item from `d_set` and return it
pop_val = d_set.pop()
print(f' popval is {pop_val} and d_set is now {d_set}')

d_set = {2, 3, 4, 5}
e_set = {4, 5, 6, 7}
# removes items from `d_set` that are NOT in the intersection of both sets
d_set.intersection_update(e_set)
print(d_set)    # {4, 5}

d_set = {2, 3, 4, 5}
# deletes all elements from `d_set` that are not in symmetic difference set
sym_diff = d_set.symmetric_difference(e_set)
print(sym_diff)  # {2, 3, 6, 7}

# `d_set` is updated with the symmetic difference of `d_set` & `e_set`
d_set.symmetric_difference_update(e_set)
print(d_set)


# use enumerate to identify 'index' location in set
for index, item in enumerate(d_set):
    print(f'index: {index} item {item}')

# print(d_set[0])    #     TypeError: 'set' object is not subscriptable
