a = 19
b = 15
c = 15

if (not(a == b)):
    print('True')


if (not(b == c)):
    print("False")


if not ((a == 4) == (a == 19)):
    print('True')
else:
    print('False')


a = int(input('Enter your number :'))

if not (a%2 == 0):
    print('ODD')
else:
    print('EVEN')