def solution(logs):
    answer = []
    dict_log = {} # 수험번호가 key
    dict_result = {}

    for log in logs:
        list_log = log.split(" ")
        dict_score = {}
        dict_score[list_log[1]] = list_log[2]

        if list_log[0] in dict_log:
            for one in dict_log[list_log[0]]:
                if one[0] == list_log[1]:
                    dict_log[list_log[0]].remove(one)
            dict_log[list_log[0]].append([list_log[1], list_log[2]])
        else:
            dict_log[list_log[0]] = [[list_log[1], list_log[2]]]
            dict_result[list_log[0]] = 0

    for person in dict_log.keys():
        dict_result[person] = len(dict_log[person])

    for one in dict_result.keys():
        if dict_result[one] < 5:
            dict_log.pop(one)

    for person in dict_log.keys():
        dict_log[person].sort()

    comparelist = []
    newlist = []
    for person in dict_log.keys(): #value 가 같은 키가 있는지 검사
        newlist.append(dict_log[person])
        comparelist.append(person)

    for i in range(len(newlist)-1):
        if newlist[i] == newlist[i+1]:
            print(newlist[i])
            answer.append(comparelist[i])
            answer.append(comparelist[i+1])
    answer = list(set(answer))

    answer.sort()
    if len(answer) == 0:
        answer.append("None")
    return answer
