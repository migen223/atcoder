s=list(input())
t=list(input())
x=[]
diff=[]
for i in range(len(s)):
    if s[i]!=t[i]:
        diff.append(i)

print(len(diff))
while diff:

    words=[]
    ind=[]
    for j in range(len(diff)):
        word=s[:diff[j]]+[t[diff[j]]]+s[diff[j]+1:]
        #print(nows,j)
        #print(small)
        words.append(word)
        ind.append(diff[j])
    
    #print(words)
    #print(small)
    #print(words)
    next=min(words)
    s=next
    print("".join(next))
    diff.remove(ind[words.index(next)])
    
    

