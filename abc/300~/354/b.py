n=int(input())
user=[]
rate=[]

for i in range(n):
    s,c=input().split()
    c=int(c)
    user.append(s)
    rate.append(c)

user.sort()
s=sum(rate)
print(user[s%n])
