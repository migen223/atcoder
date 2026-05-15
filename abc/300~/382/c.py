"""
from bisect import bisect_left
n,m=map(int,input().split())
people=list(map(int,input().split()))
sushi=list(map(int,input().split()))

for i in range(1,n):
    people[i]=min(people[i],people[i-1])
for i in range(n):
    people[i]*=-1
for i in range(m):
    
    if bisect_left(people,-sushi[i])==n:
        print(-1)
    else:
        print(bisect_left(people,-sushi[i])+1)
        """

import sys
input = sys.stdin.readline

K = 200010

def main():
    n, m = map(int, input().split())
    id = [-1] * K
    r = K
    for i in range(n):
        a = int(input())
        while r > a:
            r -= 1
            id[r] = i + 1
    for _ in range(m):
        b = int(input())
        print(id[b])

if __name__ == "__main__":
    main()
