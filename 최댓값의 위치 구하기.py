def find_max_idx(a):
    n = len(a)
    idx = 0
    for i in range(1,n):
        if a[idx] < a[i]:
            idx = i
    return idx

list = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max_idx(list))