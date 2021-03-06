# Напишите программу, которая вычисляет и выводит в stdout сумму цифр всех чисел массива,
# которые находятся в диапазоне между средним значением и 90 перцентилем. Массив чисел
# считывается из файла, путь к которому передается в виде аргумента командной строки (не stdin).
# Формат файла: каждое число (int_64) заканчивается символом новой строки.
# Примечание: конечно, задание подразумевает реализацию методов сортировки массива, поиска
# среднего значения и перцентиля.
import sys
array = []
range_sum = 0
with open(sys.argv[1], "r") as file:# Считываем данные из файла(передаем с помощью аргумента в командной строке)
	for line in file.readlines():
		array.append(int(line.strip()))#Передаем данные из файла в список array для дальнейшей работы
array.sort()#отсортированный массив

print(f"Отсортированный массив:\n{array}")
#расчет среднего
average = round(sum(array)/len(array), 2)
print("Среднее значение массива:", average)
#Расчет ранга 90-го перцентиля.
percentil_range = round(90/100*len(array))
print("90-ый перцентиль: ", array[percentil_range-1])
#Расчет суммы
for i in array:
	if (i>average and i<=array[percentil_range-1]) or (i>array[percentil_range-1] and i<=average):
		range_sum += i
print("Сумма чисел между средним и 90-ым перцентилем:",range_sum)


