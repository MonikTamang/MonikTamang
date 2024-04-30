# stack
# stack using list

stack1 = []
stack1.append('a')
stack1.append('b')
stack1.append('c')

print('Stack: ', stack1)

# Pop() function -> LIFO
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())

# stack using deque -> for quicker append and pop operation
from collections import deque

stack2 = deque()
stack2.append('d')
stack2.append('e')
stack2.append('f')

print('Stack2:', stack2)

print(stack2.pop())
print(stack2.pop())
print(stack2.pop())


# Queue with LIFO Queue
# put() and get()

from queue import LifoQueue

# initialize stack
stack3 = LifoQueue(maxsize=3)

# add value
stack3.put('g')
stack3.put('h')
stack3.put('i')

print('Stack Full:', stack3.full())  # full() -> if queue is full return true
print('Size:', stack3.qsize())  # qsize() -> size of queue

# get() -> to pop the value from queue

print(stack3.get())
print(stack3.get())
print(stack3.get())

print('Stack Empty:', stack3.empty())
