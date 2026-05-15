MOD = 10**9 + 7

L, R = map(int, input().split())
ans = 0

for d in range(1, 20):  # 桁数1～19まで（10^18まで対応）
    l = max(L, 10**(d - 1))
    r = min(R, 10**d - 1)
    if l > r:
        continue
    count = r - l + 1
    total = (count * (l + r) // 2) % MOD  # Σx
    ans = (ans + total * d) % MOD         # 桁数d倍して加算

print(ans)
