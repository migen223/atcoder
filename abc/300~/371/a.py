
sa,sb,sc=input().split()

a=0
b=0
c=0
if sa=="<" and sb=="<":
    if sc=="<":
        print("B")
    else:
        print("C")
elif sa=="<" and sb==">":
    print("A")
elif sa==">" and sb=="<":
    print("A")
else:
    if sc=="<":
        print("C")
    else:
        print("B")