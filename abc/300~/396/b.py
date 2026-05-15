q=int(input())
deck=[0]*100
for i in range(q):
    que=list(map(int,input().split()))
    if len(que)==2:
        deck.append(que[1])
    else:
        print(deck.pop())

