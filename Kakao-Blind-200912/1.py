def solution(new_id):
    answer = ''
    #1단계
    new_id = new_id.strip().lower()
    #2단계
    list_bad = list("~!@#$%^&*()=+[{]}:?,<>/")

    for s in new_id:
        if s not in list_bad and s != ' ':
            answer += s
    new_id = answer; answer = ''
    #3단계 : 연속된 .을 하나로 바꾼다
    if new_id != '':
        flag = True
        for s in new_id:
            if s == '.':
                flag = False
            else:
                if flag == False: answer += '.'
                answer += s
                flag = True
    new_id = answer;
    #4단계 양 쪽 둘다 .일때
    if new_id != '':
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[len(new_id)-1] == '.':
            new_id = new_id[:len(new_id)-1]
    #5단계
    if new_id == '': new_id += 'a'

    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[len(new_id)-1]  == '.':
        new_id = new_id[:len(new_id)-1]
    #7단계
    while len(new_id) < 3:
         new_id += new_id[len(new_id)-1]

    return new_id

print(solution("abcdefghijklmn  .p"))
