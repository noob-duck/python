import random as r

grade = [90,100,95,85,98]
result = 0
resultt = 0
print(grade[0])
print(grade[1])
print(grade[2])
print(grade[3])
print(grade[4])
print("------------------")
for x in range(5):
    result = result + grade[x]
    resultt = resultt + 1
print('총합은 :', result)
print('평균은 :',result/resultt)
print(r.choice(grade))
print('------------------')

take = [0,0,0,0,0]

take[0] = int(input('첫번째 숫자를 입력하세요'))
take[1] = int(input('두번째 숫자를 입력하세요'))
take[2] = int(input('세번째 숫자를 입력하세요'))
take[3] = int(input('네번째 숫자를 입력하세요'))
take[4] = int(input('다섯번째 숫자를 입력하세요'))
for x in range(5):
    print(take[x])



