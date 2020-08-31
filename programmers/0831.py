def solution(numbers, hand):
    answer = ''

    lpos = [3,0]
    rpos = [3,2]
#첫 번쨰로, 해당 숫자의 위치 찾아내기
    for i in numbers:
        #x랑 y는 해당 숫자의 폰에서의 위치 표현
        if i == 0:
            x,y = 3,1
        else:
            x,y = (i-1)//3, (i-1)%3

#두 번째로, 그 위치와 lpos, rpos 간의 거리 구해서 둘중 작은거 택하기
        if i in [1,4,7]:
            answer += 'L'
            lpos[0], lpos[1] = x, y
        elif i in [3,6,9]:
            answer += 'R'
            rpos[0], rpos[1] = x, y
        else :
            lsize, rsize = abs(x - lpos[0]) + abs(y - lpos[1]), abs(x - rpos[0]) + abs(y - rpos[1])
            if lsize < rsize:
                    answer += 'L'
                    lpos[0], lpos[1] = x, y
            elif lsize > rsize:
                    answer += 'R'
                    rpos[0], rpos[1] = x, y
            else:  # 만약 거리가 같다면 hand 정보 참고
                    if hand == "right" :
                            answer += 'R'
                            rpos[0], rpos[1] = x, y
                    else:
                        answer += 'L'
                        lpos[0], lpos[1] = x, y
                    #세 번째로, 작은거 택하고 나서 현재 손 위치 바꾸기
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))

# 코드는 돌아가지만 시간이 많이 걸려서.. 성능이 매우 좋지 않은 코드라서 60점 맞음...-> 반복문 3개라서 그럼..
