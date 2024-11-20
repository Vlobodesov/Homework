grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
my_dict = {}
for i in range(len(grades)):
    my_dict[students[i]] = sum(grades[i])/len(grades[i])
print(my_dict)









