# 1. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후
# 다시 그 파일을 읽어서 출력하는 프로그램이다.
# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.

with open("q1_test.txt", "w") as f:  # 파일을 열고 그 이름을 f라고 하자
    f.write(input("문자열을 입력하세요: "))  # 파일에다 다음 내용을 출력
with open("q1_test.txt", "r") as f:
    print(f.read())

# 2. 다음과 같은 내용을 지닌 파일 test.txt가 있다.
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# Life is too short
# you need java
with open('q2_test.txt', 'w') as f:
    f.write("""
            Life is too short
            you need python
            """)


#
# 3. 게임 기업 입사문제
# 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
# 예를 들어
# n=91 -> 9+1+ 91
# d(91) = 9 + 1 + 91 = 101
# d(100)=1+0+0+100=101
# 이 때, n을 d(n)의 제네레이터(generator)라고 한다. 위의 예에서 91은 101의 제네레이터이다.
# 어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
# 그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
# 예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다.
# 1 이상이고 5000 보다 작은 모든 셀프 넘버들의 합을 구하라.

# 1. d(n)을 정의
# d(n) = 각 자릿수 숫자들의 합과
def make_generator(n):
    a = n % 1000
    b = n % 100
    dkssud = n // 1000 + a // 100 + b // 10 + n % 10 + n
    return dkssud


# 더 쉬운 정의 map함수 이용
# def make_generator(n):
#    result=  n + sum(map(int, str(n))) #str n은 시퀀스 자료가 되므로 하나씩 따로 읽힌다
#    return result
# map함수를 잘 쓰자...따흑

# for 문을 사용 할 수도 있다
# def make_generator(n):
#   sum=0
#   for i in range(0,len(list(n))):
#       sum+=int(list(n[i]))
#   sum+=int(n)
#    return sum

generator = set([])
number = set(list(range(1, 5001)))
for n in range(1, 5001):
    generator.add(make_generator(n))
self_num = number.difference(generator)  # 1부터 5000사이에서 generator없는 수가 셀프넘버
self_num = list(self_num)

sum_self_num = 0
for i in self_num:
    sum_self_num += i
print(sum_self_num)

# generator=list()
# for i in range(1,5000):
#   generator.append(d(Str(i)))

# print(sum(set(range(1,5000))-set(generator))


# 4. 상자 최대 낙차 출력(S회사)
# gravity :상자높이 배열
box = [7, 4, 2, 0, 0, 6, 0, 7, 0]
box.reverse()  # 사각형 돌리기 |
i = 0
while box[-1] != 0:  # 박스가 다 옮겨지지 않았으면 계속 수행
    if box[i] < box[i + 1]:  # 박스 옮길 자리 있으면
        box[i] = box[i + 1]  # 박스 아래로 옮기기
        box[i + 1] = 0  # 박스를 옮긴 자리에는 박스가 없다
        i += 1
    elif box[i] >= box[i + 1]:
        if box[i + 1] == 0:  # 둘다 0이면 옮길 박스가 없음
            box[i + 1] = box[i + 2]  # 다음층 박스를 가져온다
        else:
            pass


# 내가 원한 결과값: box = [7,6,2,4,7,0,0,0,0]
# 내가 얻은 결과값: 무한루프
# 모르겠어서 pass.....

# 맨 위의 상자가 낙차가 클 수 밖에 없다
# 모든 상자의 낙차를 구할 필요 없다!-->
#   작은 수가 몇개냐 : 낙차 구하는 것과 같음
# 내 밑에 더 작은수를 세면(count) 됨

def max_gravity(gravities):
    max_val = 0  # 최대 낙차 값 저장할 변수
    for i in range(len(gravities)):
        if gravities[i] == 0:  # 0이면 상자가 없으므로
            continue
        col_max_val = len(gravities) - i - 1  # 나올 수 있는 최대 낙차 : row - 현재 위치
        for j in range(i + 1, len(gravities)):  # i 보다 우측에 있는 상자들에서
            if gravities[i] <= gravities[j]:  # 같은 행에 상자가 있으면 낙차 -1
                col_max_val -= 1
        max_val = max(max_val, col_max_val)  # 현재 열의 최대낙차와 이전 최대낙차 비교후 큰 값 채택
    return max_val


g = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# 최대낙차: 7, g의 각 요소값을 기준으로 오른쪽에 나열된 요소값들과 비교하여
# 더 작은 경우에는 낙차가 생기므로, 낙차변수의 값을 1 증가

d = []
for i in range(len(g) - 1):  # i는 0~7 1을 뺀 건 0은 낙차가 생기지 않으니까
    df = 0  # 낙차 저장하기 위한 변수
    if g[i] == 0:
        continue
    for j in range(i + 1, len(g)):
        if g[i] > g[j]:  # 낙차가 발생되는 조건
            df += 1
    d.append(df)  # i층의 낙차가 d에 저장
# d에는 모든 층의 낙차가 저장된다
print(max(d))

# 5. 회문
# 출력예시)
# 입력? abba
# 회문입니다
#
# 입력?abcba
# 회문입니다
#
# 입력?test
# 회문이 아닙니다

data = input("입력: ")
if data[:] == data[-1::-1]:
    print("회문입니다.")
else:
    print("회문이 아닙니다.")
# sw = True
# for i in range(int(len(data)/2)): #홀수인 경우 중간 글자 비교 필요X #짝수인 경우 반으로 나눠비교
# if data[i] != data[len(data)-1-i]:
#   print("회문 아님")
#   sw=False
#   break
# (sw):
# print("회문")


