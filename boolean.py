#Takes input of user
num = input('Give me a number: ')
num = int(num)

#Takes input and checks remainder to see if it equals odd or even
is_odd = num % 2 != 0

#returns true if it is odd and false if it is even
if is_odd:
    print(f'{num} is odd')
else:
    print(f'{num} is even')