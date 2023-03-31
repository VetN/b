class Node:
    '''создает элемент ы списка'''
    def __init__(self, value = None, next_ = None):
        self.value = value  # значение
        self. next = next_  # ссылка на след элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:
    '''реализует список'''
    # создаем пустой список
    def __init__(self):
        self.first = None
        self.last = None
    # очищаем список
    def clear(self):
        self.__init__()
    # функция печати
    def __str__(self):
        R = " "
        pointer = self.first  # берем первый указатель
        while pointer is not None:
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer. next  # идем дальше по указателю
            if pointer is not None:
                R += " "  # если указ сущ добавл пробел
        return R

    # добавляем новы элемент в начало списка (в левую часть)
    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    # добавляем элемент в конец списка (в правую часть)
    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    # удаление элемента
    # удаление из начала путем изменения указателя на первый элемент
    # удаление с конца нескольк способов
    # создание двусвязного списка или
    # модификация односвязного, сохраняя дополнительно указатель на предпоследний элемент
    def popleft(self):
        if self.first is None:
            return None
        elif self.first == self.last:
            node = self.first  # если есть только один элемент, то сохраняем его
            self.__init__()  # очищаем
            return node  # возращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next # меняем указатель на первый элемент
            return  node # возращаем сохраненный

    def popright(self):
        if self.first is None:
            return None
        elif self.first == self.last:
            node = self.first
            self.__init__()
            return node
        else:
            node = self.last  # сохраняем последний
            pointer = self.first  # создаем указатель
            while pointer.next is not node:  # пока не найдем последний указатель
                pointer = pointer.next
            pointer.next = None  # обнуляем указатели
            self.last = pointer  #чтобы предпоследний стал последним
            return node  #возвращаем сохраненный

    # добавили итератор
    def __iter__(self):
        self.current = self.first # в текущий элемент помещаем первый
        return self # возвращаем итератор

    # метод перехода
    def __next__(self):
        if self.current is None:
            # если текущ элемент стал последним, вызыв исключ
            raise StopIteration
        else:
            node = self.current  # сохраняем текущий элемент
            self.current = self.current.next # совершаем пенреход
            return node  #  возвращаем сохраненный

    # возвращаем размер структуры данных
    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next

        return count
LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
print(LL)
LL.pushright(3)
print(LL)
LL.popright()
print(LL)
LL.pushleft(4)
print(LL)
LL.pushright(5)
print(LL)
LL.popleft()

print(LL)
print(LL.__len__())