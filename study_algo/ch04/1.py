"""
< 선택 정렬 >
: 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복한다

- 선택정렬의 시간복잡도
선택 정렬은 N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다
𝑁 + (𝑁 - 1) + (𝑁 - 2) + ... + 2

이는 (𝑁² + 𝑁 - 2) / 2 로 표현할 수 있는데, 빅오 표기법에 따라서 O(N²) 이라고 작성한다

- 이미 정렬되어 있는 상태여도 n**2 만큼 반복을 할 까 ?? -> yes

"""

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)


