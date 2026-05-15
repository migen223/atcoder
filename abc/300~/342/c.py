n=int(input())
s=list(input())
q=int(input())
dic={}
for i in range(97, 123):
    dic[chr(i)]=chr(i)

#print(dic)
for i in range(q):
    c,d=input().split()
    for ch in dic:
        if dic[ch]==c:
            dic[ch]=d
ans=""
for i in range(len(s)):
    ans+=dic[s[i]]
print(ans)

"""
laklimamriiamrmrllrmlrkramrjimrial
laklimamriiamrmrllrmlrkramrjimrial

"""