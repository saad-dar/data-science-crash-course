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

# list
integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list) # 3
print(list_length) # 3
list_sum = sum(integer_list) # 6
print(list_sum) # 6

# setting or getting the nth element of a list

x = range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zero = x[0] # 0
one = x[1] # 1
nine = x[-1] # 9
eight = x[-2] # 8
print(x)
x[0] = -1 # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9] # TypeError: 'range' object does not support item assignment in python 3
print(x) # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slicing
first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, 5, 6, 7, 8, 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, 3, 4, 5, 6, 7, 8]
copy_of_x = x[:] # [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# check if a value is in a list
print(1 in [1, 2, 3]) # True
print(0 in [1, 2, 3]) # False

# concatenating lists
x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1, 2, 3, 4, 5, 6] # modifies the list in place

# if you don't want to modify the original list you can use list addition
x = [1, 2, 3]
y = x + [4, 5, 6] # y is [1, 2, 3, 4, 5, 6] # creates a new list

# append method adds a single element to the end of the list

x = [1, 2, 3]
x.append(0) # x is [1, 2, 3, 0]
y = x[-1] # 0
z = len(x) # 4
print(z, y, x)

# unpacking lists (similar to tuple unpacking)
x, y = [1, 2] # x is 1, y is 2

# pythonic way to swap variables
x, y = y, x # x is 2, y is 1

# underscores can be used to assign values to unused variables
_, y = [1, 2] # y is 2 and 1 will be ignored

# tuples
# tuples are the immutable cousins of the lists

my_list = [1, 2]    # list
my_tuple = (1, 2)   # tuple
other_tuple = 3, 4  # tuple without the parentheses

my_list[1] = 3 # my_list is now [1, 3]

print(my_list)
try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")

# tuples are a convenient way to return multiple values from functions
def sum_and_product(x, y):
    return (x + y), (x * y)

x, y = sum_and_product(2, 3) # x is 5, y is 6
print(x, y)
x, y = sum_and_product(5, 10) # x is 15, y is 50
print(x, y)

# tuples (and lists) can also be used for multiple assignment

x, y = 1, 2 # x is 1, y is 2
x, y = y, x # pythonic way to swap variables