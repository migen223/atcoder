n=1
l = 0
res = 0  # or 答え
for r in range(n):
    # 右を伸ばす

    while (True):
        # 左を縮める
        l += 1

    res += (r - l + 1)  # 個数数える系