#q1. print multiplication table
x = 20
for i in range(1,11):
    print(x, "x", i, "=", x*i)

#q2. print star pattern - right triangle
n = 7
for i in range(1, n + 1):
    print("*" * i)

#q3. print star pattern -inverted triangle
n = 7
for i in range(n, 0, -1):
    print("*" * i)

#q4. print star pattern - pyramid
n = 7
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2 * i - 1))

#q5. Fibonacci
n = 10
a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c