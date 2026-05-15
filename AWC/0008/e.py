#BIT(フェネック木)　1-indexに注意
#https://qiita.com/iorn121/items/d3c24c4d4b014531b782
class BIT:
    # 長さN+1の配列を初期化
    def __init__(self, N):
        self.size = N
        self.bit = [0]*(N+1)

    # i番目までの和を求める
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i] # フェニック木のi番目の値を加算
            i -= -i & i # 最も右にある1の桁を0にする
        return res

    # i番目の値にxを足して更新する
    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x # フェニック木のi番目にxを足して更新
            i += -i & i # 最も右にある1の桁に1を足す

n=int(input())
a=list(map(int,input().split()))
b=BIT(n)
ans=0
for i in range(n):
    b.add(a[i],1)
    ans+=b.sum(n)-b.sum(a[i])
print(ans)

