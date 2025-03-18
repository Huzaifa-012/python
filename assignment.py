for i in [1, 2, 3, 4, 5]:
    print(i)  # first line in "for i" block
    for j in [1, 2, 3, 4, 5]:
        print(j)  # first line in "for j" block
        print(i + j)  # last line in "for j" block
    print(i)  # last line in "for i" block
print("done looping")
print("Hello")
import re
print("Hello")
print("Hello")
print("Hello")
my_regex = re.compile("[0-9]+", re.I)

import re as regex
my_regex2 = regex.compile("[0-9]+", regex.I)

import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()


def double(x):
    return x * 2


print("Using the double function: ", double(2))


def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)
y = apply_to_one(lambda x: x + 4)

another_double = lambda x: 2 * x
def another_double(x):
    return 2 * x

def my_print(message="my default message"):
    print(message)

my_print("hello")
my_print()

def subtract(a=0, b=0):
    return a - b


print("Using the subtract function: ", subtract(10, 5))
single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = "\t"
print(len(tab_string))

not_tab_string = r"\t"
print(len(not_tab_string))

multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

try:
    print(0 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list)
list_sum = sum(integer_list)

x = range(10)
zero = x[0]
one = x[1]
nine = x[-1]
eight = x[-2]

first_three = x[:3]
three_to_end = x[3:]
one_to_four = x[1:5]
last_three = x[-3:]
without_first_and_last = x[1:-1]
copy_of_x = x[:]

print(1 in [1, 2, 3])
print(0 in [1, 2, 3])

x = [1, 2, 3]
x.extend([4, 5, 6])
y = x + [4, 5, 6]

x = [1, 2, 3]
x.append(0)
y = x[-1]
z = len(x)

x, y = [1, 2]
_, y = [1, 2]

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3

try:
    my_tuple[1] = 3
except TypeError:
    print("cannot modify a tuple")


def sum_and_product(x, y):
    return (x + y), (x * y)


sp = sum_and_product(2, 3)
s, p = sum_and_product(5, 10)

x, y = 1, 2
x, y = y, x

empty_dict = {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}
joels_grade = grades["Joel"]

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("no grade for Kate!")

joel_has_grade = "Joel" in grades
kate_has_grade = "Kate" in grades

joels_grade = grades.get("Joel", 0)
kates_grade = grades.get("Kate", 0)
no_ones_grade = grades.get("No One")

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_items = tweet.items()
print("user" in tweet_keys)
print("user" in tweet)

document = "Hello Hello Hello"
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

dd_list = defaultdict(list)
dd_list[2].append(1)

dd_dict = defaultdict(dict)
dd_dict["Joel"]["City"] = "Seattle"

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1

from collections import Counter

c = Counter([0, 1, 2, 0])
word_counts = Counter(document)
for word, count in word_counts.most_common(10):
    print(word, count)

s = set()
s.add(1)
s.add(2)
s.add(2)
x = len(s)
y = 2 in s
z = 3 in s

stopwords_list = ["a", "an", "at"] + ["apple", "banana"] + ["yet", "you"]
print("zip" in stopwords_list)
stopwords_set = set(stopwords_list)
print("zip" in stopwords_set)

if 1 > 2:
    message = "if only 1 were greater than two..."
elif 1 > 3:
    message = "elif stands for 'else if'"
else:
    message = "when all else fails use else (if you want to)"

x = 0
while x < 10:
    print(x, "is less than 10")
    x += 1

for x in range(10):
    if x == 3:
        continue
    if x == 5:
        break
    print(x)


class Set:
    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(list(self.dict.keys()))

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]
