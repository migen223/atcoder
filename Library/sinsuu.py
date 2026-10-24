base10=12345678
format(base10,'b')
#２進数に変換 
n=32
format(base10, f"0{n}b")
bin(n)[2:]
#n桁の2進数に変換
print(int("111",2))
#2進数を10進数に変換

#(i>>j)&1 →j bit目がたっているかどうか
#i|(1<<j) →iのjbit目を立たせる