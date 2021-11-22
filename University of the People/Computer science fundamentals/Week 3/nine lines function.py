import os

def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()
    
def nine_lines(): # as simple as given, it just print the function that prints 3 lines, three times.
    three_lines()
    three_lines()
    three_lines()

def clear_screen():

    #DID NOT WORK#os.system('CLS') #os. calls 'os' class and the funcion system with the argument 'clear'
    print("\n" * 40)
    print('the screen was cleared')
    print("\n" * 30)
    
def main():
    nine_lines()
    input()
    clear_screen()
    
main()
