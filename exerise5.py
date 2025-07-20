'''
1. Take a input and evaluate the expressions
a) Take the student name
b) Take the student english marks
maths, science, social, tamil, hindi, while taking the inputs it should be in the range (0-100)
c) Calculate the % and print
% < 35% print fail and print the grade 'F'
% > 35% and < 55% print just pass and print the grade  'D'
% > 55% and < 60% print pass and print the grade 'C'
% > 60% and < 75% print average and print the grade 'B'
% > 75% and < 90% print good and print the grade 'A'
% > 90% and <100% print excellent and print the grade 'A+'
'''

#a)
student=input("Enter student name:\n")
#b)
print("Enter your marks:\n")
english=int(input("enter the english marks \n"))
maths=int(input("enter the  math marks \n"))
science=int(input("enter the  science marks \n"))
social=int(input("enter the  soical marks \n"))
tamil=int(input("enter the  tamil marks \n"))
hindi=int(input("enter the  hindi marks \n"))


if(english<0 or english>100 or maths<0 or maths>100 or science<0 or science>100 or
 social<0 or social>100 or tamil<0 or tamil>100 or hindi<0 or hindi>100):
 print("Please Give the marks between 0-100")
else:
    sum=english+maths+science+social+tamil+hindi
    avg=sum/6

    if(avg<35):
        print("You are failed Yours % is", avg, "Grade 'F'")

    elif(avg>35 and avg<55):
        print("You are just pass Yours % is", avg, "Grade 'D'")
    elif(avg<55 and avg>60):
        print("You are pass Yours % is", avg, "Grade 'C'")
    elif(avg<60 and avg>75):
        print("You are average  Yours % is",avg, "Grade 'B'")   
    elif(avg<75 and avg>90):
        print("You are good  Yours % is",avg, "Grade 'A'")   

    else:
     print("You are excellent  Yours % is",avg, "Grade 'A+'")           


