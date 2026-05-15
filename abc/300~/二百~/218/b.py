p=list(map(int,input().split()))

dic={}
for i in range(97, 123):
    dic[i-96]=chr(i)

ans=""
for i in p:
    ans+=dic[i]
print(ans)