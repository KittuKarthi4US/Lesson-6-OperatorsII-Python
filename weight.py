cm = float(input('Enter your weight in cm :'))
kg = float(input('Enter your weight in kg :'))

Bmi = kg/(cm/100)**2

if Bmi <= 18.4:
    print( ' You are light weight')
elif Bmi <= 24.9:
    print('You are healthy')
elif Bmi <= 29.9:
    print('You are overweight')
elif Bmi <= 34.9:
    print('You are severly overweight')
elif Bmi <= 39.9:
    print('You are obese')
else:
    print ('You are severly obese')