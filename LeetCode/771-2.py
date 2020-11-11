import collections
def numJewelsInStones(J: str, S: str) -> int:
     dict_S = collections.defaultdict(int)
     for c in S:
         dict_S[c] += 1

     sum = 0
     for c in J:
         sum += dict_S[c]
     return sum

print(numJewelsInStones("aA", "aAAbbbb"))
