n,m=map(int,input().split())
s=list(input())
normal=m
logo=0

shirts=[]
logos=[]
count=0

for i in range(n):
    if s[i]=="1":
        count+=1
    elif s[i]=="2":
        logo+=1
        count+=1
    else:
        shirts.append(count)
        logos.append(logo)
        logo=0
        count=0
shirts.append(count)
logos.append(logo)
print(max(max(shirts)-m,max(logos)))