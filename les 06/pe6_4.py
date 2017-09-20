studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
    lst =[]
    for student in studentencijfers:
        gemstudent = sum(student)/len(student)
        lst.append(gemstudent)
    return (lst)


def gemiddelde_van_alle_studenten(studentencijfers):
    gemall = sum(gemiddelde_per_student(studentencijfers))/len(gemiddelde_per_student(studentencijfers))
    return (gemall)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))