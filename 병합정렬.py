def merge_sort(a):
    n = len(a)
    
    if n <= 1: # 자료가 1개 이하면 정렬할 필요가 없음
        return a
    
    mid = n // 2 # 중간을 기준으로 해서 반으로 나눔
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    
    result = [] # 최종 결과
    
    while left and right: # 두 집합에 자료가 남아있는 동안
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
            
    # 남아있는 자료들을 결과에 추가
    # 빈 집합은 지나감
    while left: result.append(left.pop(0))
    while right: result.append(right.pop(0))
    
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))