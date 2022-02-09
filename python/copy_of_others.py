# 1
t = 'As the country became embroiled in a domestic crisis, the first government was dislodged and succeeded by several different administrations. Bolikango served as Deputy Prime Minister in one of the new governments before a partial state of stability was reestablished in 1961. He mediated between warring factions in the Congo and briefly served once again as Deputy Prime Minister in 1962 before returning to the parliamentary opposition. After Joseph-Desire Mobutu took power in 1965, Bolikango became a minister in his government. Mobutu soon dismissed him but appointed him to the political bureau of the Mouvement Populaire de la Revolution. Bolikango left the bureau in 1970. He left Parliament in 1975 and died seven years later. His grandson created the Jean Bolikango Foundation in his memory to promote social progress. The President of the Congo posthumously awarded Bolikango a medal in 2005 for his long career in public service.'
with open('t.txt', 'w') as f:
    f.write(t)


def word_frequency(file):
    frequency_dict = dict()
    with open(f'{file}.txt', 'r') as tf:
        text = tf.read()
    sliced_text = text.split()
    for word in sliced_text:
        word = word.replace('.', '')
        word = word.replace(',', '')
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else:
            frequency_dict[word] += 1
    return sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)


frequency = word_frequency('t')
for word in frequency[:10]:
    print(word[0], word[1])

# 2
m = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
morse_dict = {
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z'
}


def translate_morse(code):
    morse_words = code.split("  ")
    text = ""
    for mose_word in morse_words:
        mose_chars = mose_word.split(" ")
        for mose_char in mose_chars:
            text += morse_dict[mose_char]
        text += " "
    return text


print(translate_morse(m))


# 3
def score(result):
    correct_list = result.split('X')
    score = 0
    for correct in correct_list:
        if correct:
            score += part_score_math(correct)
    return score


# for 문으로 계산
def part_score(part):
    score = 0
    for i in range(1, len(part) + 1):
        score += i
    return score


# 수식으로 계산
def part_score_math(part):
    n = len(part)
    return (n * (n + 1)) // 2


c_num = int(input())
results = [input() for _ in range(c_num)]
for result in results:
    print(score(result))


# 4
def left_employee(logs):
    employee_dict = {}
    for log in logs:
        employee, record = log
        if record == "enter":
            employee_dict[employee] = True
        else:
            employee_dict[employee] = False
    left_employees = []
    for employee in employee_dict:
        if employee_dict[employee]:
            left_employees.append(employee)
    return sorted(left_employees, reverse=True)


n = int(input())
geegle_logs = [input().split() for _ in range(n)]
geegle_left = left_employee(geegle_logs)
print('\n'.join(geegle_left))

# 5

from collections import deque


def earthworms(cabbages, size):
    m, n = size
    earthworm_num = 0
    cabbage_field = [[0] * m for _ in range(n)]
    for cabbage in cabbages:
        x, y = cabbage
        cabbage_field[y][x] = 1
    for y in range(n):
        for x in range(m):
            if cabbage_field[y][x]:
                search_field(cabbage_field, [x, y])
                earthworm_num += 1
    return earthworm_num


def search_field(field, point):
    visit, visited = deque(), list()
    visit.append(point)
    while visit:
        now = visit.popleft()
        nx, ny = now
        if field[ny][nx]:
            field[ny][nx] = 0
            if [nx + 1, ny] not in visited and nx < len(field[0]) - 1:
                visit.append([nx + 1, ny])
            if [nx, ny + 1] not in visited and ny < len(field) - 1:
                visit.append([nx, ny + 1])
    return field


T = int(input())
ans = []
for _ in range(T):
    M, N, K = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(K)]
    ans.append(earthworms(C, [M, N]))
for a in ans:
    print(a)