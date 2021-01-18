def solution(phone_book):
    phone_book.sort()

    if len(phone_book) == 1:
        return True

    # 사전순 정렬되어 있기 때문에 앞뒤만 비교해도 됨 -> O(N)
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True