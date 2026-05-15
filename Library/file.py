import os
import shutil

# 元のディレクトリ（ファイルがある場所）
src_dir = "/Users/sudamiyukimakoto/Desktop/プロジェクト 2-春 (atcoder)"
# 移動先ディレクトリ
dst_dir = "/Users/sudamiyukimakoto/Desktop/プロジェクト 2-春 (atcoder)/四百~"

# 移動先ディレクトリがなければ作成
os.makedirs(dst_dir, exist_ok=True)

# 先頭が3のファイルをすべて移動
for filename in os.listdir(src_dir):
    if filename.startswith("4"):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)
        shutil.move(src_path, dst_path)

print("移動完了！")
