
# my function will reveice a number and tells if its number is divisible by 2, 3, 4 and 5

def division(number,amount_divisors):
    i=1
    while(i<int(amount_divisors)):
        divider = i+1
        result = number%divider
        if result == 0:
            print('The number is divisible by {}'.format(divider))
        else:
            print('The number is not divisible by {}'.format(divider))
        i+=1
while(True):
    print('Type a number the number to be divided')
    number = int(input())
    print('Type the amount of divisors you want to verify')
    amount_divisors = int(input())
    division(number,amount_divisors)
    print()
