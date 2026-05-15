
s=input()
dic={0:0,1:1,6:9,9:6,8:8,9:6}

ans=""
for i in range(len(s)):
    ans+=str(dic[int(s[-1-i])])
print(str(ans))