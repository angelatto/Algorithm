# 비밀 지도 - 비트 연산을 묻는 문제
# 난이도 - 하

def solution(n, arr1, arr2):
    maps = []
    for i in range(n):
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
            .zfill(n)
            .replace('1', '#')
            .replace('0', ' ')
        )
    return maps

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))

# 파이썬 패딩 참고
print('-38'.zfill(5)) # -0038
print('-38'.rjust(5, '0')) # 00-38
print('38'.ljust(5, '0')) # 38000
