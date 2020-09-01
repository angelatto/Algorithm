import sys

height = sys.stdin.readline()

list_h = height.strip().split()
print("dddd", list_h)
print("dd", sorted(list_h))
#print(list_h.sort()) #아...원본 리스트를 정렬 -> 반환값은 None

if list_h != sorted(list_h):
    print("No")
else:
    print("Yes")

# 176 156 155 165 166 169
