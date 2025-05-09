# Tuple Tasks

# 1. Create a Tuple
tuple_data = (42, "Hello", 3.14, [1, 2, 3], (9, 8))
print("Created Tuple:", tuple_data)

# 2. Access Elements
my_tuple = ('apple', [20, 30], (1, 2, 3), 4.5, 'banana')
print("Second element:", my_tuple[1])
print("Third element’s second item:", my_tuple[2][1])

# 3. Tuple Immutability
# my_tuple = (1, 2, 3)
# my_tuple[1] = 4  # This raises TypeError because tuples are immutable.
# Correct approach:
my_tuple = (1, 4, 3)  # Create a new tuple
print("Corrected Tuple:", my_tuple)

# 4. Tuple Unpacking
coordinates = (45.4215, -75.6972)
latitude, longitude = coordinates
print("Latitude:", latitude)
print("Longitude:", longitude)

# 5. Tuple Operations
def sum_tuples(t1, t2):
    return tuple(a + b for a, b in zip(t1, t2))

print("Element-wise sum:", sum_tuples((1, 2, 3), (4, 5, 6)))

# Set Tasks

# 1. Basic Set Operations
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Union:", A | B)
print("Intersection:", A & B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Symmetric Difference:", A ^ B)

# 2. Set Membership
print("3 in A:", 3 in A)
print("6 in B:", 6 in B)

def is_member(item, s):
    return item in s

# 3. Removing Duplicates
duplicates_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(duplicates_list))
print("List without duplicates:", unique_list)

# 4. Set from String
sentence = input("Enter a sentence: ")
import string
words = sentence.lower().translate(str.maketrans('', '', string.punctuation)).split()
unique_words = set(words)
print("Unique words:", unique_words)

# 5. Advanced Set Logic
football = {"Smita", "Puspa", "Sweety", "Mamali"}
basketball = {"Puspa", "Vanket", "Mamali"}
tennis = {"Sweety", "Mamali", "Madhu"}

# All three
all_three = football & basketball & tennis
print("Play all three:", all_three)

# Only one sport
only_one = (football ^ basketball ^ tennis) - (football & basketball) - (football & tennis) - (basketball & tennis)
print("Play only one sport:", only_one)

# Exactly two sports
exactly_two = ((football & basketball) | (football & tennis) | (basketball & tennis)) - all_three
print("Play exactly two sports:", exactly_two)

# Dictionary Tasks

# 1. Count Word Frequencies
def word_count(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(word_count("apple banana apple orange banana apple"))

# 2. Merge Two Dictionaries
def merge_dicts(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

print(merge_dicts({'a': 5, 'b': 3}, {'b': 2, 'c': 7}))

# 3. Invert a Dictionary
def invert_dict(d):
    inverted = {}
    for k, v in d.items():
        inverted.setdefault(v, []).append(k)
    return inverted

print(invert_dict({'a': 1, 'b': 2, 'c': 1}))

# 4. Most Frequent Value
def most_frequent_value(d):
    from collections import Counter
    freq = Counter(d.values())
    return freq.most_common(1)[0][0]

print(most_frequent_value({'Smita': 25, 'Puspa': 30, 'Mamali': 25, 'Madhu': 30, 'Tanu': 25}))

# 5. Dictionary from Two Lists
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

print(lists_to_dict(['name', 'age', 'city'], ['Smita', 25, 'New York']))
