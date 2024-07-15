# я сделала так
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students1=list(students)
students1.sort()
sredny_bal={students1[0]:sum(grades[0])/len(grades[0]),
            students1[1]:sum(grades[1])/len(grades[1]),
            students1[2]:sum(grades[2])/len(grades[2]),
            students1[3]:sum(grades[3])/len(grades[3]),
            students1[-1]:sum(grades[-1])/len(grades[-1])}
print(sredny_bal)
# в вебинаре разбирали так
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades_x=[sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),
          sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]),
          sum(grades[4])/len(grades[4])]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students1=sorted(students)
sredny_bal1=dict(zip(students1,grades_x))
print(sredny_bal1)


