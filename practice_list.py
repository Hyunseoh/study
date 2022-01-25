#1. 리스트 생성
#영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
#순위	영화
#1	    닥터 스트레인지
#2	    스플릿
#3	    럭키
movie_rank = ["닥터 스트레인지","스플릿","럭키"]
print(movie_rank)

#2. movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("배트맨")
print(movie_rank)

#3. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

#4. movie_rank 리스트에서 '럭키'를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove("럭키")
print(movie_rank)

#5. movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.pop();movie_rank.pop()
print(movie_rank)
#another answer
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)
#another answer
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
for i in range(len(movie_rank)):
    if movie_rank[i] == '스플릿':
        del movie_rank[i]
    elif movie_rank[i] == '배트맨':
        del movie_rank[i] 
    print(movie_rank)

#6. price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
#출력 예시: [100, 130, 140, 150, 160, 170]
print(price[1:])

#7.슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#8.슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
#실행 예:[5, 4, 3, 2, 1]
print(nums[::-1])

#9.interest 리스트에는 아래의 데이터가 저장되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#출력 예시:삼성전자 Naver
print(interest[0],interest[-1])


#10. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
#출력 예시:삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(' '.join(interest))


#11. interest 리스트에는 아래의 데이터가 바인딩되어 있다.
#interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
#출력 예시:
#삼성전자
#LG전자
#Naver
#SK하이닉스
#미래에셋대우
print("\n".join(interest[:]))

#12. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
# another answer
sorted(data)


#13. 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과
#그 뒤의 숫자 부분으로 나누어 출력해 보자.

#문자열 슬라이싱
ID = "881120-1068234"
Birthdate = ID[0:6] #위치 찾을 때 인덱스 함수 사용하면 편하다
ID_Num = ID[7:] #find (-) index: Id.index("-")
print(Birthdate,ID_Num)

#another answer
#split 매서드 사용 
ID = "881120-1068234"
Birthdate,ID_Num =ID.split("-")
print(Birthdate,ID_Num)

#another answer



#14. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자.
#※ 더하기(+)를 사용해 보자.

t1 = (1,2,3)
t2 = list(t1)+ [4]
t3= tuple(t2);
print(t3,type(t3))

# 15. 다음과 같은 딕셔너리 a가 있다.
# a = dict()
# a
# {}

# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
# a['name'] = 'python'
# a[('a',)] = 'python'
# a[[1]] = 'python'
# a[250] = 'python'

#Answer: a[[1]] = 'python' 이 error 발생할 것이다.
    #키는 변형이 불가능한데 리스트는 변형이 가능하므로

#16. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'A':90, 'B':80, 'C':70}
#※ 딕셔너리의 pop 함수를 사용해 보자.

print(a.pop("B"))


#17. 리스트 year에 연도, population에 서울시 인구수가 저장되어 있습니다.
# 다음 소스 코드를 완성하여 최근 3년간 연도와 인구수가 리스트로 출력되게 만드세요.
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
Population_by_year_R3 = dict(zip(year[-3:],population[-3:]))
print(Population_by_year_R3.items())

# another answer
recent = []
for y, p in zip(year[-3:],population[-3:]):
   recent.append([y,p])
   print(recent)
# another answer
data=dict(zip(year, population))
print(list(data.items())[-3:]) 
#another answer
dic=dict(zip(year, population))
print(list(zip(dic.keys,dic.values)))


#18. 다음 소스 코드를 완성하여 튜플 n에서 인덱스가 홀수인 요소들이 출력되게 만드세요.
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])
#another answer


# 19. 표준 입력으로 숫자 또는 문자열 여러 개가 입력되어 리스트 x에 저장됩니다(입력되는 숫자 또는 문자열의 개수는 정해져 있지 않음).
# 리스트 x의 마지막 요소 5개를 삭제한 뒤 튜플로 출력되게 만드세요.

#
# 입력
# 1 2 3 4 5 6 7 8 9 10
# 결과
# ('1', '2', '3', '4', '5')

Click_num_del5 = list(input("숫자입력: ").split())
del Click_num_del5[-5:]
print(tuple(Click_num_del5))




# 입력
# oven bat pony total leak wreck curl crop space navy loss knee
# 결과
# ('oven', 'bat', 'pony', 'total', 'leak', 'wreck', 'curl')
#

Click_str_del5 = list(input("문자입력: ")).split()
del Click_str_del5[-5:]
print(Click_str_del5)





# 20. 표준 입력으로 문자열 두 개가 각 줄에 입력됩니다(문자열의 길이는 정해져 있지 않음).
# 첫 번째 문자열에서 인덱스가 홀수인 문자와 두 번째 문자열에서 인덱스가 짝수인 문자를 연결하여 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다).
# 연결 순서는 첫 번째 문자열, 두 번째 문자열 순입니다. 그리고 0은 짝수로 처리합니다.

Put_str1 = input()
Put_str2 = input()

NewPut_str = Put_str1[1::2]+Put_str2[::2]
print(NewPut_str)