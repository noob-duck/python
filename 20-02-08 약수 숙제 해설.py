n = int(input('약수를 구하고 싶은 수를 입력하세요'))
total = 0
count = 0

for x in range(1,n+1):
    if n%x == 0:
        print(n,'의 약수는' , x,'입니다')
        total = total + x
        count = count + 1
print('약수 값의 총 합은 ', total)
print('약수 값의 총 개수는', count)
        
