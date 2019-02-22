# this is just a rough outline for completing problem 1 from programming assignment 1
# you don't have to use this code if you don't want to, but at least read and understand it

#     here are suggested interfaces for the Stack and Queue classes
#
#     interface stack {
#         Boolean is_empty();           // returns True if empty, False if not
#         void push(Type X);            // pushes X onto the stack
#         Type pop() raises Underflow;  // pops top element of the stack,
#                                          raises Underflow if stack is empty
#     }
#
#     interface queue {
#         Boolean is_empty();               // returns True if empty, False if not
#         void enqueue(Type X);             // appends X to the queue
#         Type dequeue() raises Underflow;  // removes front element of the
#
#                       queue, raises Underflow if queue is empty
#     };

import sys
from doublellsentinel import DoubleLLSentinel
import copy
# custom Underflow exception
class Underflow(Exception):
    pass  # make it fancier if you want :)


# TODO: implement the stack
class Stack:

    # class constructor
    def __init__(self):
        self.t = DoubleLLSentinel()


    # push method
    def push(self, x):
        self.t.insertStack(x)


    # pop method
    def pop(self):
        if self.is_empty():
            return ("StackError")
        self.d = self.t.sntl.next.data
        self.t.delete(self.t.sntl.next)
        return self.d

    # is_empty method
    def is_empty(self):
        return len(self.t) == 0

# TODO: implement the print function
# args: s, Stack
def print_stack(s):
    # only use s.push, s.pop, and s.is_empty
    s2 = copy.deepcopy(s)
    if s2.is_empty():
        print("Empty")
    else:
        v=''
        for i in range(len(s2.t)):
            v += "{} ".format(s2.pop(), end = '')
        print(v.strip())

# this function runs the program according to the problem specification
def driver():
    s = Stack()
    with open(sys.argv[1]) as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            action, value_option = in_data[0], in_data[1:]
            if action == "push":
                value = int(value_option[0])
                # TODO: implement push action
                s.push(value)
            elif action == "pop":
                # TODO: implement pop action
                try:
                    print(s.pop())
                except Underflow:
                    print("StackError")
            elif action == "print":
                # TODO: implement print action
                print_stack(s)  # change this!

# this starter code should work with either python or python3
if __name__ == "__main__":
    driver()
