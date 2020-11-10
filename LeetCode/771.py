def numJewelsInStones(J: str, S: str) -> int:
     # S를 딕셔너리로 만들기 , 각각 키마다 몇개 있는지
     # J를 키로하는 각 개수를 더한다
     dict_S = {}
     for c in S:
         if c not in dict_S:
             dict_S[c] = 1
         else:
             dict_S[c] += 1

     sum = 0
     for c in J:
         if c not in dict_S:
             continue
         else:
             sum += dict_S[c]
     return sum

print(numJewelsInStones("aA", "aAAbbbb"))
