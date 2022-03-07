x = int(input("Enter the number: "))


def pattern(number):
    if is_even(number):
        number = number / 2
        print(number)
        pattern(number)
    elif number == 1:
        return None
    else:
        number = number * 3 + 1
        print(number)
        pattern(number)


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


pattern(x)
