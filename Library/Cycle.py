
n,m=map(int,input().split())

graph=[[] for i in range(n)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    #graph[v].append(u)

import sys
sys.setrecursionlimit(10**7)
#seen finish は要素数nのbool配列
#nvが今の位置 pv が前の位置
#cycleには始点から検出したサイクルまでの頂点が入ってる
def dfs(graph ,nv ,pv,seen ,finish):
    global cycle
    seen[nv]=True
    cycle.append(nv)
    for ne in graph[nv]:

        #有向グラフの時は消す
        if ne==pv:
            continue

        if finish[ne]:
            continue
        if seen[ne] and not finish[ne]:
            cycle.append(ne)
            return ne
        res=dfs(graph,ne,nv,seen,finish)
        if res is not False:
            return res
    
    finish[nv]=True
    cycle.pop()
    return False


seen=[False]*n
finish=[False]*n
cycle=[]
start=dfs(graph,0,-1,seen,finish)
ans=[]

if start is False:
    print(-1)
else:
    for i in range(len(cycle)):
        if cycle[i]==start:
            break
    #print(cycle,i)
    ans=cycle[i:len(cycle)-1]
    print(ans)

def find_cycle_iterative(n, graph, is_directed=False):
    seen = [False] * n
    finish = [False] * n
    # stackの中身: [現在の頂点, 親の頂点, 調べた辺の数]
    # stack自体が「今どこを歩いているか（パス）」になります
    stack = []
    
    # 非連結グラフも考慮して全頂点を確認
    for i in range(n):
        if seen[i]: continue
        
        stack.append([i, -1, 0])
        while stack:
            u, p, edge_idx = stack[-1]
            
            # 初めてこの頂点に到達したとき
            if edge_idx == 0:
                if seen[u]:
                    # 既に訪問済みかつ探索が終わっていないならサイクル発見
                    if not finish[u]:
                        # サイクル復元処理
                        cycle = []
                        found = False
                        for node, parent, _ in stack:
                            if node == u:
                                found = True
                            if found:
                                cycle.append(node)
                        return cycle # サイクルのリストを返して終了
                    
                    stack.pop()
                    continue
                seen[u] = True
            
            # 隣接辺を一つずつ調べる
            if edge_idx < len(graph[u]):
                v = graph[u][edge_idx]
                stack[-1][2] += 1 # 次のためにインデックスを進めておく
                
                # 無向グラフの場合、親への逆流を防ぐ
                if not is_directed and v == p:
                    continue
                
                stack.append([v, u, 0])
            else:
                # すべての隣接辺を調べ終えた（帰りがけ）
                finish[u] = True
                stack.pop()
                
    return None # サイクルがなかった場合