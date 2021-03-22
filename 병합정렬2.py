def merge_sort(a):
    n = len(a)
    
    if n <= 1:
        return
    
    mid = n // 2
    left = a[:mid]
    right = a[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    i1 = 0
    i2 = 0
    ia = 0
    
    while i1 < len(left) and i2 < len(right):
        if left[i1] < right[i2]:
            a[ia] = left[i1]
            i1 += 1
            ia += 1
        else:
            a[ia] = right[i2]
            i2 += 1
            ia += 1
    
    # 남아 있는 자료들을 결과에 추가
    while i1 < len(left):
        a[ia] = left[i1]
        i1 += 1
        ia += 1
    while i2 < len(right):
        a[ia] = right[i2]
        i2 += 1
        ia += 1
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
merge_sort(d)
print(d)