'''
Write a python program to create a basic calcluator which can perfrom 
a) addition
b)Substraction
c) Division
d) Multiplication
'''

def add(x,y):                             #accodint to user input the function is called
    return x+y


def sub(x,y):
    return x-y


def multiply(x,y):
    return x*y


def divide(x,y):
    #5/0 print("error")
    if y==0:
        return "cannot divide by zero"
    return x/y

while True:                                        #first time it will execute after that it will going to call the function 
    print("Enter 'add' for addition")                 
    print("Enter 'sub' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 1 for quit")

    userinput=input(":")                                                       #
    if userinput=='1':
        break
    elif userinput in ("add","sub","multiply","divide"):
        num1=int(input("Enter the first value:\n"))
        num2=int(input("Enter the Second value:\n"))

        if userinput=="add":
            print("Result :",add(num1,num2))

        elif userinput=="sub":
            print("Result :",sub(num1,num2))

        elif userinput=="multiply":
            print("Result :",multiply(num1,num2))

        elif userinput=="divide":
            print("Result :",divide(num1,num2))    

        else:
            print("Invalid input")    
        
        
