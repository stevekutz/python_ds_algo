# Variable scope
##  local environment(namespace) is created inside function
##  but it looks in global namesapce for variable 'a'
a = 10; b = 20

def scope_func():
    global a
    a = 1; b = 2


scope_func()
print(f'a is {a}') # changed to 1
print(f'b is {b}') # local change not bound to global variable   


## variables referenced inside function implicitily global
## however, if variable is assigned inside func, it is assumed to be local
# 2
c = 10

def print_val():
    print(f' \t c is {c}')  # global variable c is referenced

print_val()    

def print_val():
    c = c + 1   # c is assumed to be local but was never assigned
    print(f'NOW c is {c}')

print_val()  # UnboundLocalError: local variable 'c' referenced before assignment