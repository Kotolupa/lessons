a=int(input("Введіть а: "))
b=int(input("Введіть b: "))
c=int(input("Введіть с: "))
if a>c and a<b:
    print(a)
elif b>a and b<c:
    print(b)
else:
    print(c)