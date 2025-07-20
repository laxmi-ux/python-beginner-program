stack=[]
for i in range(10):
    n=int(input("Enter the element to insert into stack:"))
    print(n, "is inserted into stack")
    stack.append(n)
    print("the top element in the stack is: ",stack[-1])
print("Your stack is", stack)   


print("\n")
print("Pop operation:\n")
n=int(input("Enter 1 for  pop operation \n Enter 2 to check stack is empty or not"))
if(n==1):
    print("I am poping from the stack :",stack[-1])
    stack.pop()
    print("Your stack is ", stack)
elif(n==2):
    if not stack:
        print("stack is empty")
    else:
        print("stack is not  empty")            