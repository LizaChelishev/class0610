number = int(input('Enter a number'))
while number != 0 :
    while abs(number) >= 10 :
        number = number // 10
    print('Number is ' + str(number))
    number = int(input('Enter a number'))
