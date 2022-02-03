# import pandas as pd #데이터 분석 도구 판다스를 가져와 pd라는 이름으로 정의
# print(pd.read_csv('name/yob2010.txt', names= ['name','gender','births']))
# # 파일을 열 때 이름을 따로 지정하지 않으면 첫 번째 줄이 제목이 된다
# names2010=pd.read_csv('name/yob2010.txt', names= ['name','gender','births'])

# #2010년에 태어난 아이들의 수를 성별에 따라 출력
# #-->성별에 따른 그룹화
# print(names2010.groupby('gender').births.sum())
#
# #1880년부터 2010 에 태어난 아이들 데이터를 따로 변수로 저장해서 하기-->비효율적
# #names1880, names1881, ....names2010 매우 불편
#
# #for 문을 사용하여
# years=range(1880,2011)
# pieces=[]
# for year in years:
#     frame = pd.read_csv('name/yob%d.txt' %year, names= ['name','gender','births'])
#     frame['year'] = year
#     pieces.append(frame)
# #pd.concat #131개 데이터 프레임을 연결하여 1개의 데이터프레임으로 생성
# names=pd.concat(pieces, ignore_index=True) #기존 인덱스는 날아가고 새로운 인덱스 형성
# print(names)
#
# #피봇팅
# #연도별로 성별에 따라 태어난 아이들의 수를 출력하고 싶다
# #         F              M
# # 1880 태어난 아이수   태어난아이수
# #  ...
# # 2010
# #열인덱스: 연도 행인덱스:성별
#
# total_births = names.pivot_table('births', index='year',columns='gender',aggfunc=sum )
# print(total_births)
#
# print(names.groupby(['year','gender']).births.sum())
#
# def add_prop(group):
#     group['prop'] = group.births/group.births.sum() #해당 연도name에 속한 birth 값/해당 연도 여자아이(or 남자아이) 수 합계
#     return group
# names = names.groupby(['year', 'gender']).apply(add_prop)
#
# print(names)
# print(sum(names['prop']))
# #names의 prop열 값은 그룹별로(연도 및 성별에 따른 그룹) 합산했을 때 각각 1이 됨
#
# # # 연도별, 성별에 따른 태어난 아이 수의 변화를 꺾은선 그래프로 출력
# import pandas as pd
# years=range(1880,2011)
# pieces=[]
# for year in years:
#     frame = pd.read_csv('name/yob%d.txt' %year, names= ['name','gender','births'])
#     frame['year'] = year #year라는 열을 추가해주었다.
#     pieces.append(frame)
# #pd.concat #131개 데이터 프레임을 연결하여 1개의 데이터프레임으로 생성
# names=pd.concat(pieces, ignore_index=True) #기존 인덱스는 날아가고 새로운 인덱스 형성
# print(names)
#
# total_births=names.pivot_table('births', index='year', columns= 'gender', aggfunc = sum)
# print(total_births)
# import matplotlib.pyplot as plt
# total_births.plot()
# plt.show()
#
# def add_prop(group):
#     group['prop'] = group.births / group.births.sum()
#     return group
# names = names.groupby(['year', 'gender']).apply(add_prop)
#
#
# def get_top1000(group):
#     return group.sort_values(by='births', ascending=False)[:1000]
# grouped = names.groupby(['year', 'gender'])
# top1000 = grouped.apply(get_top1000)
# top1000.reset_index(inplace=True, drop=True)
# print(top1000)
#
# print(top1000[top1000.gender=='M']) #불린 참조
#
# total_births = top1000.pivot_table('births', index='year',
#                                    columns='name',
#                                    aggfunc=sum)
# total_births.info()
# subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# subset.plot(subplots=True, figsize=(12, 10),
#             title="Number of births per year")
# plt.show

import glob
print(glob.glob("c:/Windows/a*"))# *c드라이브 안에 윈도우 안에 a로 시작하는 모든 폴더 및 파일 이름 반환

import time
print(time.time()) #<1970년 1월 1일 0시~현재까지 경과된 시간을 초로 환산하여 출력>

before = time.time()
#내가 할 작업
after=time.time()

print(after-before) #작업을 수행하는데 걸리는 시간을 계산해낼 수 있다.

#정규표현식
#객체지향
#프론트엔드 (web제작)
