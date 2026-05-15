n=list(input())

k=len(n)

"""
if k==4:
    n[-1]="0"
elif k==5:
    n[-1]="0"
    n[-2]=="0"
elif k==6:
    for i in range(3):
        n[-1-i]="0"
elif k==7:
    for i in range(4):
        n[-1-i]="0"
elif k==8:
    for i in range(5):
        n[-1-i]="0"
elif k==9:
    for i in range(6):
        n[-1-i]="0"
"""
if k>=4:
    for i in range(k-3):
        n[-1-i]="0"
print("".join(n))

#print(10**9-1)