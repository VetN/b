def find(array, element):
    for i, a in enumerate(array):
        if a == element:
            return i
    return False

def count(array, a):
    count = 0
    for b in array:
        if b == a:
            count += 1
    return count


array = list(map(int, input("введите числа").split()))
print(find(array, 4))
print(count(array, 4))