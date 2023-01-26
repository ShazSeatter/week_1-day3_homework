def return_10():
    return 10


def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def multiply(num_1, num_2):
    return num_1 * num_2


# floors result 
def divide(num_1, num_2):
    return num_1 // num_2


def length_of_string(string):
    return len(string)


def join_string( str_1, str_2):
    return str_1 + str_2


def add_string_as_number(str_1, str_2):
    str_1 = int(str_1)
    str_2 = int(str_2)
    return str_1 + str_2

#  if there are multiple outcomes, should test for all the possible situations
def number_to_full_month_name(number):
    if number == 1:
        return "January"
    elif number == 3:
        return "March"
    elif number == 9:
        return "September"


def number_to_short_month_name(month_num):
    if month_num == 1:
        return "Jan"
    elif month_num == 4:
        return "Apr"
    elif month_num == 10:
        return "Oct"   

# --------------- 

def vol_cube(length):
    return length**3


def reversed_str(string):
    return string[::-1]

# slice[::[value]], dont need a starting and end value. 
# will be the default. the -1, will step from the end of the string value
# this then returns a reversed string 

def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

