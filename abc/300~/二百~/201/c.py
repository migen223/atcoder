
s=input()

def tostr(n):
    s=str(n)
    ans=""
    for i in range(4-len(s)):
        ans+="0"
    ans+=s
    return ans

ose=set()
qse=set()
xse=set()
for i in range(10):
    if s[i]=="o":
        ose.add(str(i))
    elif s[i]=="?":
        qse.add(str(i))
    else:
        xse.add(str(i))

#print(ose)
#print(xse)


ans=0
for i in range(10000):
    st=tostr(i)
    se=set(list(st))
    #print(se)
    #print(ose-se)
    #print(se&xse)
    if len(ose-se)==0 and len(se&xse)==0:
        ans+=1
print(ans)


