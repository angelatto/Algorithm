 # 한국의 면적과 가장 비슷한 국가와 그 차이를 출력
 # 그차이 절댓값이 최소인 국가를 찾기
def solution(nationWidth):
     # 딕셔너리를 처리
     korea = nationWidth["korea"]
     for nation in nationWidth:
         nationWidth[nation] = nationWidth[nation]-korea
         if nationWidth[nation] < 0:
             nationWidth[nation] = nationWidth[nation] * (-1)
     nationWidth.pop("korea")

     nationList = []
     result = min(nationWidth.values())
     for nation in nationWidth:
         if nationWidth[nation] == result:
             nationList.append(nation)

     return nationList, result

nationWidth = { 'korea': 220877,'Rusia': 17098242,'China': 9596961,'France': 543965,'Japan': 377915,'England' : 242900 }
print(solution(nationWidth))
