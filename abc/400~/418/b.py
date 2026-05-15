s=input()
max=-1
for i in range(len(s)-1):
    if s[i]!="t":
        continue
    first=i
    x=1
    for j in range(first+1,len(s)):
        if s[j]=="t":
            x+=1
            tn=j-first+1
            if tn>=3 and max<(x-2)/(tn-2):
                max=(x-2)/(tn-2)
if max==-1:
    print(0)
else:
    print(max)



        


