#q1. smallest number in a list
def smallest(n):
    small = n[0]
    for i in n:
        if i < small:
            small = i
    return small
numbers = [5, 2, 8, 1, 9]
print("Smallest number:", smallest(numbers))

#q2. average of all numbers in a list
def average(n):
    total = 0
    for i in n:
        total = total + i
    avg = total / len(n)
    return avg
numbers = [10, 20, 30, 40]
print("Average:", average(numbers))

#q3. Count how many times a particular number occurs in a list.
def count_number(m,n):
    count=0
    for i in m:
        if i == n:
            count = count + 1
    return count
numbers = [1,2,4,2,4,2]
print("count: ", count_number(numbers, 3))  

#q4. Reverse a list.
def reverse_list(n):
    rev = []
    for i in range (len(n)-1, -1, -1):
        rev.append(n[i])
    return rev
numbers = [1,2,3,4,5]
print(reverse_list(numbers))

#q5. Sort a list in ascending order.
def sort_list(n):
    for i in range (len(n)):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    return n
numbers = [5,2,8,1]
print(sort_list(numbers))

#q6. Find the common elements of two tuples.
def common_elements(t1, t2):
    common = []
    for i in t1:
        if i in t2:
            common.append(i)
    return common
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
print(common_elements(tuple1, tuple2))

#q7. Convert a list into a tuple.
def list_to_tuple(n):
    return tuple(n)
numbers = [1, 2, 3, 4]
print(list_to_tuple(numbers))

#q8. Convert a tuple into a list.
def tuple_to_list(t):
    return list(t)
data = (10, 20, 30)
print(tuple_to_list(data))

#q9. Find the union, intersection and difference of two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Union =", a | b)
print("Intersection =", a & b)
print("Difference =", a - b)

#q10. Remove duplicate values from a list using a set.
def remove_duplicates(n):
    return list(set(n))
numbers = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(numbers))