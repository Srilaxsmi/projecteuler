sum = 0
a = b = 1
while b < 4000000:
    b = a+b
    a = b-a
    if b%2 == 0:
        sum += b

print(sum)
