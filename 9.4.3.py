def par():
    string = str(input("nn"))
    print("1",string)
    string = string.split()
    print("2",string)
    li = []
    print("3",li)
    for i in string:
        print("4",li)
        print("5",i)
        if i == "(":
            li.append(i)
            print("6",li)
        elif i == ")":
            if len(li) > 0 and li[-1] == "(":
                li.pop()
            else:
                return False
            print("7",li)
    return len(li) == 0


print("8",par())