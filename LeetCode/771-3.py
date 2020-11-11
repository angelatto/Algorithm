import collections
def numJewelsInStones(J: str, S: str) -> int:
     dict_S = collections.Counter(S)
     print(dict_S)

     sum = 0
     for c in J:
         sum += dict_S[c] 
     return sum

print(numJewelsInStones("aA", "aAAbbbb"))
