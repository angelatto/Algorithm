import re
import collections
def mostCommonWord(paragraph, banned):
    # paragraph를 처리하고나서 가장 많이 나오는 거 찾기

    newpara = [ p for p in re.sub('[^\w]',' ', paragraph).lower().split()
                    if p not in banned]
    counts = collections.Counter(newpara)
    print(counts)
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit."
,["hit"]))
