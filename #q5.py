#1. Given a list of integers, extract even numbers, calculate their squares, and then extract squares greater than 100.

numbers = [2, 5, 8, 10, 12, 15, 20]
even_nos = list(filter(lambda x: x % 2 == 0, numbers))

squares = list(map(lambda x: x ** 2, even_nos))

result = list(filter(lambda x: x > 100, squares))

print("Even numbers:", even_nos)
print("Squares:", squares)
print("Squares greater than 100:", result)

#2. Given a list of strings, extract strings with length greater than 3 and convert them into uppercase

words = ["pie", "apple", "pasta", "banana", "pizza"]
filtered = list(filter(lambda x: len(x) > 3, words))
result = list(map(lambda x: x.upper(), filtered))

print("Filtered strings:", filtered)
print("Uppercase strings:", result)

#3. Write a program to extract numbers divisible by 2 or 3 and calculate their squares.

numbers = [2, 3, 4, 5, 6, 8, 9, 10, 12]
filtered = list(filter(lambda x: x % 2 == 0 or x % 3 == 0, numbers))
squares = list(map(lambda x: x ** 2, filtered))

print("Filtered:", filtered)
print("Squares:", squares)

#4. Given a list of integers, add 10 to every element and then extract elements greater than 30.

numbers = [10, 15, 20, 25, 30, 35]
added = list(map(lambda x: x + 10, numbers))
result = list(filter(lambda x: x > 30, added))

print("Updated list:", added)
print("Numbers greater than 30:", result)

#5. Write a program to extract negative numbers and convert them into their absolute values.

numbers = [-5, 10, -3, 8, -12, 4, -7]
negative = list(filter(lambda x: x < 0, numbers))
result = list(map(lambda x: abs(x), negative))

print("Negatives:", negative)
print("Absolutes:", result)

#6. Given a list of words, extract words ending with the letter 'n' and calculate their lengths.

words = ["lion", "tiger", "elephant", "deer", "hen", "monkey"]
filtered = list(filter(lambda x: x.endswith('n'), words))
result = list(map(lambda x: len(x), filtered))

print("Filtered:", filtered)
print("Lengths:", result)

#7. Write a program to extract numbers that are perfect squares from a given list.

import math
numbers = [4, 7, 9, 12, 16, 20, 25, 30, 36]
result = list(filter(lambda x: math.isqrt(x) ** 2 == x, numbers))

print("Squares:", result)