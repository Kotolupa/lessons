a=int(input("Введіть а: "))
b=int(input("Введіть b: "))
c=int(input("Введіть c: "))
if a>0 and b<=0 and c<=0:
    print("TRUE")
elif b>0 and a<=0 and c<=0:
    print("True")
elif c>0 and a<=0 and b<=0:
    print("TRUe")
else:
    print("False")