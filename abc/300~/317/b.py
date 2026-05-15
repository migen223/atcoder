n=int(input())
a=list(map(int,input().split()))

for i in range(min(a),max(a)+1):
    if i not in a:
        print(i)
        break