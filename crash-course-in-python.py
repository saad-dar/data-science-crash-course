from __future__ import division
# white spaces formatting
for i in [1, 2, 3, 4, 5]:
    print(i)
    for j in [1, 2, 3, 4, 5]:
        print(j)
        print(i + j)
    print('again')
    print(i)
print("done looping")

# long winding list computation
long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 
                           + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easy_to_read_list_of_lists = [[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]]

two_plus_three = 2 + \
                    3
for i in [1, 2, 3, 4, 5]:

    # notice the blank line
    print(i)

# modules

import re
my_regex = re.compile("[0-9]+", re.I)

# importing module with alias

import re as regex
# import matplotlib.pyplot as plt
my_regex = regex.compile("[0-9]+", regex.I)

# importing specific functions from a module

from collections import defaultdict, Counter
loopup = defaultdict(int)
my_counter = Counter()

# importing all functions from a module into the global namespace (usually discouraged)
match = 10
from re import *
print(match) # "<function re.match>" # above match value is replaced by re.match function

# arithmetic operations

print(5/2) # 2.5
# to get only the integer part of the division
print(5//2) # 2

# functions

def double(x):
    return x * 2

# python functions are first class which means you can assign them to variables and pass them into functions just like any other arguments
def apply_to_one(f):
    return f(1)

my_double = double # refers to the previously defined function
x = apply_to_one(my_double) # 2
print(x)

# anonymous functions (lambda functions)
y = apply_to_one(lambda x: x + 4) # 5

another_double = lambda x: 2 * x # don't do this(not recomended)
def another_double(x): return 2 * x # do this (recommended)

# default arguments
def my_print(message="my default message"):
    print(message)

my_print("hello") # hello
my_print() # my default message

# specifying arguments by name
def subtract(a=0, b=0):
    return a - b

#print(subtract(10, 5)) # 5
#print(subtract(0, 5)) # -5
#print(subtract(b=5)) # -5 # a is not specified

# strings

single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t" # represents the tab character
print(len(tab_string)) # 1

# raw strings with backslaches (useful when dealing with regular expressions)

not_tab_string = r"\t" # represents the characters '\' and 't'
print(len(not_tab_string)) # 2

# multiline strings

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""
# prints with the new line characters
print(multi_line_string)

# exceptions

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")