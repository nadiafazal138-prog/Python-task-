
# Exercise 1: Variables and Data Types

name = "Nadia"
age = 25
salary = 50000
is_developer = True

print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Developer:", is_developer)


# Exercise 2: Add Two Numbers

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)


# Exercise 3: Basic Calculator

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero")


# Exercise 4: Even or Odd

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Exercise 5: Positive, Negative or Zero

number = float(input("\nEnter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Exercise 6: Pass or Fail

marks = float(input("\nEnter marks out of 100: "))

if 0 <= marks <= 100:
    if marks >= 50:
        print("Pass")
    else:
        print("Fail")
else:
    print("Invalid marks")


# Exercise 7: Largest of Three Numbers

a = float(input("\nEnter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# Exercise 8: Multiplication Table

number = int(input("\nEnter a number for its table: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# Exercise 9: Sum from 1 to N

n = int(input("\nEnter a positive number: "))
total = 0

if n >= 1:
    for i in range(1, n + 1):
        total += i
    print("Total sum:", total)
else:
    print("Please enter a positive integer")


# Exercise 10: Countdown Using While Loop

count = int(input("\nEnter countdown starting number: "))

while count > 0:
    print(count)
    count -= 1

print("Done!")
