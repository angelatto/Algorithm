# print("Enter your name:")
# somebody = input()
# print("Hi", somebody, "How are you today?")

# temperature = float(input("온도를 입력하세요: "))
# print(temperature)

cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
print(cities[0:2]) #출력 : ['서울', '부산']
print(cities[0:7])
print(cities[7:])
print(cities[-8:-1])
print(cities[:-7])
print(cities[::2])
print(cities[::-1])
print(cities[::-2])

#리스트의 연산
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']
print(color1 + color2)
print(len(color1 + color2))
print(color1 * 2)
print('blue' in color1)

#리스트 추가 및 삭제
color1.append('white')
print(color1)

color1.append(color2)
print(color1)

color1.extend(color2)
print(color1)

color1.insert(1, 'purple')
print(color1)

color1.remove('red')
print(color1)

color1.remove(color1[0])
print(color1)

del color1[0]
print(color1)
