class DualSegTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n *= 2

        # 遅延値のみ保持
        self.lazy = [0] * (2 * self.n)

    def apply(self, l, r, x):
        l += self.n
        r += self.n

        while l < r:
            if l & 1:
                self.lazy[l] = max(self.lazy[l], x)
                l += 1

            if r & 1:
                r -= 1
                self.lazy[r] = max(self.lazy[r], x)

            l //= 2
            r //= 2

    def get(self, p):
        p += self.n

        res = 0

        while p:
            res = max(res, self.lazy[p])
            p //= 2

        return res

n,d=map(int,input().split())
a=list(map(int,input().split()))

ma=max(a)
dst=DualSegTree(ma+1)

def out():
    for i in range(ma+1):
        print(dst.get(i),end=" ")
    print()

ans=-1
for i in range(n-1,-1,-1):
    now=dst.get(a[i])
    #print(max(0,a[i]-d),min(ma+1,a[i]+d+1),now+1)
    dst.apply(max(0,a[i]-d),min(ma+1,a[i]+d+1),now+1)
    ans=max(ans,now+1)
    #out()
print(ans)