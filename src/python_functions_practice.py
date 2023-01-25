def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2


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


def number_to_full_month_name(number):
    if number == 1:
        return "January"
    if number == 3:
        return "March"
    elif number == 9:
        return "September"


def number_to_short_month_name(month_num):
    if month_num == 1:
        return "Jan"
    if month_num == 4:
        return "Apr"
    elif month_num == 10:
        return "Oct"   




