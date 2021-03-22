def quick_sort(a, start, end): # 범위를 지정하여 정렬하는 재귀 호출 함수
    if end - start <= 0: # 종료 조건
        return
    
    pivot = a[end] #
    i = start
    
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    
    a[i], a[end] = a[end], a[i]
    
    quick_sort(a, start, i - 1)
    quick_sort(a, i + 1, end)

def q_sort(a):
    quick_sort(a, 0, len(a) - 1)

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
q_sort(d)
print(d)