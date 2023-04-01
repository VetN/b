# двоичный поиск
def binary_search(array, element, left, right):
    # если левая граница выше правой, значит эл-т отсут
    if left > right:
        return False

    middle = (right + left) // 2  # находим середину
    # если эл-т в середине, возвр этот индекс
    if array[middle] == element:
        return middle
    # если эл-т меньше эл-та в середине,
    # рекурсивно ищем в левой половине
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)

element = int(input("введите element:"))
array = [i for i in range(1, 100)]

print("ответ:", binary_search(array, element, 0,99))