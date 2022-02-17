#유클리드 거리
#유클리드 거리를 토대로 값들간의 유사도를 구할 수 있어서 유클리디안 거리로 유사도를 측정하는 방식을
#유클리디안 유사도(Euclidean Similarity)라고도 한다.

#피타고라스 정리  c**2=a**2 + b**2 를 응용한 것
#피타고라스 정리는 이미 만들어진 삼각형을 쓴다면, 유클리드 거리는 삼각형을 만들어서 쓴다고 보면 된다.

# https://needjarvis.tistory.com/454 참조
# https://blog.naver.com/pjt3591oo/221913081091 참조

#if titanic dataset
#나이, 운임, 선실등급, 성별...생존
#(10,100,2,1)
#(50,1000,1,2)
#...
#결과에 가장 큰 영향을 주는 것->선실등급?--> 각 데이터의 범위가 다르므로 표준화 작업 필요
#

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

#개선점: BTS가 보지 않은 영화를 다른 그룹이 봤다면 error발생
#for문을 사용해 print를 하는게 좋을 듯
import math
def eucldis(critics, group1, group2):
    s=0
    for i in critics[group1]:
        if i in critics[group2]:
            s+=pow(critics[group1][i]-critics[group2][i],2)
        else:
            pass
    return math.sqrt(s)

print(eucldis(critics,'BTS','손흥민')) #1.118033988749895
print(eucldis(critics,'BTS','레드벨벳')) #3.24037034920393
print(eucldis(critics,'BTS','트와이스')) #3.8078865529319543

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



#다음과 같은 데이터셋에서
data=[['A', '5', '4', '', '3.5', '4.5'],
 ['B', '', '2', '5', '4', ''],
 ['C', '2.5', '3', '3', '3', ''],
 ['D', '4', '3', '4', '4', '4'],
 ['E', '3', '3.5', '', '4', '3.5'],
 ['F', '4', '3', '4', '3', '2'],
 ['G', '5', '4', '', '', ''],
 ['H', '5', '5', '4', '5', '4'],
 ['I', '3', '3', '4', '4', '2'],
 ['J', '', '2', '4', '2', ''],
 ['H', '5', '3', '3', '2', '']]


def euclidean(data,standard):
    distance=[]
    for user in data:
        if standard in user:
            idx=data.index(user) #기준 유저의 인덱스 저장
    for i in range(len(data)):#다른 유저들과 비교 위한 for문
        sum=0 #유저마다 거리 출력 필요하므로 for문 안에 sum 변수 선언
        for j in range(1,len(data[i])): #range1로 시작해 점수만 확인
            if data[i][j] !='' and data[idx][j] !='': #둘다 영화 봤을때
                sum+=(float(data[i][j])-float(data[idx][j]))**2
            else:
                pass
        distance.append(np.sqrt(sum))
    return distance

#1. C와 가장 다른 취향의 유저 찾기
def different_taste(user): #나와 가장 다른취향을 가진 유저 찾는 함수 정의
    lst=euclidean(data,user) #거리 리스트 중
    far=max(lst)#제일먼거리
    different_taste=lst.index(far) #제일 먼거리의 인덱스 기억
    print(data[different_taste][0],far)#유저이름, 거리 출력
different_taste('C')


#2. C와 가장 비슷한 취향의 유저 찾기
def second_min(lst): #두번째로 작은 값 구하는 함수 정의
    __lst=sorted(lst)
    return(__lst[1])
def similar_taste(user): #나와 가장 비슷한 취향을 가진 유저 찾는 함수 정의
    lst=euclidean(data,user) #거리 리스트 중
    close=second_min(lst) #두번째로 먼 거리(가장 가까운건 나 자신)
    similar_taste=lst.index(close)
    if data[similar_taste][0] != user: #나랑 취향 똑같은 사람 있을 수 있어 if문 사용
        return data[similar_taste][0]
    else:
        close=min(lst)
        similar_taste=lst.index(close)
        return data[similar_taste][0]
similar_taste('C')

#3. G에게 영화 추천하기

def recommend_movie(me):
    no_watching=[]
    movie_num={}
    similar_user=similar_taste(me) #제일비슷한 취향의 유저
    for user in data:
        if similar_user in user:
            idx=data.index(user)#같은취향 유저 인덱스
        elif me in user:
            my_idx=data.index(user)#내 인덱스
    for i in range(1,len(data[my_idx])):
        if data[my_idx][i] == '' and data[idx][i] != '': #난 안봤는데 같은취향 유저는 봤으면
            no_watching.append(data[idx][i]) #리스트에 일단 평점 추가
            movie_num[(data[idx][i])]=i #평점을 키로, 인덱스를 값으로 저장
    x=max(no_watching)
    return movie_num[x]

recommend_movie('G')

#값은 인덱스로 나와 영화 제목 리스트가 있으면 좋을 것 같음
movie=['영화1','영화2','영화3','영화4','영화5']
mv_n=recommend_movie('G')
movie[mv_n-1] #유저 이름때문에 -1해줌

#쓸데없이 복잡한 느낌이 든다...
#더 간단하게 로직을 짤 수 없을까? ㅜㅡㅜ
#


