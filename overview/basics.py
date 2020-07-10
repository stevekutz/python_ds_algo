import random
# from builtins import str
import string
import time

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
# print(new_list) # ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

# # joins the strings
# str3 = "cat" ; str4 = "dog"
# print(str3.join(str4))  # dcatocatg

##########################################################
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

############################################
# # ## List comprehensions
# def f1(x): return x*2
# def f2(x): return x*4

# list_new = []
# for i in range(16):
#     list_new.append(f1(f2(i)))

# print(list_new)     # 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]

################################
# # with list comprehension
# print( [f1(x) for x in range(64) if x in [f2(j) for j in range(16)] ])
# # 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]

# # list comprehension instead of nested for loops
# list1 = [[1,2,3],[4,5,6]]
# cross_list = [i * j for i in list1[0] for j in list1[1]]
# print(f' cross_lists is {cross_list}')  # cross_lists is [4, 5, 6, 8, 10, 12, 12, 15, 18]


# # find values in cross_list that are between 8 & 14 inclusive (e.g. 8-14)
# find_8_14 = [val for val in cross_list if val in range(8,15)]
# print(f'find_8_14 is {find_8_14}')

# # d = 8
# # print(type(d))
# # num_str = str(d)
# # print(type(num_str))

# # List comprehension: Find values in cross_list that contain the digit '8'
# ## Note that we need to import string to use 'find'
# ## find returns index of item found, -1 otherwise

# list_8 = [item for item in cross_list if str(item).find('8') != -1]
# print(list_8)  # [8, 18]

# for item in list_8:
#     print(type(item))

# <class 'int'>
# <class 'int'>

# # some debug code to run above
# list_8 = []
# for item in cross_list:
#     print(str(item).find('8'))

# list_8 = []
# for item in cross_list:
#     if str(item).find('8') != -1:
#         list_8.append(item)

# print(list_8)        
# ############    Repeated values 
# # count all repeated values into a dict & put repeated vals into a list
# list_vals = [1, 4, 5, 6, 6, 8, 10, 12, 12, 15, 18, 1]
# list_rep = []
# dict_count = {}
# for val in list_vals:
#     if val in dict_count:
#         dict_count[val] += 1
#         list_rep.append(val)
#     else:
#         dict_count[val] = 1

# ## just for debugging fun
# # for k,v in dict_count.items():
# #     if v > 1:
# #         list_rep.append(k)

# print(f' list_rep  {list_rep}')

# # Find repeated vals and put into a list
# rep_vals = list(set([val for val in list_vals if list_vals.count(val) > 1]))
# print(f" Using list comprehension {rep_vals}")


# squares = [value**2 for value in range(1,11)]
# print(squares)

# # using nested for loops
# cross_list2 = []
# for i in list1[0]:
#     for j in list1[1]:
#         cross_list2.append(i*j)

# print(f' cross_list2 is {cross_list2}')  # cross_list2 is [4, 5, 6, 8, 10, 12, 12, 15, 18]      

# new_list = [value * 8 for value in range(0,16)]
# print(new_list)




##############################################
# higher order functions
## function that take other function as arguments OR that return functions

# def greeting(language):
#     if language == 'eng':
#         return 'hello world'
#     elif language == 'fr':
#         return 'Bonjour le monde'
#     else: return 'language not supported'

# # function is included in a list
# l_func = [ greeting('eng'), greeting('fr'), greeting('ger')]

# print(l_func[0])  # hello world
# print(l_func[1])  # Bonjour le monde
# print(l_func[2])  # language not supported

# # function used as argument for another function
# def call_other_func(other_func):
#     language = 'fr'
#     return ( other_func(language) )  

# print(call_other_func(greeting))    # Bonjour le monde


# def call_other_func2(other_func, lang):
#     return ( other_func(lang) )

# print(call_other_func2(greeting, "eng"))  # hello world


# def call_other_func3(other_func, lang = "fr"):
#     return ( other_func(lang) )

# print( call_other_func3(greeting) )     # Bonjour le monde
# print(call_other_func3(greeting, 'ital'))  # language not support

# using Python 3 HOF map & filter , these return an iterator
# lambda is just an anonymous function

str = "the quick brown fox jumped over the lazy dog"
new_list = str.split()
# ind = 0

# for item in map(lambda n: n, new_list):
#     print(f' item {ind} is {item}')
#     ind += 1

# #  item 0 is the
# #  item 1 is quick
# #  item 2 is brown
# #  item 3 is fox
# #  item 4 is jumped
# #  item 5 is over
# #  item 6 is the
# #  item 7 is lazy
# #  item 8 is dog

# # convert list of capitalized words to lower case
# lower_list = [item.lower() for item in new_arr]
# print(f' lower list {lower_list} ')

# # swap upper-lower case
# swapped = [item.swapcase() for item in new_arr]
# print(f' swapped cases {swapped} ')

# # removes leading & trailing white space
# str_ws = " cat dog  "
# no_lead_trail_ws = str_ws.strip(' ')     
# print(f'>>{no_lead_trail_ws} with length {len(no_lead_trail_ws)}')  #
# print(f'{str_ws} with length {len(str_ws)}')

# str_char = "the fat cat"
# no_t = str_char.strip('t')
# print(f'{no_t}')

# # remove all whitespace using       replace
# str_sp = " the mouse house  "
# no_sp = str_sp.replace(" ", "")
# print(f'{no_sp}')


# # using lambda to capitalize every word in list
# new_arr = []
# for item in map(lambda n: n.capitalize(), new_list):
#     new_arr.append(item) 

# print(new_arr)   # ['The', 'Quick', 'Brown', 'Fox', 'Jumped', 'Over', 'The', 'Lazy', 'Dog']
# print(new_list)  # ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']


# filtered_list = []
# for item in filter(lambda n: len(n) > 4, new_list):
#     filtered_list.append(item)

# print(filtered_list)  #  ['quick', 'brown', 'jumped']   


# words = str.split('the longest word in the sentence')

# print(words)     # ['the', 'longest', 'word', 'in', 'the', 'sentence']
# print(sorted(words, key=len))   # ['in', 'the', 'the', 'word', 'longest', 'sentence']

# sl = ['A', 'b', 'a', 'C', 'c']

# sl.sort(key = str.lower)

# print(f' Using sort method {sl}')     # Using sort method ['A', 'a', 'b', 'C', 'c']

# sl.sort()
# print(f' direct sort gives {sl}')

# # sorting by index location using lambda operator
# # each element is grocery item, price, and quantity
# grocery_list = [["rice", 2.4, 8], ["flour", 1.9, 5], ["corn", 4.7, 6]]

# grocery_list.sort(key=lambda item: item[1])
# print(grocery_list)   # [['flour', 1.9, 5], ['rice', 2.4, 8], ['corn', 4.7, 6]]

# grocery_list.sort(key=lambda item: item[0])
# print(grocery_list)   # [['corn', 4.7, 6], ['flour', 1.9, 5], ['rice', 2.4, 8 ]]

#################################################################
# Recursion
## Base case is argument that tests for terminating process to avoid infinite loop
## Recursion is a special case of iteration called tail-iteration
## You should be able to convert an iterative function to a recursive & vice-versa
## Usually iteration is more efficient
## Recursion usually easier to understand & useful for linked lists & trees

# # Using iteration(while loop)
# def iterTest(low, high):
#     list = []
#     while low <= high:
#         list.append(low)
#         low += 1
#     print(f' Using iteration {list}')

# iterTest(1,5)  # Using iteration [1, 2, 3, 4, 5]

# # Using recursion(function calls itself)
# list = []
# def recurTest(low, high):
#     if low <= high:
#         list.append(low)
#         print(f' list is {list}')
#         recurTest(low + 1, high) 

# recurTest(1, 5)
# # list is [1]
# # list is [1, 2]
# # list is [1, 2, 3]
# # list is [1, 2, 3, 4]
# # list is [1, 2, 3, 4, 5]

# print(f' using recursion {list}')  # using recursion [1, 2, 3, 4, 5]

####################################
# Generators
## Generators are funtions that return an entire sequence of results(use yeild)
## Generators yields items instead of making a list
## Generators always return None



# import time

# # generator function creates an iterator of odd itegers between n & m
# def oddGen(n, m):
#     while n < m:
#         print(n)
#         yield n
#         n += 2    

# # creates a list of odd numbers between n & m
# def oddList(n, m):
#     list = []
#     while n < m:
#         list.append(n)
#         n += 2
#     return list

# # show run time
# t1 = time.time()

# sum(oddGen(1, 100_000_000))
# # print("Time to sum an iterator: %f" % (time.time() - t1))
# print(f' Time to sum an iterator {time.time() - t1}')

# t1 = time.time()
# sum(oddList(1, 100_000_000))
# print(f' Time to build & sum a list {time.time() - t1}')

## Generator expressions build generator obj more succintly (similar to using list comprehensions)
## Since generator return a lazy iterator obj, it can looped over without storing the entire 
## content of what is being looped over in memory. A list loads itself into memory.

# t1 = time.time()
# square_nums_lc = [val**2 for val in range(1,1000000)]
# print(f' List Comprehension time is {time.time() - t1}')

# t1 = time.time()
# square_nums_gc = (val**2 for val in range(1,1000000))
# print(f' Generator time is {time.time() - t1}')

#################################################################################
## Classes

class Employee():
    numEmployee_instances = 0

    def __init__(self, name, rate):
        self.owed = 0    # setting a default valie within __init__
        self.name = name
        self.rate = rate

        Employee.numEmployee_instances += 1

    def __del__(self):
        Employee.numEmployee_instances -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return (" %.2f hours worked" % numHours)

    def pay(self):
        self.owed = 0
        return("payed %s " % self.name)     

    def __repr__(self):
        return (" custom object (%r)" % self.name)


emp1 = Employee("Moe", 19.25)
emp2 = Employee("Joe", 18.25)

print(Employee.numEmployee_instances)    # 2

print(emp1.hours(30)) # 0.00 hours worked
print(emp1.owed)      # 577.5
print(emp1.pay())     # payed Moe
print(emp1.__repr__)  # <bound method Employee.__repr__ of  custom object ('Moe')>


class SpecialEmployee(Employee):
    # __init__  needed for subclass to define its own class variables
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate)  # same as super().__init_(self, name, rate)
        self.bonus = bonus


    
    def hours(self, numHours):
        self.owed += numHours * self.rate + self.bonus
        return(" %.2f hours worked NOW " % numHours)


# verify if subclass
print(issubclass(SpecialEmployee, Employee))  # True
print(issubclass(Employee, SpecialEmployee))  # False


Howie = SpecialEmployee("Google", 50, 1000)
Jack = Employee("Alphabet", 4500)

print(isinstance(Howie, Employee))         # True
print(isinstance(Howie, SpecialEmployee))  # True


## Static vs Class methods
# Class methods only deals with class itself and not instances
# Static methods deals with parameters passed in, has no acccess to class variables

class Exponential():
    base = 3  # base class variable
    @classmethod
    def exp(cls, x):    # first arg is cls by convention
        return (cls.base**x)  

    @ staticmethod
    def addition(x, y):
        return (x + y)
        # return (x + y + base)  # NameError: name 'base' is not defined

    @classmethod
    def change_base(cls):
        base = 5    

class Exponential_Child(Exponential):
    base = 2  # base class variable changed to 4

exp_class = Exponential()
print(f' 4 cubed is from class method   {exp_class.exp(4)} ')   # 4 cubed is from class method   81 
print(f' Sum from static method recieves parameters {exp_class.addition(4,10)} ')  # Sum from static method recieves parameters 14 
exp_class.change_base()  # # Does not change class
print(f' 4 raised to 5 is from class method   {exp_class.exp(4)} ')   # Does not change class

exp_child = Exponential_Child()
print(f' 4 squared is from inherited class method using new base {exp_child.exp(4)}')  # 4 squared is from inherited class method using new base 16 
print(f' Sum from static method received parameters {exp_child.addition(1,3)}')  # Sum from static method received parameters 4


