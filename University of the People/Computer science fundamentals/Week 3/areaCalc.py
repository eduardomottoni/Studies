#math.pi defines the irrational number PI
import math

def print_volume(r):
     volume = (4*math.pi*(r**3))/3 # the equation must have some brackets
     print('The radius is {} and the volume is:'.format(r))
     print("%.2f" % volume) #this is to print just 2 decimals
     print()
     
def main():
    print('Declare the radius of the sphere.') #the users input the radius of the sphere
    radius = int(input()) #receive the argument and passes it to the function
    print_volume(radius)
while(True):
    main()

