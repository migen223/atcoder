#edgeは(頂点,頂点、重さ)の形式の辺が格納されてるリスト、nodesは頂点数
#O(頂点数^3)
def WF(edge,nodes):
    res=[[10**32]*nodes for i in range(nodes)]
    for i in range(nodes):
        res[i][i]=0
    for u,v,w in edge:
        res[u][v]=min(res[u][v],w)
        res[v][u]=min(res[v][u],w)
    for k in range(nodes):
        for i in range(nodes):
            for j in range(nodes):
                res[i][j]=min(res[i][j],res[i][k]+res[k][j])
    
    return res
