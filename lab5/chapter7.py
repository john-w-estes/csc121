#Variables used in the example 'if' statements
a = 4
b = 5
c = 6

#Basic comparisons
if a < b:
    print("a is less than b.")

if a > b:
    print("a is greater than b.")

print("Done")

#Equal

if a == b:
    print("a is equal to b.")

if a != b:
    print("a is not equal to b.")

print("Done")

#Indentation matters
if a == 1:
    print("If a is one, this will print.")
    print("So will this.")

print("This will always print because it is not indented.")

#and
if a < b and a < c:
    print("a is less than b and a is less than c.")

# Non-exclusive or:
if a < b or a < c:
    print("a is less than b or a is less than c (or both).")

#Boolean data type. This is legal!
a = True
if a:
    print("a is true.")

if not a:
    print("a is false.")

a = True
b = False

if a and b:
    print("a and b are both true")

a = 3
b = 3
c = a == b
print(c)

#These are also legal and will trigger as being true because
# these values are not zero:
if 1:
    print("1")

if "A":
    print("A")

if 0:
    print("Zero")

#Comparing variables to multiple values.
# The first is statement appears to work, but it will always
# trigger as true even if the variables a and b are not equal.
# This is because "b" by itself is considered true.
a = 'c'
if a == "B" or "b":
    print(" a is equal to b... Maybe")

# This is the proper way to do if statements:
if a == "B" or a == "b":
    print("a is equal to b.")

# Example 1: If statement
temperature = int(input("What is the temerpature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside!")
print("Done")

# Example 2: Else statement
temperature = int(input("What is the temerpature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside!")
else:
    print("It is not hot outside.")
print("Done")

# Example 3: Else if statements
temperature = int(input("What is the temerpature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside!")
elif temperature > 110:
    print("Oh man, you could fry eggs on the pavement.")
elif temperature < 30:
    print("Baby, it's cold outside.")
else:
    print("It is ok outside.")
print("Done")

# Comparison using string/text
# The input statement will ask the user for input and put in a user_name.
user_name = input("What is your name? ")
if user_name == "Paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")
