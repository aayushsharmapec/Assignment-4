#grade_of_students
marks= float(input('enter your marks:'))
if(marks<25):
    print("your grade is:F")
elif(marks>=25 and marks<45):
    print("your grade is:E")
elif(marks>=45 and marks<50):
    print('your grade is:D')
elif(marks>=50 and marks<60):
    print('your grade is:C')
elif(marks>=60 and marks<80):
    print('your grade is:B')
elif(marks>=80 and marks<=100):
    print('your grade is:A')