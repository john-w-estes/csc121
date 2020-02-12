def print_hello():
    '''This is a comment that defines a function'''
    print("Hello!")

def print_goodbye():
    print("Bye!")


def main():
    '''This is my main program function'''
    print_hello()
    print_goodbye()

#Only run the main function if we are running this file. Don't run it
#if we are importing the file.
if __name__ == "__main__":
    main()

def print_number(my_number):
    print(my_number)

print_number(55)
print_number(25)
print_number(8)

def add_numbers(a, b):
    print(a, b)

add_numbers(11, 7)

#Add two numbers and return the result
def sum_two_numbers(a, b):
    result = a + b
    return result

# Capture the function's result into a variable
# by putting "my_result =" in front of it.
# (Use whatever variable name best describes the data,
# don't blindly use 'my_result' for everything.)
my_result = sum_two_numbers(22, 15)

#Now that I captured the result, I print it.
print(my_result)

#Volume of a cylinder
def volume_clinder(radius, height):
    '''Returns the volume of a cylinder given radius, height.'''
    pi = 3.1415926653589
    volume = pi * radius ** 2 * height
    return volume

six_pack_volume = volume_clinder(2.5, 5) * 6

#Function that prints the result
def sum_print(a, b):
    result = a + b
    print(result)

#Function that returns the result
def sum_return(a, b):
    result = a + b
    return result

# This prints the sum of 4+4
sum_print(4, 4)

#This does not
sum_return(4, 4)

#This will set x1 to the sum
#It actually gets a value of 'none'
x1 = sum_print(4, 4)
print("x1 = ", x1)

#This will set x2 to the sum
# and print it properly
x2 = sum_return(4, 4)
print("x2 = ", x2)

def calculate_average(a, b):
    ''' Calculate an average of two numbers '''
    result = (a + b)/2
    return result

x = 45
y = 56

average = calculate_average(x, y)
print(average)

# Define a simple function that prints x
def f(x):
    x += 1
    print(x)

#Set y
y = 10
#Call the Function
f(y)
#Print y to see if it changed
print(y)

#Example 1
def a():
    print("A")

def b():
    print("B")

def c():
    print("C")

a()
#Example 2
def a():
    b()
    print("A")

def b():
    c()
    print("B")

def c():
    print("C")

a()

#Example 3
def a():
    print("A")
    b()

def b():
    print("B")
    c()


def c():
    print("C")

a()

#Example 4
def a():
    print("A start")
    b()
    print("A end")

def b():
    print("B start")
    c()
    print("B end")

def c():
    print("C start and end")

a()

#Example 5
def a(x):
    print("A start, x = ", x)
    b(x+1)
    print("A end, x = ", x)

def b(x):
    print("B start, x = ", x)
    c(x+1)
    print("B end, x = ", x)

def c(x):
    print("C start and end, x = ", x)

a(x)

#Example 6
def a(x):
    x = x + 1

x = 3
a(x)

print(x)

#Example 7
def a(x):
    x = x + 1
    return x

x=3
a(x)
print(x)


#Example 8
def a(x):
    x = x + 1
    return x

x=3
x = a(x)
print(x)


#Example 9
def a(x, y):
    x = x + 1
    y = y + 1
    print(x, y)

x = 10
y = 20
a(x, y)

#Example 10
def a(x, y):
    x = x + 1
    y = y + 1
    return x
    return y

x = 10
y = 20
z = a(x, y)

print(z)

#Example 11
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y

x = 10
y = 20
z = a(x, y)

print(z)

#Example 12
def a(x, y):
    x = x + 1
    y = y + 1
    return x, y

x = 10
y = 20
x2, y2 = a(x, y) #Most computer languages do not support this

print(x2)
print(y2)

# Example 13:
def a(my_data):
    print("function a, my_data = ", my_data)
    my_data = 20
    print("function a, my_data = ", my_data)

my_data = 10

print("global scope, my_data = ", my_data)
a(my_data)
print("global scope, my_data = ", my_data)

# Example 14:
def a(my_list):
    print("function a, list = ", my_list)
    my_list = [10, 20, 30]
    print("function a, list = ", my_list)

my_list = [5, 2, 4]

print("global scope, list = ", my_list)
a(my_list)
print("global scope, list = ", my_list)

# Example 15:
# New Concept!
# Covered in more detail in a later chapter
def a(my_list):
    print("function a, list = ", my_list)
    my_list[0] = 1000
    print("function a, list = ", my_list)

my_list = [5, 2, 4]

print("global scope, list = ", my_list)
a(my_list)
print("global scope, list = ", my_list)
