from bisect import *
n=int(input())
x=list(map(int,input().split()))
p=list(map(int,input().split()))
q=int(input())
ruiseki=[] #累積和のリスト
now=0
for i in p:
    now+=i
    ruiseki.append(now)

for _ in range(q):
    l,r=map(int,input().split())
    if r<x[0] or l>x[len(x)-1]: #範囲内に含まれる村がない場合0を出力し、次のクエリへ
        print(0)
        continue
#二分探索で村の開始位置と最終位置を特定
    l_ind=bisect_left(x,l)
    r_ind=bisect_right(x,r)-1 #最終位置より１つ大きい値が返されるので-1
    if l_ind==0: #開始位置が一つ目の村だった場合引く必要がなくなる
        print(ruiseki[r_ind])
    else:
        print(ruiseki[r_ind]-ruiseki[l_ind-1])


"""
a = [1, 3, 3, 5, 7]
print(bisect_left(a, 3))   # 1 ３以上の最小のインデックスを返す　（挿入する位置）
print(bisect_right(a, 3))  # 3 3より大きい最小のインデックスを返す
print(bisect_left(a, 4))   # 3
print(bisect_right(a, 4))  #3
"""