#Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
#Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
import math
n = int(input("n="))
i = 0
sum = 0

lis = [round((1 + 1 / n) ** n) for n in range(1, n + 1)]
while n>i:
    sum+=lis[i]
    i+=1
print(lis)
print(sum)
