
inFile = open('./data1.txt', 'r')
# s = inFile.readlines()
# print(s)

# while True:
#     s = inFile.readline()
#     if s == '':
#         break
#     print(s, end='')

s_list = inFile.readlines()
for i in range(len(s_list)):
    print(i+1, ":", s_list[i], end='')


inFile.close()