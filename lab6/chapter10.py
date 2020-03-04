#types
def tell_me_type(x):
    print("x =", x, "and is type:", type(x))

tell_me_type(3)
tell_me_type(3.145)
tell_me_type("Hello neighbor!")
tell_me_type(True)

x = (2, 3, 4, 5)
tell_me_type(x)

x = {2, 3, 4, 5}
tell_me_type(x)

x = [1, 2]
print(x)
print(x[0])

x = [1, 2]
print(x)

x[0] = 222
print(x)

x = (1,2)
print(x)

#x[0] = 222
#print(x)

def print_list(my_list):
    for item in my_list:
        print(item)

my_list = [101, 20, 50, 110]
print_list(my_list)

my_list = ["Hello", "Aloha", "Hola", "Ciao"]
print_list(my_list)

my_list = [[1,2], ["red fish", "blue fish"], ["Mercury", "Venus", "Earth"]]
print_list(my_list)

for index, value in enumerate(my_list):
    print(index, value)

my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)

#User - created lists
my_list = []

#for i in range(5):
#    user_input = input("Enter an integer: ")
#    user_input = int(user_input)
#    my_list.append(user_input)
#    print(my_list)

#creat a list with 100 0's
my_list = [0] * 100

#copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

#Initial sum should be zero
list_total = 0

# Loop up from 0 to the number of elements
# in the array
for index in range(len(my_list)):
    #Add elements 0, next 1, next 2, etc
    list_total += my_list[index]

# Print results
print(list_total)

#copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

#Initial sum should be zero
list_total = 0

# Loop up from 0 to the number of elements
# in the array
for item in my_list:
    #Add elements 0, next 1, next 2, etc
    list_total += item

# Print results
print(list_total)

#copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

#Initial sum should be zero
list_total = 0

# Loop up from 0 to the number of elements
# in the array
for index in range(len(my_list)):
    #Add elements 0, next 1, next 2, etc
    my_list[index] = my_list[index] * 2

# Print results
print(my_list)

#Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

#Loop through each element in my_list
for item in my_list:
    #This doubles item, but not change the array
    #because item is a copy of a single element.
    item = item*2

print(my_list)

x = "This is a sample string"
#x = "0123456789"

print("x = ", x)

#Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])

#from the right side
print("x[-1]=", x[-1])

#Accessings 0-5
print("x[:6]=", x[:6])
#Access 6
print("x[6:]=", x[6:])
#Access 6-8
print("x[6:9]=", x[6:9])

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

for character in "This is a test.":
    print(character)

#Months printing exercise
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))

print(months[3*n - 3:3 * n])

#Secret Codes
plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(c, end=' ')
print()

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(ord(c), end=' ')
print()

plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end=' ')
print()

plain_text = "This is a test. ABC abc"

#Encryption
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

#Decryption
encrypted_text = 'Uijt!jt!b!uftu/!BC!bcd'

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)

# Create an empty associative array
# Note the curly brackets
x = {}

#Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1

# Fetch and print an item
print(x["fred"])
