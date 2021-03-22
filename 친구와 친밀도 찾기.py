def print_all_friends(g, start):
    qu = []                               # 앞으로 처리해야 할 사람들을 큐에 저장
    done = set()                          # 이미 큐에 추가한 사람들을 집합에 기록(중복 방지)
    
    qu.append((start, 0))                 # 사람들의 정보를 하나의 튜플로 묶어 처리, 자기 자신의 친밀도: 0
    done.add(start)                       # 집합에도 추가
    
    while qu:                             # 큐에 처리할 사람들이 남아 있는 동안
        (p, d) = qu.pop(0)                # 큐에서 정보를 p와 d로 각각 꺼냄
        print(p, d)                       # 사람 이름과 친밀도를 출력
        for x in g[p]:                    # 친구들 중에
            if x not in done:             # 아직 큐에 추가된 없는 사람을
                qu.append((x, d + 1))     # 친밀도를 1 증가시겨 큐에 추가하고
                done.add(x)               # 집합에도 추가

friend_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(friend_info, 'Summer')
print()
print_all_friends(friend_info, 'Jerry')