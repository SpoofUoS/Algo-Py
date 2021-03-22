def bi_search(a, x, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return bi_search(a, x, mid + 1, end)
    else:
        return bi_search(a, x, start, mid -1)
    
    return -1

def binary_search(a, x):
    return bi_search(a, x, 0, len(a)-1)

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))