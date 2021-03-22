def find_same_name(a): # a: 리스트
    name_dict = {}
    
    for name in a:                  # 리스트 a에 있는 이름들을 차례로 반복
        if name in name_dict:       # 이름이 name_dict에 있으면 
            name_dict[name] += 1    # 등장 횟수를 1 증가
        else:                       # 새 이름이면
            name_dict[name] = 1     # 등장 횟수를 1로 저장
        
    result = set()  # 결과 값을 저장할 새 집합 
    
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    
    return result

name = ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))