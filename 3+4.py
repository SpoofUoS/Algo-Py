Q = int(input())
while Q > 0:
    x = int(input())
    if x&(-x) == x:
        print('1')
    else:
        print('0')
    Q -= 1