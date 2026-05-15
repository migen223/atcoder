n=int(input())
s=list(input())
done=set()
now=[s[0],1]
done.add((s[0],1))
for i in range(1,n):
    if s[i]==now[0]:
        now[1]+=1
        done.add((now[0],now[1]))
    else:
        now[0]=s[i]
        now[1]=1
        done.add((now[0],now[1]))
print(len(done))