ans=[]
while True:
    a=int(input())
    ans.append(a)
    if a==0:
        break
for i in range(len(ans)):
    print(ans[-1-i])