print('Bank of Eric')
pin = int(input('Enter your pin: '))
while pin != 1234:
    pin = int(input('Incorrect pin, enter your pin again: '))
if pin == 1234:
    print ('PIN accepted!')