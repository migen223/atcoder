
n=int(input())
# 1 以上 N 以下の整数が素数かどうかを返す
def Eratosthenes(N):
    # テーブル
    isprime = [True] * (N+1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか
    return isprime

p=[]
era=Eratosthenes(2*10**6+2)
for i in range(len(era)):
    if era[i]:
        p.append(i)

ans=0
for i in range(len(p)-1):
    if p[i]**2>n:
        break
    for j in range(i+1,len(p)):
        if (p[i]**2)*(p[j]**2)>n:
            break
        else:
            ans+=1
            #print(p[i],p[j])

for i in range(len(p)):
    if p[i]**8>n:
        break
    else:
        ans+=1
print(ans)



