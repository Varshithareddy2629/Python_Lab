#q1. Create a list of 10 numbers and print only even numbers.
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
print("Even numbers are:")
for n in numbers:
    if n % 2 == 0:
        print(n)

#q2. Find the second-largest value in a list.
numbers = []
n = int(input("How many numbers? "))
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
numbers.sort()
print("Second largest number is:", numbers[-2])

#q3. Create a tuple of 5 subjects and unpack it.
subjects = ("Python", "Maths", "English", "Physics", "Chemistry")
a, b, c, d, e = subjects
print(a)
print(b)
print(c)
print(d)
print(e)

#q4. Remove duplicates from a list using a set.
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
duplicate_numbers = list(set(numbers))
print("List without duplicates:")
print(duplicate_numbers)

#q5. Create a dictionary of 5 students and their marks.
students = {
    "Amit": 85,
    "Riya": 92,
    "Rahul": 78,
    "Sneha": 88,
    "Kiran": 95
}
print("Student Records:")
for name in students:
    print(name, ":", students[name])

#q6. Count character frequencies in a string using a dictionary.
text = "hello"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)
