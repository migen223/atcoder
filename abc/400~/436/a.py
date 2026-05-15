from collections import deque
n=int(input())
s=deque(list(input()))
while len(s)<n:
    s.appendleft("o")
print("".join(list(s)))