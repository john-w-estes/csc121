# Problem 1
def print_n_stars(n):
  for i in range(n):
    print('*', end=' ')
  print()

print_n_stars(10)

#Problem 2
print_n_stars(10)
print_n_stars(5)
print_n_stars(20)

#Problem 3
def print_star_grid(m,n):
    for row in range(m):
        for col in range(n):
            print("*", end=' ')
        print()

print_star_grid(10, 10)

#Problem 4
""" He mentions a 5x10 rectangle. Using standard matrix indices,
this is a 10x5 rectangle.
"""
print_star_grid(10,5)

#Problem 5
print_star_grid(5,20)

#Problem 6
def problem_6():
    for row in range(10):
        for col in range(10):
            print(str(col), end=' ')
        print()

problem_6()

#Problem 7
def problem_7():
    for row in range(10):
        for col in range(10):
            print(str(row), end=' ')
        print()

problem_7()

#Problem 8
def problem_8():
    for row in range(10):
        for col in range(10):
            if row >= col:
                print(str(col), end=' ')
        print()

problem_8()

#Problem 9
def problem_9():
    for row in range(10):
        for col in range(row):
            print(" ", end=' ')
        for col in range(10-row):
            print(str(col), end=' ')
        print()

problem_9()

#Problem 10
def problem_10():
    for row in range(1,10):
        for col in range(1,10):
            if row*col < 10:
                print(" "+str(row*col), end=' ')
            else:
                print(str(row*col), end=' ')
        print()

problem_10()

#Problem 11
def problem_11():
    for row in range(1,10):
        for col in range(9-row):
            print(' ', end=' ')
        for col in range(1,row+1):
            print(str(col), end=' ')
        for col in range(row-1, 0, -1):
            print(str(col), end=' ')
        print()

problem_11()

#problem 12
def problem_12():
    for row in range(1,10):
        for col in range(9-row):
            print(' ', end=' ')
        for col in range(1,row+1):
            print(str(col), end=' ')
        for col in range(row-1, 0, -1):
            print(str(col), end=' ')
        print()
    for row in range(1,9):
        for col in range(row):
            print(' ', end= ' ')
        for col in range(1,10-row):
            print(str(col), end=' ')
        print()

problem_12()

#problem 13
def problem_13():
    for row in range(1,10):
        for col in range(9-row):
            print(' ', end=' ')
        for col in range(1,row+1):
            print(str(col), end=' ')
        for col in range(row-1, 0, -1):
            print(str(col), end=' ')
        print()
    for row in range(1,9):
        for col in range(row):
            print(' ', end= ' ')
        for col in range(1,10-row):
            print(str(col), end=' ')
        for col in range(8-row, 0, -1):
            print(str(col), end=' ')
        print()

problem_13()
