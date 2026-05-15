from sortedcontainers import SortedList,SortedSet

S = SortedList([3, 1, 2, 1]) #O(nlogn)
S.add(4) #O(logN)
S.discard(3) #値を削除 O(logn)
S.pop(2) #O(logn)
S[1] #O(logN)
2 in S 
# O(logn)
len(S) #現在の要素数 O(1)
S.bisect_left(1)
S.bisect_right(1)
S.index(2)
#1 Sに2が現れる最初の位置を返す。ないとValueError
S.count(2)
#2 Sに含まれる要素の個数を返す
S.irange(0,2) #[1, 2] S に含まれる 0以上2以下（両端含む）の要素を列挙

