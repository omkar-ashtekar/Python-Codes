def check_remainder(a, b):
    if b == 0:
        raise Exception("Can not divide by 0")
        raise ZeroDivisionError
    result = a // b
    remainder = a % b
    print(a, "/", b, "are", result, "and remainder is", remainder)


def main():
    num1 = int(input("Enter first number\n"))
    num2 = int(input("Enter second number\n"))
    check_remainder(num1, num2)


main()
