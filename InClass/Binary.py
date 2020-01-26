import math

def is_clean(input_string):
    error = 0 #this will be returned at the end, 1 means error (unclean), 0
    #means no error (clean)
    for x in input_string:
        if x != "0" and x != "1":
            error = 1
            break
    return error

def binary_to_decimal():
    number = input("input binary number: ")
    while (is_clean(number) == 1):
        number = input("not a valid binary number: ")
    reversed = number[::-1]
    decimal = 0
    for x in range(len(reversed)):
        if reversed[x] == "1":
            decimal += (2 ** x)
    print(decimal)

def calculate_sum(number_1, number_2):
    return number_1 + number_2

def calculate_avg(number_1, number_2):
    return calculate_sum(number_1, number_2) / 2

def max(number_1, number_2, number_3):
    current_max = 0
    if number_1 >= number_2:
        current_max = number_1
        if number_3 > number_1:
            current_max = number_3
    if number_2 > number_1:
        current_max = number_2
        if number_3 > number_2:
            current_max = number_3

    print(current_max)

def consecutive(number_1, number_2):
    test = (number_1-number_2)**2
    if test == 1:
        print("consecutive")
    else:
        print("not consecutive")

consecutive(59,62)

def area(radius):
    return math.pi*(radius**2)

def circumference(radius):
    return math.pi*(radius*2)

def vol_sphere(radius):
    return (4/3)*math.pi*(radius**3)

def vol_cylinder(radius, height):
    return math.pi*(radius**2)*height
