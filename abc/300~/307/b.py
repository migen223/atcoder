import sys
n=int(input())
ss=[input() for i in range(n)]

def check(s):
    for i in range(len(s)//2):
        if s[i]!=s[-1-i]:
            return False
    return True

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        now=ss[i]+ss[j]
        if check(now):
            print("Yes")
            #print(now)
            sys.exit()


print("No")