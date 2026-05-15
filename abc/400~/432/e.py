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

n,q=map(int,input().split())
a=list(map(int,input().split()))
b1=BIT(5*10**5+2) #個数のBIT
b2=BIT(5*10**5+2) #値のBIT

for i in range(n):
    b1.add(a[i]+1,1)
    b2.add(a[i]+1,a[i])


for i in range(q):  
    que=list(map(int,input().split()))
    #print(que)
    if que[0]==1:
        x,y=que[1:]
        pre=a[x-1]
        b1.add(pre+1,-1)
        b2.add(pre+1,-pre)
        b1.add(y+1,1)
        b2.add(y+1,y)
        a[x-1]=y
    elif que[0]==2:
        l,r=que[1:]
        ans=0
        if l<r:
            fr=b1.sum(l+1-1)
            ba=b1.sum(5*10**5+1)-b1.sum(r+1)
            ans+=l*fr+r*ba
            ans+=b2.sum(r+1)-b2.sum(l+1-1)
            #print("fr",fr,"ba",ba,"mid",b2.sum(r+1)-b2.sum(l+1-1))
        else:
            ans+=l*n
        print(ans)
