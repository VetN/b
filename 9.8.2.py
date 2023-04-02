# сортировка выбором отсортир слева и неотсортир справа.
# Ищется миним эл-т в неотсортиров части и меняется местами с эл-том в начале неотсортир части
# И так продолж, пока не закончит внешний цикл

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
count_1 = 0

for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс времен миним эл-та
    for j in range(i, len(array)):  # от i вправо
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальнм, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
print(count)
print(array)
print("**********")

# сортировка по убыванию
for a in range(len(array)):
    a_max = a
    for p in range(a, len(array)):
        count_1 += 1
        if array[p] > array[a_max]:
            a_max = p
    if a != a_max:
        array[a_max], array[a] = array[a], array[a_max]
print(count_1)
print(array)
print("**********")
# сортировка пузырьком
for s in range(len(array)):
     for l in range(len(array) - s-1):
         if array[l] > array[l+1]:
             array[l], array[l + 1] = array[l + 1], array[l]
print(array)
print("**********")
# cортировка вставками
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count_3 = 0
for m in range(1, len(array)):
    x = array[m]
    idx = m
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
        count_3 += 1
    array[idx] = x
print(array)
print(count_3)
print("**********")

# сортировка слиянием
def m_sort(L):
    if len(L) < 2:  # если кусок массива меньше 2
        return  L[:]  #  выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = m_sort(L[:middle])  # рекурсивно делим левую часть
        right = m_sort(L[middle:])  # правую
        return merge(left, right)  # слияние

def merge(left, right):
    result = []  # итоговый массив
    i, j = 0, 0  #  указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print(result)
    return result

L =  [2, 3, 1, 4, 6, 5, 9, 8, 7]
m_sort(L)
print("**********")
# быстрая сортировка


def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
            qsort(array, left, j)
    if right > i:
            qsort(array, i, right)




array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
L = [2, 3, 1, 4, 6, 5, 9, 8, 7]
