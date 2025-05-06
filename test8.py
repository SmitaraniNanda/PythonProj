s = "hello"
print(s[::-1])


s = "madam"
print( s == s[::-1])


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_count = 0
consonant_count = 0
s = "python"
for i in s:
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Number of vowels: {vowel_count} and number of consonants: {consonant_count}")


from collections import Counter
s = "aabbcc"
print( dict(Counter(s)))


s = " a b c "
print( s.replace(" ", ""))

s = "I like Java"
print( s.replace("Java", "Python"))


s1 = "abc123def"
s2 = "".join([char for char in s1 if char.isnumeric()])
print(s2)


s = "Hello123"
print( s.isalpha())


s = "hello world"
print( s.title())








