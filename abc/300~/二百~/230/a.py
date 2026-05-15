
n=int(input())
if n<10:
    print(f"AGC00{n}")
else:
    if n<42:
        print(f"AGC0{n}")
    else:
        print(f"AGC0{n+1}")