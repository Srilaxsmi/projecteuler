from itertools import count 

def primes():
    D = {4:[2]}
    yield 2
    for i in count(3):
        if i in D:
            for j in D[i]:
                D.setdefault(i+j,[]).append(j)
            D.pop(i)
        else:
            D[i+i] = [i]
            yield i

for i,p in enumerate(primes()):
    if i == 10000:
        print(p)
        break
