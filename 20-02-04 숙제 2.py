n = int(input('약수를 구할 수는?'))
a = 0
b = 0
for x in range(1,n+1):
    if n%x == 0:
        print(x)
        a = a+1
        b = b+x
print('약수의 개수 :',a,'개 입니다')
print('약수의 합은 :',b,'개 입니다')
    

