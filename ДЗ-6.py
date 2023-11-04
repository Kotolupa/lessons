a=int(input("Введіть а: "))
b=int(input("Введіть b: "))
c=int(input("Введіть с: "))
if a>c and a>b:
    if b>c:
        print(b)
    else:
        print(c)
elif b>a and b>c:
    if a>c:
        print(a)
    else:
        print(c)
elif a>b:
        print(a)
else:
        print(b)