def solution(n, customers):
    answer = 0
    people = len(customers) # 총 고객 명 수

    # 키오스크 사용 여부를 나타내는 배열  - 인덱스 번호가 키오스크 번호임
    l_kiosk = [ 0 for _ in range(n)]
    print(l_kiosk)

    for customer in customers:
        # 한 명의 고객에 대하여 매칭중 
        l_one = customer.split()
        print(l_one)

        if 0 in l_kiosk: #아직 안쓰는 키오스크가 있다면










    return answer #키오스크에 매칭된 고객 명 수 리턴 (최대값)


print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26",
"10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13",
"10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))
