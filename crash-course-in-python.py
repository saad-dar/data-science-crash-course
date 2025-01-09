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
