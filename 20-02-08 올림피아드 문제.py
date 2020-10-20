day = int(input('오늘 날짜를 입력하세요')) % 10

car = [0,0,0,0,0]

violation = 0

car[0] = int(input('첫번째 차 끝자리'))
car[1] = int(input('두번째 차 끝자리'))
car[2] = int(input('세번째 차 끝자리'))
car[3] = int(input('네번째 차 끝자리'))
car[4] = int(input('다섯번째 차 끝자리'))

for x in range(5):
    if car[x] == day:
        violation = violation + 1
print('위반한 차량 수는',violation)
        
