''' 
1.write a python program to initialize variable and print its datatype
2. do type conversion for:-
    a) int to string
    b) string to int
    c) bool to string 
    d) string to bool
'''
#1.
name="laxmi pal"
role="programmer"
salary=20000
print(name,role,salary)
print(type(name),type(role),type(salary))

#2.
#a :-int to string
mynum="100"
print(mynum)
print(type(mynum))

#b :- string to int
mynum=int(mynum)
print(mynum)
print(type(mynum))

print("\n")  # string should be first number
mynum=122345679
print(type(mynum))
mynum=str(mynum)
print(type(mynum))

#c :- boolean to string
mybool=True
print(type(mybool))
mybool=str(mybool)
print(type(mybool))


#d :- string to boolean

mybool="True"
print(type(mybool))
mybool=bool(mybool)
print(type(mybool))