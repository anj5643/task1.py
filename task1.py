# 1. Sum of Two Numbers – Take input & print their sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

# 2. Odd or Even Checker – Check if a number is odd/even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Factorial Calculation – Using a loop or recursion.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

# 4. Fibonacci Sequence – Generate first n numbers.
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 5. String Reverse – Reverse user-input string.
s = input("Enter a string: ")
print(s[::-1])

# 6. Palindrome Check – Is the word same forward & backward?
w = input("Enter a word: ")
if w == w[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 7. Leap Year Check – Check if a given year is leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")

# 8. Armstrong Number – Example: 153 → 1³ + 5³ + 3³ = 153.
num = int(input("Enter a number: "))
temp = num
total = 0
while temp > 0:
    d = temp % 10
    total = total + d ** 3
    temp = temp // 10
if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
