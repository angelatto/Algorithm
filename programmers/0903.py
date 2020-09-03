def solution(record):
    answer = []

    list_r = [r.split(' ') for r in record]
    dict_uid = {} # key: 유저 아이디 value : 닉 네임

    for i in range(len(list_r)):
        type = list_r[i][0]
        uid = list_r[i][1]
        if type == 'Enter':
            nick = list_r[i][2]
            dict_uid[uid] = nick

        elif type == 'Change':
            nick = list_r[i][2]
            dict_uid[uid] = nick

    for i in range(len(list_r)):
        type = list_r[i][0]
        uid = list_r[i][1]
        if type == 'Enter':
            answer.append(dict_uid[uid] + '님이 들어왔습니다.')
        if type == 'Leave':
            answer.append(dict_uid[uid] + '님이 나갔습니다.')


    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
