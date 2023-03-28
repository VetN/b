di = {'(': ')', '<': '>'}


def par(string):
    li = []
    for i in string:
        print("4", li)
        print("5", i)
        if i in ") >": # ищем значения и длобавляем в стек
            li.append(i)
            print("6", li)
        elif i in "( <" : 
            # если встретился ключ,смотрим есть ли в стеке что 
            # сравниваем это со значением 
            # и если ключ и значение подходят удаляем
            # если стек пустой true
            if len(li) > 0 and li[-1] == di[i]:
                li.pop()
            else:
                return False
        print("7", li)
    return len(li) == 0


print("11", par("()"))
print("12", par(")("))
print("13", par("()({)"))
print("14", par("()){("))
print("15", par("()({))("))
print("6", par("()<>"))
print("17", par("(<)>"))
print("18", par(")(><"))
print("19", par("<>"))
print("19.1", par("><"))
print("20", par("<.>"))