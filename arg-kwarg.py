def argskwargs(*args, **kwargs):
    print(args)
    print(1,kwargs)    


args=(1,2,3,4,5,6,7,8)

kwargs={
    "employeeName":"Rohan",
    "employeeSalary":15000.52,
    "isActive":True,
    "role":"Front end dev",
    "address":['bangalore','devenhali'],
    "phonenumber":4556789953,
    "hobbies":("dance","sining"),
    "skills":{"python","django"},
}

name="laxmi"

argskwargs(name,args,**kwargs)


argskwargs(name,args,)
argskwargs(name,**kwargs)