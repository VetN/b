import random
# наивная сортировка
# массив из целых чисел
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
is_sort = False  # пока не отсортирован
count = 0
while not is_sort:
    count += 1

    random.shuffle(array)  # перемешиваем массив

    # проверяем отсортирован ли массив
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
print(count)