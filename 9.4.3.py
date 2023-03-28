def par():
    string = str(input("nn"))
    print(string)
    string = string.split()
    print(string)
    li = []
    print(li)
    for i in string:
        print(li)
        print(i)
        if i == "(":
            li.append(i)
            print(li)
        elif i == ")":
            if len(li) > 0 and li[-1] == "(":
                li.pop()
            else:
                return False
            print(li)
    return len(li) == 0


print(par())