
s=list(input())
se=set()
for i in range(len(s)):
    for j in range(i,len(s)):
        st=tuple(s[i:j+1])
        se.add(st)

print(len(se))