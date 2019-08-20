def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print(sum(5))   # 5+4+3+2+1+0



