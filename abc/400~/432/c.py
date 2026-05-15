import sys
n,x,y=map(int,input().split())

a=list(map(int,input().split()))

xy=x-y
diff=[]
for i in range(n-1):
    if (y*(a[i]-a[i+1]))%xy==0:
        diff.append((y*(a[i]-a[i+1]))//xy)
    else:
        print(-1)
        sys.exit()

#print(diff)
ruiseki=[diff[0]]
for i in range(1,len(diff)):
    ruiseki.append(ruiseki[-1]+diff[i])

for i in range(n-1):
    if ruiseki[i]>a[i+1]:
        print(-1)
        sys.exit()

mi=min(0,min(ruiseki))

ans=a[0]-abs(mi)
now=abs(mi)
#print(now)
for i in range(1,n):
    now+=diff[i-1]
    ans+=a[i]-now

    #if now>a[i]:
     #   print(-1)
      #  sys.exit()
    print(f"now={now}")
print(diff)
#print(ruiseki)


print(ans)




"""
import math
N, X, Y = map(int, input().split())
A = list(map(int,input().split()))
A = sorted(A,reverse=True)

g = math.gcd(X,Y)
X_n = X // g
Y_n = Y // g

m = A[len(A)-1] * Y

MAX = A[0]
MIN = 0
mid = (MIN + MAX) // 2

while MAX-MIN > 0:
    if mid * Y + (A[0]-mid) * X < m:
        MIN = mid+1
    else:
        MAX = mid
    
    mid = (MIN + MAX) // 2

ans = mid
b = mid
s = A[0]-mid

flag = True
for i in range(1,N):
    dif = abs(A[i] - A[i-1])
    b += (dif * X_n)
    s -= (dif * Y_n)
    if (s < 0):
        flag = False

    ans += b

if flag:
    print(ans)
else:
    print(-1)

"""