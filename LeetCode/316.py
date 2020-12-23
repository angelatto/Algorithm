def removeDuplicateLetters(s: str) -> str:
    # 딕셔너리에 넣고 이미 있으면 리스트에 추가 안하는?

    new = []
    for char in s:
        if char not in new:
            new.append(char)

    new.sort()
    return ''.join(new)
print(removeDuplicateLetters("bcabc"))
