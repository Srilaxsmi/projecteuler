import timeit

def lpf(N):
    while N % 2 == 0:
        N = N/2
    if 2 > N:
        return 2
    for i in range(3,N,2):
        while N % i == 0:
            N = N/i
        if i > N:
            return i

print(lpf(600851475143))
t = timeit.timeit(lambda: lpf(600851475143),number=1000)
print(t)
