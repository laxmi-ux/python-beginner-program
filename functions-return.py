def employeesdetails(ename,esalary):
    print("Employees name is:",ename,"Salary is :",esalary)
    return esalary

s1=employeesdetails("Anees",50000)
s2=employeesdetails("Laxmi",45000)
s3=employeesdetails("Priya",20000)
s4=employeesdetails("Neha",88000)
s5=employeesdetails("aakrit",90000)

salaryissues=s1+s2+s3+s4+s5
print("Total Amount Used for Sending By Employees is",salaryissues)