# 리스트에서 r에서 v가 들어가야할 위치를 알려주는 함수
def find_ins_idx(r, v):
    for i in range(len(r)): # 앞에서부터 확인하여
        if v < r[i]:        # v 값이 i 값보다 크면
            return i        # v 가 i 바로 앞에 놓어야 정렬 순서가 유지된다.
    return len(r)           # 적절한 자료가 없으면 맨 뒤에 삽입한다.

def ins_sort(a):
    result = []
    while a:  # 모두 추출하여 a가 []가 되면 false가 되어 while이 종료된다.
        value = a.pop(0)                          # a에서 하나를 꺼내 
        ins_idx = find_ins_idx(result, value)     # 적당한 위치를 찾아
        result.insert(ins_idx, value)             # 해당 위치에 넣는다.
    return result

d = [2, 4, 5, 1, 3]
print(ins_sort(d))