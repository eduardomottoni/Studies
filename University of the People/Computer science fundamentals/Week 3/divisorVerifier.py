
# my function will receive a number and tell if its number is divisible by all numbers until the mid of the range of numbers between 2 and the number of choices

# update 1.2, now the program tells if the number is prime or not, awesome!

def division(number,amount_divisors):
    i=1
    while(i<int(amount_divisors)):
        verifyPrime = True
        divider = i+1
        result = number%divider
        if result == 0:
            print('{} is divisible by {}'.format(number, divider))
            verifyPrime = False
        else:
            print('{} is not divisible by {}'.format(number, divider))
        i+=1
    return verifyPrime
    
def main():
    while(True):
        print('Type a number the number to be divided')
        number = int(input())
        amount_divisors = int(number/2)
        print('Press enter to verify the division of {} until {}'.format(number,amount_divisors))
        input()
        isPrime = division(number,amount_divisors)
        if isPrime == True:
            print('The number {} is prime!'.format(number))
        else:
            print('The number {} is not prime. :/'.format(number)) #all we love prime numbers, right?
        print()

main()
