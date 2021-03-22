def find_min_idx(a):
    min_idx = 0
    for i in range(1,len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []
    while a: # a가 전부 추출되어 []가 되면 false로 while문이 종료된다.
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

arr = [2, 4, 5, 1, 3]
print(sel_sort(arr))