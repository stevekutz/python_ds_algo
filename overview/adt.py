# from collections import deque, ChainMap
import itertools, collections, string



# #################################################
# # Double-ended queues (deques) are mutable lists that allow fast appends & pops on either end
# # CANNOT be directly sliced, but a list can be sliced out

# # create a new deque
# dq1 = deque('newdeque')
# print(f' dq1 is  {dq1} of type {type(dq1)}')
# # dq1 is  deque(['n', 'e', 'w', 'd', 'e', 'q', 'u', 'e']) of type <class 'collections.deque'>


# # add to deque
# dq1.append('R')
# print(dq1)   # deque(['n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R'])

# # add to beginning
# dq1.appendleft('A')
# print(dq1)     # deque(['A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R'])

# # add multiple items to the right
# dq1.extend("CDE")
# print(dq1)   # deque(['A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D', 'E'])

# # add mutliple items to the left, note how order is added on
# dq1.extendleft("123")
# print(dq1)    # deque(['3', '2', '1', 'A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D', 'E'])

# # pop & popLeft remove items from either end & return value removed
# pop1 = dq1.pop()
# print(dq1)   # deque(['3', '2', '1', 'A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D'])
# print(f' popped val is: {pop1}')    # popped val is: E

# pop2 = dq1.popleft()
# print(dq1)  # deque(['2', '1', 'A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D'])
# print(f' poppedLeft val is {pop2}')  # poppedLeft val is 3

# dq2 = deque('012345')
# print(dq2)    # deque(['0', '1', '2', '3', '4', '5'])

# # rotate all values 3 to the right
# dq2.rotate(3)
# print(dq2)    # deque(['3', '4', '5', '0', '1', '2'])

# # rotate all values 1 to the left
# dq2.rotate(-1) 
# print(dq2)    # deque(['4', '5', '0', '1', '2', '3'])

# # slice out part of deque as a list
# sliced = list(itertools.islice(dq2, 2,4))
# print(sliced)    # ['0', '1']

# # create circular buffer
# dq3 = deque([], maxlen = 4)
# for i in range(10):
#     dq3.append(i)
#     print(dq3)

# # deque([0], maxlen=4)
# # deque([0, 1], maxlen=4)
# # deque([0, 1, 2], maxlen=4)
# # deque([0, 1, 2, 3], maxlen=4)
# # deque([1, 2, 3, 4], maxlen=4)
# # deque([2, 3, 4, 5], maxlen=4)
# # deque([3, 4, 5, 6], maxlen=4)
# # deque([4, 5, 6, 7], maxlen=4)
# # deque([5, 6, 7, 8], maxlen=4)
# # deque([6, 7, 8, 9], maxlen=4)    

######################################################################################
# ChainMap class allows linking of dictionaries into one ordered list of dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5}

# Create Chainmap
## if we imported as `from collections import deque, ChainMap`
## wwe would declare as chain_map0 = ChainMap(dict1)

chain_map0 = collections.ChainMap(dict1)
print(f' chain_map0 is {chain_map0.maps}')

chain_map = collections.ChainMap(dict1, dict2)
print(f'chain_map is {chain_map}')  # chain_map is ChainMap({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5})

print(f' \t >>>  dict1 is {dict1}')

# return a list of ChainMap mappings
print(chain_map.maps)   # [{'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}]

# return all keys
print(chain_map.keys())    # KeysView(ChainMap({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}))

# return all keys in a list
print(list(chain_map.keys()))  # ['d', 'e', 'a', 'b', 'c']

# return all values
print(chain_map.values())  # ValuesView(ChainMap({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}))

print(f' \t >>>  dict1 is {dict1}')

# return all values in a list
print(list(chain_map.values()))    # [4, 5, 1, 2, 3]clear

# print out first index
print(f' first value in chain_map is {chain_map.maps[0]} ')

print(f' \t >>>  dict1 is {dict1}')

# change value in first mapping  {'a': 100, 'b': 2, 'c': 3}
# only updates/deletes can be done to first mapping
chain_map['a'] = 100
print(f' changed first chain value  {chain_map.maps}')    # [{'a': 100, 'b': 2, 'c': 3}, {'d': 4, 'e': 5}]


print(f' \t >>>  dict1 is {dict1}')


# try to change value in second mapping
##  >>   This appends to first chain and does not update second chain key of 'e'
##  >>   VERY ODD, this redefines dict1   
# chain_map['e'] = 40
# print(f' tried to change second chain {chain_map.maps}')  # tried to change second chain [{'a': 100, 'b': 2, 'c': 3, 'e': 40}, {'d': 4, 'e': 5}]
# print(f' \t\t >>>  dict1 is {dict1}')

# create child ChainMap with value that overrides parent
chain_map2 = chain_map.new_child({'a': -999})
print(chain_map2.maps)

# print(f' \t >>>  dict1 is {dict1}')

# reverse child ChainMap
print(f' \t >>>  dict1 is {dict1}')
chain_map3 = collections.ChainMap(dict1, dict2)
print(f' chain_map3 is {chain_map3}')

chain_map3.maps = reversed(chain_map3.maps)
print(f'should be reversed {(chain_map3)}')

print("Reversed Chain: " + str(chain_map3))

dict3 = {"A": "apple", "B": "beetle", "C": "cow"}
chain_map4 = collections.ChainMap(dict3)
print(chain_map4)

chain_map4 = chain_map4.new_child({"E": "egg"})
print(f' added E: egg  {chain_map4}')

chain_map4.maps = reversed(chain_map4.maps)

print(f' REVERSED !!!   {chain_map4}')
print("Reversed Chain: " + str(chain_map4))

con_code1 = {'India' : 'IN', 'China' : 'CN'}
con_code2 = {'France' : 'FR', 'United Kingdom' : 'GB'}
code = {'Japan' : 'JP'}
chain = collections.ChainMap(con_code1, con_code2)
print("Initial Chain: " + str(chain.maps))
chain = chain.new_child(code)    #Insert New Child
print("Chain after Inserting new Child: " + str(chain.maps))
chain.maps = reversed(chain.maps)
print("Reversed Chain: " + str(chain))