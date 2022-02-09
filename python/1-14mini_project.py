#못풀었던 내용
# 1.입력 가장 많이 나온 순서대로 단어 10개와 그 단어의 빈도를 출력

#아래 내용을 가진 텍스트파일을 미리 만들어 두고, 프로그램을 실행하면 파일 내용을 읽어들인다
# 작업1. 파일 만들기와 파일 읽기
with open ('sample.txt','w') as f:
    f.writelines("As the country became embroiled in a domestic crisis, the first government was dislodged and succeeded by several different administrations. Bolikango served as Deputy Prime Minister in one of the new governments before a partial state of stability was reestablished in 1961. He mediated between warring factions in the Congo and briefly served once again as Deputy Prime Minister in 1962 before returning to the parliamentary opposition. After Joseph-Desire Mobutu took power in 1965, Bolikango became a minister in his government. Mobutu soon dismissed him but appointed him to the political bureau of the Mouvement Populaire de la Revolution. Bolikango left the bureau in 1970. He left Parliament in 1975 and died seven years later. His grandson created the Jean Bolikango Foundation in his memory to promote social progress. The President of the Congo posthumously awarded Bolikango a medal in 2005 for his long career in public service.")
with open ('sample.txt','r') as f:
    text = str(f.read()) #실패1.(readlines 써서 text가 리스트가 됨)(read를 써야 한 문장으로 읽힌다)

words_with_marks = text.split()

# 작업1. 읽어낸 문장을 단어 단위로 나누기
words=[] # 문장 안 단어들
for i in words_with_marks: #작업2. 문장 부호 삭제
    if ',' in i:
        words.append(i[:i.find(",")]) #문장부호
    elif '.' in i:
        words.append(i.replace(".",'')) #삭제하고 저장
    else:
        words.append(i) # 이제 words 에는 문장 부호를 제외한 단어들만 저장됨    

#2-1 단어갯수 저장하는 리스트 만들기
count_words=[] #단어의 빈도를 세는 리스트
for i in range(len(words)):
    count_words.append(words.count(words[i]))

    #2-2 단어개수와 단어 매칭하기
match=list(set(zip(words,count_words))) #[('단어',단어의 빈도)]
word=list(set(words)) # 중복 제거한 단어들
num=list(set(count_words)) # 중복 숫자들


#제출답변
# 1.입력 가장 많이 나온 순서대로 단어 10개와 그 단어의 빈도를 출력

#아래 내용을 가진 텍스트파일을 미리 만들어 두고, 프로그램을 실행하면 파일 내용을 읽어들인다
# 작업1. 파일 만들기와 파일 읽기
with open ('sample.txt','w') as f:
    f.writelines("As the country became embroiled in a domestic crisis, the first government was dislodged and succeeded by several different administrations. Bolikango served as Deputy Prime Minister in one of the new governments before a partial state of stability was reestablished in 1961. He mediated between warring factions in the Congo and briefly served once again as Deputy Prime Minister in 1962 before returning to the parliamentary opposition. After Joseph-Desire Mobutu took power in 1965, Bolikango became a minister in his government. Mobutu soon dismissed him but appointed him to the political bureau of the Mouvement Populaire de la Revolution. Bolikango left the bureau in 1970. He left Parliament in 1975 and died seven years later. His grandson created the Jean Bolikango Foundation in his memory to promote social progress. The President of the Congo posthumously awarded Bolikango a medal in 2005 for his long career in public service.")
with open ('sample.txt','r') as f:
    text = str(f.read()) #실패1.(readlines 써서 text가 리스트가 됨)(read를 써야 한 문장으로 읽힌다)

words_with_marks = text.split()

# 작업2. 읽어낸 문장을 단어 단위로 나누기
words=[] # 문장 안 단어들
for i in words_with_marks: #아직 문장부호를 가지고 있는 단어 목록에서
    if ',' in i:
        words.append(i[:i.find(",")]) #문장부호
    elif '.' in i:
        words.append(i.replace(".",'')) #삭제하고 저장
    else:
        words.append(i) # 이제 words 에는 문장 부호를 제외한 단어들만 저장됨

# 작업3. (단어: 단어개수) 묶어주기: 딕셔너리 이용
dic={} #딕셔너리에는 '단어':단어개수 저장됨
for word in words:
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1
    # 키<--> 밸류 변환 방법 두 가지
    #   dict(map(lambda e:(e[1],e[0]), dic.items()))
    #   print(dict((value,key) for (key,value) in dic.items()))

# 작업4. 개수 세기
# (가장 많이 나온 순서대로 단어 10개와 그 단어의 빈도를 출력하기)
# 모르겠어서 풀이 참조했는데 그래도 잘 모르겠습니다ㅜㅜ
print(sorted(dic.items(), key=lambda dic: dic[1], reverse=True)[0:10:])

# 2. 모스 부호 해독
# 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
# 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
# .... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--


# 작업 1. dic 만들기
# 입력값과 key 값을 차례대로 비교해서 value 값을 출력할 예정
Mosdict = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}
# 작업2. 입력받을 변수 생성
mos=list(input("모스 부호를 입력하세요: ").split('  ')) #입력값 저장(공백 두 개)(단어들로 나눠서 저장)
# 작업3. 해독 프로그램 만들기
def Translate_mos(mos):
    M_list=[]
    for i in mos: #단어들
        for j in i.split(' '):#글자 사이 공백 지정
            M_list.append(Mosdict[j]) #해당 모스 부호에 맞는 알파벳 찾아 리스트에 넣어줌
    M_list.append(" ") #단어 사이 띄어쓰기 넣어줌(없으면 HESLEEPSEARLY로 글자 붙여서 나옴)
    return "".join(M_list)
print(Translate_mos(mos))

# 3.
# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
#
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.


result = input("퀴즈 결과를 입력하세요: ") #퀴즈 결과 입력받음
score=0 #OX판별해 점수 받을 변수
finalScore=0 #콤보점수(연속되면 앞의 점수+1) 포함한 실제 점수
for i in result: #입력받은 데이터 값에서
    if i == 'O': #정답이 나오면
        score+=1 #1점 적립
        finalScore+=score #앞 점수에 대해 +적용(combo역할)
    else: #오답이면
        score=0 #combo 없어지고 초기값으로 리셋됨
print(finalScore)

# s= 0; t=0
# if x= 'O' s+=1 t+=s

# 4.
# 문제
# 상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다.
# 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.
# 각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.
# 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다.
# 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
recordEnter=[]
recordLeave=[]
n = int(input("출입 기록의 수: ")) #출입 기록을 입력받는다
for _ in range(n): # 입력한 수만큼 출입 기록을 입력받는다.
    name,OX=input("출입기록 :").split()
    if OX == 'enter': #들어오면
        recordEnter.append(name) #들어온 사람 이름 리스트에 추가
    elif OX == 'leave': #떠나면
        recordLeave.append(name) #떠난 사람 리스트에 추가
    for i in recordEnter: #출근 리스트에서
        if i in recordLeave: #퇴근했으면
            recordEnter.remove(i) #이름빼줌
print(recordEnter) #출근 상태인 사람의 이름만 출력됨



# 5.
# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다.
# 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에,
# 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
# (인접해있으면 계속 이동 가능)
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다.
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.
# 1	 1	0	0	0	0	0	0	0	0
# 0	 1	0	0	0	0	0	0	0	0
# 0	 0	0	0	1	0	0	0	0	0
# 0	 0	0	0	1	0	0	0	0	0
# 0	 0	1	1	0	0	0	1	1	1
# 0	 0	0	0	1	0	0	1	1	1
# 입력

T_num = int(input("테스트 케이스의 수를 입력: "))
for _ in T_num: #입력받은 테스트 케이스 수만큼 반복
    M, N, K = map(int,input("가로길이, 세로길이, 배추 개수: ").split())
    field = [[0]*M for _ in range(N)] # 밭을 N행(세로) M열(가로) 0으로 초기화
                                        # #[0,0,0...](0이 m개)인 리스트가 n개 들어간 리스트가 밭 초기값
    for _ in K: #줄마다 배추 심어야 하니까 일단 K번 반복
        x, y = map(int, input().split()) # x와 y라는 위치를 할당받는다.
        field[x][y]=1 #밭의 x, y위치에 배추를 심어줌

#푸는중...