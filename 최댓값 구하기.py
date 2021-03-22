def find_max(a):  # 입력: 숫자가 n개 들어있는 리스트
    n = len(a)
    max = a[0]
    for i in range(1,n):
        if a[i] > max:
            max = a[i]
    return max
    
list = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max(list))