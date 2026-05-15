n=int(input())
user=set()
for i in range(1,n+1):
    name=input()
    if name not in user:
        user.add(name)
        print(i)