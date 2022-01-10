def solution(key, lock):
    answer, result = True, 1
    key90, key180, key270, data, now = [], [], [], [], []

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

            for _ in range((len(key)-1)*2+len(lock)):
                data0.append([0]*((len(key)-1)*2+len(lock)))
                data90.append([0]*((len(key)-1)*2+len(lock)))
                data180.append([0]*((len(key)-1)*2+len(lock)))
                data270.append([0]*((len(key)-1)*2+len(lock)))
                
            for x in range(len(lock)):
                for y in range(len(lock)):
                    data0[x+len(key)-1][y+len(key)-1] = lock[x][y]
                    data90[x+len(key)-1][y+len(key)-1] = lock[x][y]
                    data180[x+len(key)-1][y+len(key)-1] = lock[x][y]
                    data270[x+len(key)-1][y+len(key)-1] = lock[x][y]
            
            for x in range(len(key)):
                for y in range(len(key)):
                    if 0 <= x+i <= len(data)-1 and 0 <= y+j <= len(data)-1:
                        if key[x][y] == 1 and data[x+i][y+j] == 0:
                            data0[x+i][y+j] = 2
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
                    if data0[x+len(key)-1][y+len(key)-1] == 0:
                        result = 0
                    if data90[x+len(key)-1][y+len(key)-1] == 0:
                        result90 = 0
                    if data180[x+len(key)-1][y+len(key)-1] == 0:
                        result180 = 0
                    if data270[x+len(key)-1][y+len(key)-1] == 0:
                        result270 = 0
                        
            if result == 1 or result90 == 1 or result180 == 1 or result270 == 1:
                return answer
                    
    answer = False
    return answer
