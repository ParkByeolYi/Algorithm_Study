def solution(key, lock):
    answer, result = True, 1
    data, now, key90, key180, key270  = [], [], [], [], []

    # lock의 주변을 len(key)-1로 확장시킨 2차원 리스트 0으로 생성
    for _ in range((len(key)-1)*2+len(lock)):
        data.append([0]*((len(key)-1)*2+len(lock)))
    
    for i in range(len(lock)):
        for j in range(len(lock)):
            data[i+len(key)-1][j+len(key)-1] = lock[i][j]
            
    for i in range(len(key)):
        # 90도 돌린 key
        for j in range(len(key)-1, -1, -1):
            now += [key[j][i]]
        key90 += [now]
        now = []
        
    for i in range(len(key)-1, -1, -1):
        # 180도 돌린 key
        for j in range(len(key)-1, -1, -1):
            now += [key[i][j]]
        key180 += [now]
        now = []
        
        # 270도 돌린 key
        for j in range(len(key)):
            now += [key[j][i]]
        key270 += [now]
        now = []
                    
    for i in range(len(data)):
        for j in range(len(data)):
            data0, data90, data180, data270 = [], [], [], []
            result, result90, result180, result270 = 1, 1, 1, 1
            
            # 회전한 key와 lock이 맞는지 확인할 2차원 리스트 0으로 생성
            for _ in range((len(key)-1)*2+len(lock)):
                data0.append([0]*((len(key)-1)*2+len(lock)))
                data90.append([0]*((len(key)-1)*2+len(lock)))
                data180.append([0]*((len(key)-1)*2+len(lock)))
                data270.append([0]*((len(key)-1)*2+len(lock)))
            
            # lock을 가운데에 삽입
            for x in range(len(lock)):
                for y in range(len(lock)):
                    data0[x+len(key)-1][y+len(key)-1] = lock[x][y]
                    data90[x+len(key)-1][y+len(key)-1] = lock[x][y]
                    data180[x+len(key)-1][y+len(key)-1] = lock[x][y]
                    data270[x+len(key)-1][y+len(key)-1] = lock[x][y]
            
            for x in range(len(key)):
                for y in range(len(key)):
                    # 범위 밖으로 벗어나면 안 됨
                    if 0 <= x+i <= len(data)-1 and 0 <= y+j <= len(data)-1:
                        # key와 lock이 맞으면 2
                        if key[x][y] == 1 and data[x+i][y+j] == 0:
                            data0[x+i][y+j] = 2
                        # key와 lock이 1이면 0으로 바꿔서 통과하지 못함
                        elif key[x][y] == 1 and data[x+i][y+j] == 1:
                            data0[x+i][y+j] = 0
                        
                        if key90[x][y] == 1 and data[x+i][y+j] == 0:
                            data90[x+i][y+j] = 2
                        elif key90[x][y] == 1 and data[x+i][y+j] == 1:
                            data90[x+i][y+j] = 0
                        
                        if key180[x][y] == 1 and data[x+i][y+j] == 0:
                            data180[x+i][y+j] = 2
                        elif key180[x][y] == 1 and data[x+i][y+j] == 1:
                            data180[x+i][y+j] = 0
                        
                        if key270[x][y] == 1 and data[x+i][y+j] == 0:
                            data270[x+i][y+j] = 2
                        elif key270[x][y] == 1 and data[x+i][y+j] == 1:
                            data270[x+i][y+j] = 0
                            
            for x in range(len(lock)):
                for y in range(len(lock)):
                    # lock에 0이 있으면 탈락
                    if data0[x+len(key)-1][y+len(key)-1] == 0:
                        result = 0
                    if data90[x+len(key)-1][y+len(key)-1] == 0:
                        result90 = 0
                    if data180[x+len(key)-1][y+len(key)-1] == 0:
                        result180 = 0
                    if data270[x+len(key)-1][y+len(key)-1] == 0:
                        result270 = 0
            
            # key와 lock이 맞으면 return True
            if result == 1 or result90 == 1 or result180 == 1 or result270 == 1:
                return answer
                    
    answer = False
    return answer
