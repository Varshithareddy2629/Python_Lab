#q1. Hello World
print ("Hello World!")
print("Welcome to python programming")

#q2. Add two numbers
a = 10
b = 20
sum = a + b
print ("Sum: ", sum)

#q3. Largest of 3 numbers
a = 15
b = 16
c = 17
largest = a
if b >largest:
    largest = b
if c >largest:
    largest = c
print ("largest number among them is: ", largest)    

#q4. Even or odd
number = 17
if number%2==0:
    print(number, "; this number is even")
else:
    print(number, "its odd!")

#q5.  Multiplication table
number = 6
for i in range(1,11):
    print(number, "x",i,"=",number*i)

b = 12
for i in range(1,11):
    print(b,"x",i,"=",b*i)

# q6. Factorial
number = 5
factorial=1
for i in range(1,number+1):
    factorial*=i
print("Factorial is: ", factorial)

#q7. prime number
number = 10
is_prime=True
if number<=1:
    is_prime=False
else:
    for i in range(2,number):
        if number%1==0:
            is_prime=False
            break
print("prime" if is_prime else "Not prime")

#q8. reverse a string
text = "python"
print(text[::-1])

#q9. Sum of list elements
numbers = [10,20,30,40,50]
total = 0
for n in numbers:
    total+=n
    print(total)

#q10. Fibbonacci series
n = 10
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

#end