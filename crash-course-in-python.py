from __future__ import division
import random
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

# dictionaries

empty_dict = {} # pythonic
empty_dict2 = dict() # less pythonic
grades = {"Joel": 80, "Tim": 95} # dictionary literal
joels_grade = grades["Joel"] # 80
print(joels_grade)

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

# check for the existence of a key using in

joel_has_grade = "Joel" in grades # True
print(joel_has_grade)
kate_has_grade = "Kate" in grades # False
print(kate_has_grade)

# get method that returns a default value (instead of raising an exception) when you look up a key that's not in the dictionary

joels_grade = grades.get("Joal", 0) # 80
kates_grade = grades.get("kate", 0) # 0
no_ones_grade = grades.get("No One") # default is "None"
print(joels_grade, kates_grade, no_ones_grade)

# assignment using key value pairs

grades["Tim"] = 99 # replaces the old value
grades["Kate"] = 100 # adds a third entry
num_students = len(grades) # 3
print(grades, num_students)

# dictionaries are used to represent structured data

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys() # list of keys
tweet_values = tweet.values() # list of values
tweet_items = tweet.items() # list(array) of (key, value) tuples

print(tweet)
print(tweet_keys)
print(tweet_values)
print(tweet_items[0])

print("user" in tweet_keys) # True
print("user" in tweet) # True
print("joelgrus" in tweet_values) # True

# defaultdict

# counting words in document using a dictionary

document = ["data", "science", "crash", "course", "data", "science", "beginner", "course"]
word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)

# using forgiveness is better than permission approach

word_counts = {}
#print(word_counts) # {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

print(word_counts)

# using get method

word_counts = {}
print(word_counts) # {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1
print(word_counts)

# using defaultdict

word_counts = defaultdict(int) # int() produces 0
for word in document:
    word_counts[word] += 1
print(word_counts)
# they can also be useful with list or dict or even your own functions

dd_list = defaultdict(list) # list() produces an empty list
dd_list[2].append(1) # now dd_list contains {2: [1]}
dd_list[3].append(2) # now dd_list contains {2: [1], 3: [2]}
print(dd_list)

# using dict
dd_dict = defaultdict(dict) # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle" # {"Joel": {"City": "Seattle"}}
dd_dict["Joel"]["State"] = "WA" # {"Joel": {"City": "Seattle", "State": "WA"}}
print(dd_dict)

#using lambda function
dd_pair = defaultdict(lambda: [0, 0]) # [0, 0] is the default value
dd_pair[2][1] = 1 # now dd_pair contains {2: [0, 1]}
dd_pair[3][0] = 2 # now dd_pair contains {2: [0, 1], 3: [2, 0]}
dd_pair[2][0] = 3 # now dd_pair contains {2: [3, 1], 3: [2, 0]}
print(dd_pair)

# Counter

# counting words in a document using Counter

c = Counter([0, 1, 2, 0]) # c is {0: 2, 1: 1, 2: 1}
print(c)
word_counts = {}
word_counts = Counter(document)
print(word_counts)

# a Counter instance has a most_common method that is frequently useful
for word, count in word_counts.most_common(3):
    print(word, count)

# Sets

# represent a collection of distinct elements

s = set()
s.add(1) # s is {1}
s.add(2) # s is {1, 2}
s.add(2) # s is still {1, 2}
s.add(3) # s is {1, 2, 3}
print(s)
x = len(s) # 3
print(x)

y = 2 in s # True
z = 3 in s # True
print(y, z)

hundreds_of_other_words = []

stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list # False, but have to check every element

stopwords = set(stopwords_list)
"zip" in stopwords # very fast to check

# find distinct items in a collection

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)
num_distinct_item = len(item_set)
distinct_item_list = list(item_set)
print(item_list, num_items, item_set, num_distinct_item, distinct_item_list)

# control flow

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

x = 4
parity = "even" if x % 2 == 0 else "old"
print(parity)

x = 0
while x < 10:
    print(x, "is less than 10")
    x += 1

# we use for and in together

for x in range(10):
    print(x, "is less than 10")

for x in range(10):
    if x == 3:
        continue # go immediately to the next iteration
    if x == 5:
        break # quit the loop entirely
    print(x)

# Truthiness

one_is_less_than_two = 1 < 2 # True
true_equals_false = True == False # False
print(one_is_less_than_two, true_equals_false)

x = None # None is a special value similar to null in other languages
print(x == None) # True, but not pythonic
print(x is None) # True, pythonic

# python lets you use any value where it expects a boolean
# the following are all false
print(bool(False)) # False
print(bool(None)) # False
print(bool([])) # False
print(bool({})) # False
print(bool("")) # False
print(bool(set())) # False
print(bool(0.0)) # False
print(bool(0)) # False

def some_function_that_returns_a_string():
    return "string"

s = some_function_that_returns_a_string()

if s:
    first_char = s[0]
else:
    first_char = ""

print(first_char)
second_char = s and s[1]
print(second_char)

# when x is either a number or possibly None
safe_x = x or 0
print(safe_x)

# any() and all() function python

all([True, 1, {3}]) # True
all([True, 1, {}]) # False, {} is falsy
any([True, 1, {}]) # True, True is truthy
print(all([])) # True, no falsy elements in the list
print(any([])) # False, no truthy elements in the list

print(all([1,2,3, True])) # True, all elements in iterable(list) are truthy
print(any([1,2,3, False])) # True, at least one element in iterable(list) is truthy

print(all([1,2,3, False])) # False, at least one element in iterable(list) is falsy
print(any([False, ""])) # False, all elements in iterable(list) are falsy

# Sorting

# (sort or sorted) sort a list from smallest to largest 
x = [4, 1, 2, 3]
y = sorted(x) # y is [1, 2, 3, 4], x is unchanged
x.sort() # now x is [1, 2, 3, 4]
print(x, y)

# sort the list from largest to smallest using the reverse argument
# we can also provide a second argument to specify the sorting criteria

# sort the list by the absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True) # is [-4, 3, -2, 1]
print(x)

# here we sort the list of words by their lengths from longest to shortest
wc = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
print(wc)

# List comprehensions

# we can use list comprehensions to transform or filter a list

even_numbers = [x for x in range(5) if x % 2 == 0] # [0, 2, 4]
print(even_numbers)
squares = [x * x for x in range(5)] # [0, 1, 4, 9, 16]
print(squares)
even_squares = [x * x for x in even_numbers] # [0, 4, 16]
print(even_squares)

# you can turn lists into dictionaries or sets
square_dict = {x: x * x for x in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(square_dict)
square_set = {x * x for x in [1, -1]} # {1}
print(square_set)

# if you don't need the value from the list, it's common to use an underscore as the variable

zeroes = [0 for _ in even_numbers] # has the same length as even_numbers
print(zeroes)

# a list comprehension can include multiple fors and later fors can use the results of earlier ones
pairs = [(x, y)
            for x in range(10)
            for y in range(10)] # 100 pairs (0,0) (0,1) ... (9,8), (9,9)

print(pairs)

increasing_pairs = [(x, y) # only pairs with x < y]
                    for x in range(10) # range(lo, hi) equals [lo, lo + 1, ..., hi - 1]
                    for y in range(x + 1, 10)]
print(increasing_pairs)

# generator and iterators
# a generator is something that you can iterate over (for us, usually using for) 
# but whose values are produced only as needed (lazily)

def lazy_range(n):
    """a lazy version of range"""
    i = 0
    while i < n:
        yield i
        i += 1

for i in lazy_range(10):
    print(i)

# python commes with lazy_range function called xrange
# in python 3, range is a lazy_range
# in python 2, range is not lazy
# in python 3, range is xrange

# infinite lazy_range generator
def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

# natural_numbers() is a generator
print('natural_numbers() is a generator')
for i in natural_numbers():
    print(i)
    if i == 100:
        break

# another way to create generators is by using for comprehensions wrapped in parentheses

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
print(lazy_evens_below_20)
for i in lazy_evens_below_20:
    print(i)

# random module

four_uniform_ramdoms = [random.random() for _ in range(4)]

print(four_uniform_ramdoms)
# these random numbers are actually pseudorandom
# they are deterministic based on the initial state of the generator
# we can set the initial state using random.seed

random.seed(10) # set the seed to 10
print(random.random()) # 0.5714025946899135
random.seed(10) # reset the seed to 10
print(random.random()) # 0.5714025946899135

# random module also includes functions to get random integers, 
# choose randomly from a list, shuffle a list, and more like randrange(), choice(), shuffle()

print(random.randrange(10)) # choose randomly from range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.randrange(3, 6)) # choose randomly from range(3, 6) = [3, 4, 5]

# randomly reorder a list using shuffle()
up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)
print(up_to_ten)

# randomly pick one element from a list using choice()
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
print(my_best_friend)

# randomly choose a sample of elements without replacement(without duplicates) using sample()
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print(winning_numbers)

# choose sample of elements from list with replacement (duplicates) using choice()

four_with_replacement = [random.choice(range(10)) for _ in range(4)]
print(four_with_replacement)
