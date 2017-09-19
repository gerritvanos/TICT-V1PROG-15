def avg(lst):
    for student in lst:
        avgstudent = sum(student)/len(student)
        print(avgstudent)

grades = [[95,92,86,87],[66,54],[89,72,100],[33,0,0]]
avg(grades)