# Task № 1

# day = int(input("Enter week day: "))
# if(day > 7):
#     print('Error')
# if (day == 6) or (day == 7):
#     print("Yes")
# elif(day < 6):
#     print("No")



# Task № 2

# for X in range(2):
#     for Y in range(2):
#         for Z in range(2):
#             print(f'{X, Y, Z} : {(not (X or Y or Z)) == (not X and not Y and not Z)}')


# Task №3

# X = int(input('Enter the coordinate X: '))
# Y = int(input('Enter the coordinate Y: '))
# if (X == 0 or Y == 0):
#     print(f'{X,Y} : the entered data does not meet the condition')
# elif (X > 0 and Y > 0):
#     print(f'{X,Y} : the coordinates of the plane are in {1} quarters')
# elif (X < 0 and Y > 0):
#     print(f'{X,Y} : the coordinates of the plane are in {2} quarters ')
# elif (X < 0 and Y < 0):
#     print(f'{X,Y} : the coordinates of the plane are in {3} quarters')
# elif (X > 0 and Y < 0):
#     print(f'{X,Y} :the coordinates of the plane are in {4} quarters')


# Task № 4

# plane = int(input('Enter quarter plane: '))
# if (plane == 1):
#     for X in range(0, 10):
#         for Y in range(0, 10):
#             print(f'{X,Y}')
# elif (plane == 2):
#     for X in range(-10, 0):
#         for Y in range(0, 10):
#             print(f'{X,Y}')
# elif (plane == 3):
#     for X in range(-10, 0):
#         for Y in range(-10, 0):
#             print(f'{X,Y}')
# elif (plane == 4):
#     for X in range(0, 10):
#         for Y in range(-10, 0):
#             print(f'{X,Y}')


# Task № 5
# import math
# X1 = int(input('Enter coordinate X1: '))
# Y1 = int(input('Enter coordinate Y1: '))
# X2 = int(input('Enter coordinate X2: '))
# Y2 = int(input('Enter coordinate Y2: '))
# d = float (round((math.sqrt(math.pow(X1 - X2, 2) + math.pow(Y1 - Y2,2))),2))
# print(d)

