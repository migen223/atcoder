from itertools import *
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
#a,b,cの中から順番を考えて並び替えたものを列挙 [a,b],[b,a],[a,c],[c,a]...

#itertoolsの返り値は全てイテレータであることに注意　リストとして使いたい時はlist()