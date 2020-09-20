import collections
def groupAnagrams(strs):

    # 1. O(n) 한 번 돌면서 원형을 정렬하지 말고 반환된 정렬한것으로 비교해서 그걸 키로 만들고 안에
    #   값으로 다 넣기
    # 2. 딕셔너리의 값들로 이차원 배열 만들어서 리턴하기 -> 96 ms 걸림
    # anagrams = {}
    # for s in strs:
    #     new = ''.join(sorted(s))
    #     if new not in anagrams.keys():
    #         anagrams[new] = []
    #     anagrams[new].append(s)

    # 더 간단한 풀이
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
