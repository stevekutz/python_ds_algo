import random

# # Variable scope
# ##  local environment(namespace) is created inside function
# ##  but it looks in global namesapce for variable 'a'
# a = 10; b = 20

# def scope_func():
#     global a
#     a = 1; b = 2


# scope_func()
# print(f'a is {a}') # changed to 1
# print(f'b is {b}') # local change not bound to global variable   


# ## variables referenced inside function implicitily global
# ## however, if variable is assigned inside func, it is assumed to be local
# # 2
# c = 10

# def print_val():
#     print(f' \t c is {c}')  # global variable c is referenced

# print_val()    

# def print_val():
#     c = c + 1   # c is assumed to be local but was never assigned
#     print(f'NOW c is {c}')

# print_val()  # UnboundLocalError: local variable 'c' referenced before assignment


# ## Looping
# x = 'one'
# if x == 0:
#     print(f'False')
# elif x == 1:
#     print(f'True')
# else: 
#     print(f'Something else')        

# x = 0
# while x < 3: print(x); x += 1    

# x = 100
# while x < 300:
#     print(f' x is {x}')
#     x *= 2

# words= ['cat', 'dog', 'mouse']
# for w in words:
#     print(w)    

## 
# str = 'mouse'  
# print(str)
# print(type(str))
# str = ['mouse', 'cat'] 
# print(str) 
# print(type(str))

# for item in str:
#     item = item.capitalize()
#     print(item)
# print(str)   

# ## string functions
# str = "the quick brown fox jumped over the lazy dog"
# print(str.capitalize())  # The quick brown fox jumped over the lazy dog
# print(str.count("the"))  # 2

# # returns True if string ends with specified substring
# print(str.endswith("dog"))  # True

# # find first occurence of substring
# print(str.find("brown"))

# str2 = "abc123"  # a space will result in False for both
# # returns True if all chars are alphanumeric
# print(str2.isalnum())  # True

# # returns True is all chars are alphabetic
# print(str2.isalpha())  # False

# # return True is all chars are digits
# print(str2.isdigit())

# # Splits string separated by whitespace or optional seperator
# new_list = str.split()
# print(new_list) # ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'

# # joins the strings
# str3 = "cat" ; str4 = "dog"
# print(str3.join(str4))  # dcatocatg

# # some common list functions
# list_1 = ['mouse', 'cat']
# # str[0] = str[0].capitalize()
# # str.insert(0, str[0].capitalize())  # ['Mouse', 'mouse', 'cat']
# print(list_1)
# index = 0
# while index < len(list_1):
#     list_1[index] = list_1[index].capitalize()
#     index += 1
# print(list_1)

# print(f' returns list of sequences {list(list_1)}') # returns list of sequences ['Mouse', 'Cat']

# # add to the end of a list
# list_1.append("giraffe")
# print(list_1)

# # append a list to another list
# list_2 = ["turtle", "fish"]
# list_1.extend(list_2)
# print(list_1)

# # count how many times 'cat' is in list
# print(f' cat occurs {list_1.count("cat")} times')  # 0 times
# print(f' Cat occurs {list_1.count("Cat")} times ')  # 1 time

# list_2.extend(list_2)
# print(f' fish occurs first at index {list_2.index("fish")}')

# # generate a random list
# rand_list = [value + random.randrange(10) for value in range(1,11)] 
# print(rand_list)

# rand_list2 = random.sample(range(0,10) ,10)
# print(rand_list2)

# # sort list
# sorted_list = rand_list2[:]  # copy by reference
# sorted_list.sort()
# print(sorted_list)

# reverse_sorted_list = rand_list[:]
# reverse_sorted_list.sort(reverse = True)
# print(f'{reverse_sorted_list}')

## List comprehensions
def f1(x): return x*2
def f2(x): return x*4

list_new = []
for i in range(16):
    list_new.append(f1(f2(i)))

print(list_new)     # 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]

# with list comprehension
print( [f1(x) for x in range(64) if x in [f2(j) for j in range(16)] ])

new_list = [value * 8 for value in range(0,16)]
print(new_list)