sum = 0
a = b = 1
while b < 4000000:
    c = a+b
    a = b
    b = c
    if b%2 == 0:
        sum += b

print(sum)
