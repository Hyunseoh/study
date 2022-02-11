#1. 리스트에서 20 보다 작은 3의 배수를 출력하라
list = [13, 21, 12, 14, 30, 18]
num_3=[]
for i in list:
    if i <20 and i%3 == 0:
        num_3.append(i)
print(num_3)


#2. 리스트에서 세 글자 이상인 단어를 화면에 출력하라
list = ["I", "study", "python", "language", "!"]
overlen_3 =[]
for i in range(len(list)):
    if len(list[i]) >= 3:
        overlen_3.append(list[i])
print(overlen_3)
    
#another answer #better answer
list = ["I", "study", "python", "language", "!"]
for i in list:
    if len(i) > 3:
        print(i)


#3. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. 
list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in range(len(list)):
    only_name,filetype = list[i].split(".")
    print(only_name)

# for i in range(len(list)) 보다는 바로 for i in list를 써주는 것이 좋다

#another answer
list = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list:
    print(i[:i.index(".")]) #print(i.find("."))

    

#4. my_list를 아래와 같이 출력하라.

my_list = ["가", "나", "다", "라"]
i = 0
while True:
    print(my_list[i],end= " ") # 바로 print(출력1, 출력2) 를 해줬어도 됐다.
    print(my_list[i+1])
    i+= 1
    if i == 3:
        break
#another answer
for i in range(len(my_list)-1):
    print(my_list[i],my_list[i+1])

        

#5. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]
print_list =[]
for i in range(len(my_list)-1): # range(3)--> i = 0 to 2 
    print_list = my_list[-i-1] +" " + my_list[-i-2]
    print(print_list)


#6.리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, 
# low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

for i in range(0,5):    
    volatility = []
    volatility.append(high_prices[i]-low_prices[i])
    print(volatility)



#7.리스트에 저장된 데이터를 아래와 같이 출력하라.

apart = [ [101, 102], [201, 202], [301, 302] ]
#101 호
#102 호
#-----
#201 호
#202 호
#-----
#301 호
#302 호
#-----

for i in apart:
    for j in i: #[101,102]/
        print(j,"호", end ="\n")
    print("-----")


#8. 구글 입사 test
#1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
#8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
#(※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

count_8 = 0
for i in range(1,10001):
    if str(i).count('8') > 0:
        count_8 += str(i).count('8')
print(count_8)

#another answer
print(str(list(range(1,10001))).count('8'))
#한줄로도 코딩이 가능하다

