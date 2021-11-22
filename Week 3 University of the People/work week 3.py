#DEVELOPED BY EDUARDO OTTONI, PUBLIC USES MEAN REFERENCES

def getname():
    print("write your name")
    name = input() #the imput function means 
    return name

def getcourse():
    print("write your course")
    course = input()
    course += "'"
    return course
    
def main () :
    name = getname()
    course = getcourse()
    print("The name of the student is: '"+name+"' and the course of the student is: '" + course)
    input()
main()
