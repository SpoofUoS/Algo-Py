def sel_sort(a):
    for i in range(len(a)-1):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
                a[i], a[min_idx] = a[min_idx], a[i]
                
arr = [2, 4, 5, 1, 3]
sel_sort(arr)
print(arr)