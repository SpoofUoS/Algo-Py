def quick_sort(a):
    n = len(a)
    
    if n <= 1:
        return a
    
    pivot = a[0] # 기준 값은 아무거나 해도 상관 없음
    left = []
    right = []
    
    for i in range(1, n): # 기준 값인 a[0]을 제외한 나머지 부분
        if a[i] < pivot:
            left.append(a[i])
        else:
            right.append(a[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))