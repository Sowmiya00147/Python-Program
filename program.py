#reverse string
def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

#frequent number
from collections import Counter
def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
print(most_frequent([1,2,3,2,4,2,5]))

#prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))


#missing Number
def find_missing_number(arr, n):
    total = n * (n + 1) // 2
    return total - sum(arr)
print(find_missing_number([1, 2, 4, 5], 5))

#intersection of 2 list
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))


#2 largest number
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]
print(second_largest([10, 20, 4, 45, 99]))


#count vowels
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')
print(count_vowels("Hello World"))

#merge 2 sorts
def merge_sorted_lists(a, b):
    return sorted(a + b)
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

#non repeating character
from collections import Counter
def first_non_repeating(s):
    count = Counter(s)
    for ch in s:
        if count[ch] == 1:
            return ch
    return None
print(first_non_repeating("swiss"))

#output of following code
a = [1, 2, 3]
b = a
c = a[:]
print(a == b)
print(a is b)
print(a == c)
print(a is c)

#output
nums = [1, 2, 3, 4, 5]
result = ['Even' if x % 2 == 0 else 'Odd' for x in nums]
print(result)

#output
a, *b, c = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)









