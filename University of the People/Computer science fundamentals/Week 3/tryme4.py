#this code is about printing lines and nested functions
def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()
    
def nine_lines(): #nested fuction
    three_lines() 
    three_lines() 
    three_lines()
    # as simple as given, it just print the function that prints 3 lines, three times.

def clearScreen(): #nested function
    print('Calling clearScreen')
    new_line()
    three_lines()
    three_lines()
    nine_lines()
    nine_lines()
    
    #another way to do it print('\n' * 25) works as well

def main():
    print('Printing nine lines')
    nine_lines() #print 9 dots
    print('press enter to clear screen') #help users to understand the program
    input() #wait an enter before clear screen
    clearScreen() #prints 21 dots
    input() # this function holds the program static
    
main() # Lot of languages define a function as main to the program
