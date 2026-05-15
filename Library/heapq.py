import heapq
#優先度付きキュー
#通常は最小の要素の操作　最大の要素を操作したいときは全ての要素に-をかける
#ほとんどの操作をO(logn)でできる
h=[] #heapq.heapify(list) でリストをheapqに変換(O(n))
heapq.heappush(h,4)
heapq.heappush(h,6)
heapq.heappush(h,3)
heapq.heappush(h,8) #hに第二引数を追加
heapq.heappop(h) #最小の要素を返し、削除 O(logn)