#
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