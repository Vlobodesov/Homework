def get_matrix(n,m,value):
    matrix = []
    for row in range(n):
        matrix.append([])
        for col in range(m):
            matrix[row].append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

























#Пункты задачи:
#Объявите функцию get_matrix и напишите в ней параметры n, m и value.
#Создайте пустой список matrix внутри функции get_matrix.
#Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
#В первом цикле добавляйте пустой список в список matrix.
#Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
#Во втором цикле пополняйте ранее добавленный пустой список значениями value.
#После всех циклов верните значение переменной matrix.
#Выведите на экран(консоль) результат работы функции get_matrix.
#result1 = get_matrix(2, 2, 10)
#result2 = get_matrix(3, 5, 42)
#result3 = get_matrix(4, 2, 13)
#print(result1)
#print(result2)
#print(result3)

#Вывод на консоль:

#[[10, 10],
#[10, 10]]

#[[42, 42, 42, 42, 42],
 #[42, 42, 42, 42, 42],
 #[42, 42, 42, 42, 42]]

#[[13, 13],
 #[13, 13],
 #[13, 13],
 #[13, 13]]
