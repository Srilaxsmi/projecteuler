N = 600851475143
for i in range(2,N):
    while N % i == 0:
        N = N/i
    if i > N:
        print(i)
        break


