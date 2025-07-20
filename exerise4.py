'''
1) Write a python program to validate a person can vote or not 
* take the age as input from the user
if age < 18 print he can't vote
if age > 18 print he can vote
if age > 90 print please stay at home
if age is 18 than print please make a voter id 
'''

age=int(input("Enter Your age \n")) #input
if(age<18):
    print("he can't vote")
elif(age>18 and age<90):
    print("he can vote")
elif(age>90):
    print("Please stay at home")
elif(age==18):
    print("please make voter id") 
else:
    print("else")               