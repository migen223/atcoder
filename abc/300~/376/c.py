import sys
n=int(input())
a=list(map(int,input().split()))#おもちゃ
b=list(map(int,input().split()))#はこ
a.sort(reverse=True)
b.sort(reverse=True)
offset=0
offsind=0
boxind=0
for i in range(n-1):
    if b[boxind]>=a[i]:
        boxind+=1
    else:
        offset+=1
        offsind=i
        if offset>=2:
            print(-1)
            sys.exit()
if offset==1:
    if b[n-2]<a[n-1]:
        print(-1)
    else:
        print(a[offsind])
else:
    print(a[-1])

