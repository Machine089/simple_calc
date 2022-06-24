print("    Calculator    ")

r = str(input("If you want to open help - enter 'Help', other 'Skip' "))
ref = ("""    References
Operation:
'+' - addition
'-' - subtraction
'*' - multiplication
'/' - division
'**' - square
'//' - integer division
'%' - remainder division
'percent' - percentage number
'share' - percentage share
""")

if r == 'Help':
    print(ref)


def easy_math_operation():
    if action == '+':
        return print(a + b)
    if action == '-':
        return print(a - b)


def middle_math_operation():
    if action == '*':
        return print(a * b)
    if action == '/':
        return print(a / b)
    if action == '**':
        return print(a ** b)


def hard_math_operation():
    if action == '//':
        return print(a // b)
    if action == '%':
        return print(a % b)


def equation():
    if action == 'percent':
        return print((int(a) * int(b)) / 100)
    if action == 'share':
        return print((int(a) / int(b)) * 100)


while True:
    action = str(input('Enter the sign of the required operation: '))
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))

    if action == '+' or '-':
        easy_math_operation()
    if action == '*' or '/' or '**':
        middle_math_operation()
    if action == '//' or '%':
        hard_math_operation()
    if action == 'percent' or 'share':
        equation()
    x = str(input("For exit press 's', if continue 'n': "))
    if x == 's':
        break
