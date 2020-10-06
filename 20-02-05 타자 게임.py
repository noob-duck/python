import random as r
import time as t

w = ['']
n = 1
print('[타자게임 아님?] 준비되지 않으면 엔터치지 마시오')
input()
start = t.time()
q = r.choice(w)

while n <= 500:
    print('*문제',n)
    print(q)
    x = input()
    if q == x:
        print('통과')
        n = n+1
        q = r.choice(w)
    else:
        print('오타! 다시하세요')
end = t.time()
et = end - start
et2 = format(et,'.2f')
print('타자시간 :',et2, '초')


