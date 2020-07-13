from collections import deque
import itertools

#################################################
# Double-ended queues (deques) are mutable lists that allow fast appends & pops on either end
# CANNOT be directly sliced, but a list can be sliced out

# create a new deque
dq1 = deque('newdeque')
print(f' dq1 is  {dq1} of type {type(dq1)}')
# dq1 is  deque(['n', 'e', 'w', 'd', 'e', 'q', 'u', 'e']) of type <class 'collections.deque'>


# add to deque
dq1.append('R')
print(dq1)   # deque(['n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R'])

# add to beginning
dq1.appendleft('A')
print(dq1)     # deque(['A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R'])

# add multiple items to the right
dq1.extend("CDE")
print(dq1)   # deque(['A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D', 'E'])

# add mutliple items to the left, note how order is added on
dq1.extendleft("123")
print(dq1)    # deque(['3', '2', '1', 'A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D', 'E'])

# pop & popLeft remove items from either end & return value removed
pop1 = dq1.pop()
print(dq1)   # deque(['3', '2', '1', 'A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D'])
print(f' popped val is: {pop1}')    # popped val is: E

pop2 = dq1.popleft()
print(dq1)  # deque(['2', '1', 'A', 'n', 'e', 'w', 'd', 'e', 'q', 'u', 'e', 'R', 'C', 'D'])
print(f' poppedLeft val is {pop2}')  # poppedLeft val is 3

dq2 = deque('012345')
print(dq2)    # deque(['0', '1', '2', '3', '4', '5'])

# rotate all values 3 to the right
dq2.rotate(3)
print(dq2)    # deque(['3', '4', '5', '0', '1', '2'])

# rotate all values 1 to the left
dq2.rotate(-1) 
print(dq2)    # deque(['4', '5', '0', '1', '2', '3'])

# slice out part of deque as a list
sliced = list(itertools.islice(dq2, 2,4))
print(sliced)    # ['0', '1']

# create circular buffer
dq3 = deque([], maxlen = 4)
for i in range(10):
    dq3.append(i)
    print(dq3)

# deque([0], maxlen=4)
# deque([0, 1], maxlen=4)
# deque([0, 1, 2], maxlen=4)
# deque([0, 1, 2, 3], maxlen=4)
# deque([1, 2, 3, 4], maxlen=4)
# deque([2, 3, 4, 5], maxlen=4)
# deque([3, 4, 5, 6], maxlen=4)
# deque([4, 5, 6, 7], maxlen=4)
# deque([5, 6, 7, 8], maxlen=4)
# deque([6, 7, 8, 9], maxlen=4)    