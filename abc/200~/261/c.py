
n=int(input())
se=set()
dic={}
for i in range(n):
    s=input()
    #print(i)
    if s not in se:
        print(s)
        se.add(s)
        dic[s]=1
    else:
        print(f"{s}({dic[s]})")
        dic[s]+=1
    

