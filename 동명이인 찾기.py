def find_same_name(a):
    n = len(a)
    result = set()                      #결과를 저장할 빈 집합
    for i in range(0, n-1):             #이미 비교를 완료했기 때문에 마지막 부분은 제외
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

names = ['Tom', 'Jerry', 'Mike', 'Tom']
print(find_same_name(names))