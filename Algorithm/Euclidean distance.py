#유클리드 거리
#유클리드 거리를 토대로 값들간의 유사도를 구할 수 있어서 유클리디안 거리로 유사도를 측정하는 방식을
#유클리디안 유사도(Euclidean Similarity)라고도 한다.

#피타고라스 정리  c**2=a**2 + b**2 를 응용한 것
#피타고라스 정리는 이미 만들어진 삼각형을 쓴다면, 유클리드 거리는 삼각형을 만들어서 쓴다고 보면 된다.

# https://needjarvis.tistory.com/454 참조
# https://blog.naver.com/pjt3591oo/221913081091 참조

#문제
#BTS의 평점과 가장 비슷한 그룹은?

#=========================================
#풀이1- numpy 이용
import numpy as np

critics = {
    'BTS': {'암수살인': 5, '바울': 4, '할로윈': 1.5},
    '손흥민': {'바울': 5, '할로윈': 2},
    '레드벨벳': {'암수살인': 2.5, '할로윈': 1},
    '트와이스': {'암수살인': 3.5, '바울': 4, '할로윈': 5}
}

def euclidean(x, y):
    return np.sqrt(np.sum(np.square(x - y)))
#유클리드 거리 공식을 미리 적용


standards = list(critics['BTS'])  # BTS가 평가한 영화 리스트 생성
for group in critics:
    x = []
    y = []  # 그룹마다의 평점 리스트 생성 위해 for문 밖이 아닌 안에서 리스트 선언
    if group == 'BTS':  # 기준인 BTS는 비교할 필요X
        pass
    else:
        for movie in standards:  # BTS가 평가한 영화
            if movie in critics[group]:  # BTS가 평가한 영화에 대한 평가가 존재하면
                x.append(critics['BTS'][movie])  # x리스트에 bts의 평점 추가
                y.append(critics[group][movie])  # y리스트에 다른 그룹의 평가 추가
            else:  # 다른 그룹이 BTS가 평가한 영화 보지 않았으면
                pass  # 그 영화는 비교군에서 뺌
        x_doc = np.array(x)
        y_doc = np.array(y)
        print(group, euclidean(x_doc, y_doc))

#==================================================================
# %% 풀이2 math 사용
#pow는 거듭제곱
import math
def euclidian(x, y):
    sum = 0
    movies = y.keys() #영화 제목만 추출한 리스트 생성
    for movie in movies: #영화 하나씩 비교
        sum += math.pow(x[movie] - y[movie], 2) #(x-y)^2 를 더한 sum값 생성
    result = math.sqrt(sum) #루트씌움
    return result

print("손흥민: ", euclidian(critics['BTS'], critics['손흥민']))
print("레드벨벳: ", euclidian(critics['BTS'], critics['레드벨벳']))
print("트와이스: ", euclidian(critics['BTS'], critics['트와이스']))

#============================================================================
# %% 풀이3
# try-except 구문 사용
s = 0
for i in critics: # i는 그룹을 의미
    for j in critics['BTS'].keys(): #BTS가 평점을 준 영화 리스트 중
        try:
            a = (((float(critics[i][j]) - float(critics['BTS'][j])) ** 2)) #(다른그룹의 평점-BTS의 평점)^2
        except: #오류(다른 그룹에 값이 없음)일 경우
            continue #계속 진행
        s = s + a #sum값
    print(i, s ** 0.5) #그룹명과 유클리드 거리 출력



