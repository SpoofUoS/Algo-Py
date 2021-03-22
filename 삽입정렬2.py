def ins_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음 
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j] # 삽입할 공간이 생기도록 값을 오른쪽으로 한 칸 이동 
            j -= 1
            a[j + 1] = key

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)