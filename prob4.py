def isPalin(N):
    a = N
    b = 0
    while a > 0:
        b = (10 * b) + (a % 10)
        a = int (a / 10)
    return N == b

m = 0       
for i in range(999,99,-1):
    for j in range(i,99,-1):
        c = i * j
        if isPalin(c):
            if c > m:
                m = c
            break
        if c < m:
            break

print(m)