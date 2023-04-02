
# факториал 100
f = int(input("число"))
count = 0
factorial = 1
a = 2
while a != f + 1:
    factorial *= a
    count += 1
    a += 1

print(factorial)
print(count)
print(len(str(factorial)))