from itertools import product,permutations,combinations,accumulate
from bisect import *
from math import gcd,comb
from collections import deque
import heapq
import sys
#read 'num?数字を入力: ' && mkdir -p "./$num" && touch "./$num"/{a,b,c}.py
#数字を入力するとそのフォルダとa~c.pyを作ってくれる

#b,c=map(int,input().split())
 
#l=list(map(int,input().split()))

#sys.exit() プログラムを強制終了させる　下の文を読みたくない時に

s={1,2,3}
#セット　リストよりも高速に探せる
s.add(4)
if 4 in s:
    print("4が含まれます")
a="hello"
print(a[1:3])
#"el"  インデックスが１から(3-1)番目の文字を取り出す

#a~zまでのアルファベットをすべて表示
for i in range(97, 123):
    print(chr(i))
#A~Zまでのアルファベットをすべて表示
for i in range(65,91):
    print(chr(i))


a=a.replace("l","o")
print(a)
#heooo

print(int("111",2))
#２進数の111を10進数に変換して返す  7


a=[1,2,3,4,5,6,7]
a[1:4]#インデックスの1から3まで 　2,3,4
print(a[::-1])
print(list(reversed(a)))
#両方[7,6,5,4,3,2,1]   後ろから一個ずつABC出力
print(a[:3])#最初の３項を出力 [1,2,3]
print(a[:-3])#末尾の３項を除いて出力 [1,2,3,4]
print(a[3:])#最初の３項を除いて末尾まで出力 [4,5,6,7]
print(a[-3:])#末尾の３項を出力  [5,6,7]
for i in reversed(a):#返り値はイテレータ
    print(i)
# 7 6 5 4 3 2 1
a=[1,2,3,4,5,6]
print(a[-1:-5:-1])
#[6,5,4,3]  後ろから1番目から(5-1)番目まで１ずつ出力
print(a.index(3))
# 2 .index(n)　リストの中でnと初めて一致するインデックスを返す

if "abc" in "sabcde":
    print("含まれます")

for p in product("ab",repeat=3):
    print(list(p))
#[a,b],[a,b],[a,b]の３つの積を出力 ["a","a","a"],["a","a","b"]...
for p in product("abc",[1,2]):
    print(list(p))
#[a,b,c],[1,2]の積を出力 ["a",1],["a",2],["b,1"]...
#repeat=...を加えることでリストの重複組合せ（順序なし）を作れる
for c in combinations('abc',2):
    print(list(c))
#a,b,cのなかから順番を考えずに並び替えたものを列挙 [a,b],[a,c],[b,c]
for p in permutations("ABC",2):
    print(list(p))
#a,b,cの中から順番を間変えて並び替えたものを列挙 [a,b],[b,a],[a,c],[c,a]...

#itertoolsの返り値は全てイテレータであることに注意　リストとして使いたい時はlist()

ex=["a","b","c"]
print("".join(ex))
#exを""で囲まれた文字で区切って出力 abc　文字列にしか使えないことに注意
a="abcde"
print("-".join(a))
#a-b-c-d-e

a=[1,2,3,4]
b=[4,3,2,1]
print(list(zip(*[a,b]))) #zip(*)列ごとにまとめる 返り値はタプルのリスト
#2次元配列Sを右に９０度回転する関数
s=[a,b]
def right_rot90(S):
    return list(zip(*S[::-1]))
print(right_rot90(s))
print(right_rot90(right_rot90(s)))


print(gcd(36,12,24))
#引数の最大公約数を返す　12　計算量は２個のときはO(log(min(引数)))　３個以上の時はO(n*logM) n:要素数 M最大の数
print(comb(5,2)) #10 comb(n,k)n個のものからk個取り出す場合の数　計算量はO(K)ですむ
s="thankyou"
#文字列の末尾に指定した文字列があるかどうかを返す boolean
#startswithもある(先頭の文字列)
if s.endswith("you"):
    print("最後がyouで終わります")

an=deque([1,2,3,4,5,6,7])
an.append(8)  #末尾に追加 [1,2,3,4,5,6,7,8]
an.appendleft(0) #先頭に追加 [0,1,2,3,4,5,6,7,8]
an.pop() #末尾を削除 [0,1,2,3,4,5,6,7]
an.rotate(1) #末尾を先頭に　[7,1,2,3,4,5,6] 
an.rotate(-1)  #先頭を末尾に [1,2,3,4,5,6,7]
#全てO(1)でできる

#優先度付きキュー
#通常は最小の要素の操作　最大の要素を操作したいときは全ての要素に-をかける
#ほとんどの操作をO(logn)でできる
h=[] #heapq.heapify(list) でリストをheapqに変換(O(n))
heapq.heappush(h,4)
heapq.heappush(h,6)
heapq.heappush(h,3)
heapq.heappush(h,8) #hに第二引数を追加
heapq.heappop(h) #最小の要素を返し、削除 O(logn)

1 <<3
#1を左に３bitずらす　=8

#bit全探索 002 Encyclopedia
N=4 #全体の長さ
for i in range(1 << N): #0から2^Nまで
    Candidate = ""
    for j in reversed(range(N)):
        # iのjビット目が0なら"(", 1なら")"
        if (i & (1 << j)) == 0:
            Candidate += "("
        else:
            Candidate += ")"

#二分探索
a = [1, 3, 3, 5, 7]
print(bisect_left(a, 3))   # 1 ３以上の最小のインデックスを返す　（挿入する位置）
print(bisect_right(a, 3))  # 3 3より大きい最小のインデックスを返す
print(bisect_left(a, 4))   # 3
print(bisect_right(a, 4))  #3
#bisect(list,value,lo=start,hi=end)
#listの中からインデックスがstartからend未満の範囲でのリストのにぶたん

#深さ優先探索
graph=[[1],[0,2],[1]]#隣接リスト表現

def dfs(at,p,d,dist):#at:現在地 p:前にいた位置 d:現在の深さ dist:各ノードの深さのリスト
    dist[at]=d
    for to in graph[at]:
        if to!=p:
            dfs(to,at,d+1,dist)
dist=[-1]*3
dfs(0,-1,0,dist)
print(dist) #[0,1,2]


"""

if <数値> in <list or set>:
リスト(セット)に数値があるかどうか　セットはリストより早い！
セットにリストを入れたいときはtupleにして入れる
t_set = set(tuple(x) for x in t)
if tuple(s[j]) not in t_set:

計算量は10^8以内にしたい！
max(l)
l内の最大値を返す

from fractions import Fraction
分数を扱える
x=Fraction(1,3) #=1/3

.pop(n)
インデックスnの値を返し、その値を削除 O(n) 
末尾を取り出したい場合は.pop()か.pop(-1)で行うことでO(1)で実行できる
.remove(m)
リスト内にmがあればその１つ目を削除　ないとエラーななるので注意
.sort()
昇順に並べる(小さい方から)降順にしたいときはreverse=True
math.floor()
math.ceil()
切り下げ、切り上げ
pow(a,n,j)->a^n%j   計算量O(logn)

木、森の性質
木->辺の数:頂点の数-1
森->辺の数:頂点の数-(連結成分の個数)
"""