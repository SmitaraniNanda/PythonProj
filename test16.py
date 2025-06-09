# 1. Count Vowels in a String
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

print("1. Vowel Count:", count_vowels("Hello World"))

# 2. Reverse a String Without Using [::-1]
def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print("2. Reverse String:", reverse_string("Python"))

# 3. Find the Largest Number in a List
def find_largest(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
    return largest

print("3. Largest Number:", find_largest([3, 7, 2, 9, 4]))

# 4. Check for Palindrome
def is_palindrome(s):
    s = str(s)
    return s == reverse_string(s)

print("4. Palindrome Check:", is_palindrome("madam"))

# 5. Generate Fibonacci Series
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

print("5. Fibonacci Series:", fibonacci_series(10))

# 6. Find Prime Numbers in a Range
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print("6. Primes in Range:", primes_in_range(10, 30))

# 7. Word Frequency Counter
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print("7. Word Frequency:", word_frequency("this is a test this is only a test"))

# 8. Remove Duplicates from a List
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

print("8. Remove Duplicates:", remove_duplicates([1, 2, 2, 3, 1, 4]))

# 9. Sum of Digits
def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(int(number))))

print("9. Sum of Digits:", sum_of_digits(12345))
