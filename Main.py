import math

one_result = {}
two_result = {}
final_result = {}
tnov = 0 

class Calculate: # 정당의 정보를 통해 수월하게 계산하기 위하여 클래스를 이용합니다.
    def __init__(self, nov, name): # 각 정당 별 데이터 저장
        self.nov = nov
        self.name = name
    
    def one_cal(self, bnov): # 1차 배분
        return self.nov / bnov
    
def ask(msg, type): # 질문할때마다 while, try 문을 이용하는 것이 번거롭기 때문에 함수로 지정합니다.
    while True: 
        try:
            if type == int:
                answer = int(input(f'{msg} >>> '))
            else:
                answer = input(f'{msg} >>> ')
        except Exception as errormsg:
            print(f'\n 올바른 값을 입력해주세요. \n\n ')
            continue
        else:
            break

    return answer


print('='*56, end='\n\n')
print(' '*7, '대한민국 비례대표 의석수 분배 프로그램')
print(' '*9, '헤어-니마이어 계산법 (최대잔여법)')
print(' '*14, '24-01-26', end='\n\n')
print('='*56, end='\n\n')
input('시작하려면 아무 키나 누르십시오. . . ')

party_count = ask('비례대표 선거에 출마한, 봉쇄조항을 충족한 정당의 총 개수를 입력해주세요.', int)

for i in range(party_count):
    print(f'\n{i+1}/{party_count}')
    party_name = ask('정당의 이름을 입력해주세요.', None)
    party_nov = ask('정당의 득표수를 입력해주세요', int) 
    tnov += party_nov

    globals()[f'party_class{i}'] = Calculate(party_nov, party_name)

for i in globals().copy(): # globals()은 모든 전역 변수를 담은 딕셔너리다. 이 반복문 안에서 전역 변수가 변화되게 될 경우, global()의 값 또한 변화가 생기게 되어 Runtime 에러가 발생하게 된다. 그러므로, global()를 복사 해줌으로써 문제를 해결하게 되었다.
    if i[0:11] == 'party_class':
    
        one_nos = globals()[i].one_cal(tnov // 47) # 기준득표수. 기준득표수는 총득표수 나누기 의석인데, 대한민국의 비례대표 의석수는 47석이기에 47로 나눠주도록 한다.
        nosmodf = math.modf(one_nos)
        one_result[globals()[i].name] = nosmodf[1]
        two_result[globals()[i].name] = nosmodf[0]

final_result = one_result.copy()
two_result = sorted(two_result.items(), key = lambda x: x[1], reverse= True)
re_seat = int(47 - sum(one_result.values()))

if re_seat != 0:
    for i in range(re_seat):
        final_result[two_result[i][0]] += 1 

print('\n' + '='*56, end='\n\n')

for i in final_result.keys():
    print(f'{i} : {int(final_result[i])} 석', end='\n\n')

print('='*56, end='\n\n')
print('여러가지 변수로 인해 실제 의석배분과 약간의 차이가 있을 수 있습니다.')
print('\n' + '='*56)
