listNames = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
average = [9.0, 7.3, 5.8, 6.7, 8.5]

firstNameList = []

firstNameList = [name[0] for name in listNames]

studentsAverageList = list(zip(firstNameList, average))
# print(studentsAverageList)

candidates= [student[0] for student in studentsAverageList if student[1] >= 8]

print(candidates)

