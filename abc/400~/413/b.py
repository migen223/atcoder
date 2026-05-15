n=int(input())
string=[]
for i in range(n):
    s=input()
    string.append(s)
check=[]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        else:
            s=string[i]+string[j]
            if s in check:
                continue
            else:
                check.append(s)
print(len(check))
