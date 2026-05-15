s=input()
l=[]
push=[]
for a in s:
    l.append(int(a))
#print(l)
for i in range(len(s)-1):
    if l[i]<l[i+1]:
        push.append(10+l[i]-l[i+1])
    else:
        push.append(abs(l[i]-l[i+1]))
#print(push)
#print(t)
print(sum(push)+len(push)+1+int(s[-1]))








