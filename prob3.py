def lpf(N):
    for i in range(2,N):
        while N % i == 0:
            N = N/i
        if i > N:
            return i

print(lpf(600851475143))