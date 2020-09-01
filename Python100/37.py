names = input().strip().split()

dict_name = {}
for n in names:
    dict_name[n] = names.count(n)

for n in dict_name.keys():
    print("{}이가 총 {}표로 반장이 되었습니다.".format(n, dict_name[n]))
