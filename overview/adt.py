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
# A ChainMap incorporates the underlying mappings by reference, e.g.  copies mem location
# therefore, updating the first chain will change dict that was used to load in ChainMap values
# therefore, updating a dict that was used to load in ChainMap values
#
# A ChainMap makes a good “context” container, since it can be treated as a stack 
# for which changes happen as the stack grows, with these changes being discarded again as the stack shrinks

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
##  >>   A ChainMap incorporates the underlying mappings by reference, e.g.  copies mem location
##  This will also update `dict_4`


# chain_map['e'] = 40
# print(f' tried to change second chain {chain_map.maps}')  # tried to change second chain [{'a': 100, 'b': 2, 'c': 3, 'e': 40}, {'d': 4, 'e': 5}]
# print(f' \t\t\t >>>  dict1 is {dict1}')    # {'a': 100, 'b': 2, 'c': 3, 'e': 40}

# create child ChainMap with value that overrides parent
chain_map2 = chain_map.new_child({'a': -999})
print(chain_map2.maps)

# print(f' \t >>>  dict1 is {dict1}')

# reverse child ChainMap
print(f' \t >>>  dict1 is {dict1}')
chain_map3 = collections.ChainMap(dict1, dict2)
print(f' chain_map3 is {chain_map3}')    # chain_map3 is ChainMap({'a': 100, 'b': 2, 'c': 3, 'e': 40}, {'d': 4, 'e': 5})

chain_map3.maps = reversed(chain_map3.maps)
print(f'should be reversed {(chain_map3)}')    # should be reversed ChainMap({'d': 4, 'e': 5}, {'a': 100, 'b': 2, 'c': 3, 'e': 40})

print("Reversed Chain: " + str(chain_map3))

dict3 = {"A": "apple", "B": "beetle", "C": "cow"}
chain_map4 = collections.ChainMap(dict3)
print(chain_map4)   # ChainMap({'A': 'apple', 'B': 'beetle', 'C': 'cow'}

chain_map4 = chain_map4.new_child({"E": "egg"})
print(f' added E: egg  {chain_map4}')     # ChainMap({'E': 'egg'}, {'A': 'apple', 'B': 'beetle', 'C': 'cow'})

chain_map4.maps = reversed(chain_map4.maps)

print(f' REVERSED !!!   {chain_map4}')
print("Reversed Chain: " + str(chain_map4))     # ChainMap({'A': 'apple', 'B': 'beetle', 'C': 'cow'}, {'E': 'egg'})

con_code1 = {'India' : 'IN', 'China' : 'CN'}
con_code2 = {'France' : 'FR', 'United Kingdom' : 'GB'}
code = {'Japan' : 'JP'}

chain = collections.ChainMap(con_code1, con_code2)
print("Initial Chain: " + str(chain.maps))
# Initial Chain: [{'India': 'IN', 'China': 'CN'}, {'France': 'FR', 'United Kingdom': 'GB'}]


chain = chain.new_child(code)    #Insert New Child
print("Chain after Inserting new Child: " + str(chain.maps))
# Chain after Inserting new Child: [{'Japan': 'JP'}, {'India': 'IN', 'China': 'CN'}, {'France': 'FR', 'United Kingdom': 'GB'}]

chain.maps = reversed(chain.maps)
print("Reversed Chain: " + str(chain))   
# Reversed Chain: ChainMap({'France': 'FR', 'United Kingdom': 'GB'}, {'India': 'IN', 'China': 'CN'}, {'Japan': 'JP'})



####  Since linking involves mapping by reference
# updating `dict_4` will update `new_chain`
# AND updating `new_chain` will update `dict`
dict_4 = {"One": 1, "Two": 2}
dict_5 = {"Five": 5, "Six": 6}

new_chain = collections.ChainMap(dict_4)
print(f' new chain is {dict_4}')

new_chain["three"] = 3

print(f'new_chain is {dict_4} ')   # new_chain is {'One': 1, 'Two': 2, 'three': 3} 
print(f' dict_4 is {dict_4}')      # dict_4 is {'One': 1, 'Two': 2, 'three': 3}


new_chain["four"] = 4
print(f'new_chain is {dict_4} ')    # new_chain is {'One': 1, 'Two': 2, 'three': 3, 'four': 4} 
print(f' dict_4 is {dict_4}')      #  dict_4 is {'One': 1, 'Two': 2, 'three': 3, 'four': 4}

dict_4["FIVE"] = 5
print(f'new_chain is {dict_4} ')     # new_chain is {'One': 1, 'Two': 2, 'three': 3, 'four': 4, 'FIVE': 5}
print(f' dict_4 is {dict_4}')        # dict_4 is {'One': 1, 'Two': 2, 'three': 3, 'four': 4, 'FIVE': 5}


new_chain2 = collections.ChainMap(dict_4, dict_5)
print(f' list new_chain2 {new_chain2} ')
# list new_chain2 ChainMap({'One': 1, 'Two': 2, 'three': 3, 'four': 4, 'FIVE': 5}, {'Five': 5, 'Six': 6}) 

# `parents` skips over original map
parent_chain = new_chain2.parents
print(f' parent_chain {parent_chain}')   # parent_chain ChainMap({'Five': 5, 'Six': 6})


# popping values from the first mapping, will not see children
# popped = new_chain2.pop("One")
# print(f' popped is {popped}')    # popped is 1
# print(f' new_chain2 is {new_chain2}')   # new_chain2 is ChainMap({'Two': 2, 'three': 3, 'four': 4, 'FIVE': 5}, {'Five': 5, 'Six': 6})

# removes item from end of first mapping
popped = new_chain2.popitem()
print(f' popped is {popped}')
print(f' new_chain2 is {new_chain2} ') # new_chain2 is ChainMap({'One': 1, 'Two': 2, 'three': 3, 'four': 4}, {'Five': 5, 'Six': 6}) 


class ReadNestedChain(collections.ChainMap):
    " Read/Write into nested mappings"

    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value    


    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        # raise KeyError(key)
        print(f' key \"{key}\"  does not exist ')            


deep_nested_chain = ReadNestedChain({'One': '1', 'Two': '2', 'three': '3', 'four': '4'}, {'Five': '5', 'Six': '6'}, {'eight': '8', 'nine': '9'})
print(f' {deep_nested_chain}')

# we can tell if a value is in the ChainMap but can only modify first mapping
print({"nine" in deep_nested_chain})   # True

deep_nested_chain2 = ReadNestedChain(deep_nested_chain)
print(f' {deep_nested_chain2}')
# ReadNestedChain(ReadNestedChain({'One': '1', 'Two': '2', 'three': '3', 'four': '4'}, {'Five': '5', 'Six': '6'}, {'eight': '8', 'nine': '9'}))

# change key value that is two levels down
deep_nested_chain2["nine"] = 999
print(f' {deep_nested_chain2}')
# ReadNestedChain(ReadNestedChain({'One': '1', 'Two': '2', 'three': '3', 'four': '4'}, {'Five': '5', 'Six': '6'}, {'eight': '8', 'nine': 999}))

# append to first mapping
deep_nested_chain2["Zero"] = 0
print(f' {deep_nested_chain2}')
# ReadNestedChain(ReadNestedChain({'One': '1', 'Two': '2', 'three': '3', 'four': '4', 'Zero': 0}, {'Five': '5', 'Six': '6'}, {'eight': '8', 'nine': 999}))

# try to delete key that does not exist 
del deep_nested_chain2["twelve"]    #  key "twelve"  does not exist 

# delete key that exsits
del deep_nested_chain2["nine"]
print(f' after del {deep_nested_chain2}')

# for item in deep_nested_chain2.items():
#     print(item)
