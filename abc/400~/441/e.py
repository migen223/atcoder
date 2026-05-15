
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

    def print(self):
        print(self.bit)

n=int(input())
s=input()
ab=[0]
ans=0
for i in range(n):
    if s[i]=="A":
        ab.append(ab[-1]+1)
    elif s[i]=="B":
        ab.append(ab[-1]-1)
    else:
        ab.append(ab[-1])
minus=abs(min(ab))
ab=[ab[i]+minus for i in range(len(ab))]
bit=BIT(max(ab)+1)
for i in range(len(ab)):
    bit.add(ab[i]+1,1)
    ans+=bit.sum(ab[i])

#bit.print()
print(ans)

