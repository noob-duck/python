while True:
    print("======================")
    print("== 1. 정수 출력하기 ==")
    print('== 2. 짝수 출력하기 ==')
    print('== 3. 홀수 출력하기 ==')
    print('== 4. 배수 출력하기 ==')
    print('== 5. 약수 출력하기 ==')
    print('== 6. 그만하기 =======')
    print('======================')

    s = int(input('메뉴를 선택하세요'))

    if s == 6:
        print('프로그램을 종료합니다')
        break
    if s == 5 or s == 4 or s == 3 or s == 2 or s == 1:
        x = int(input('최댓값은? : '))
        if s == 4 or s == 5:
            n = int(input('숫자값은? : '))
    if s == 1:
        for x in range(1,x+1):
            print('출력할 값은 ',x,'입니다')
    elif s == 2:
        for x in range(1,x+1):
            if x % 2 == 0:
                print('짝수 값은 ',x,'입니다')
    elif s == 3:
        for x in range(1,x+1):
            if x % 2 == 1:
                print('홀수 값은 ',x,'입니다')
    elif s == 4:
        for x in range(1, x+1):
            if x % n == 0:
                print(n ,'의 배수는 ',x,'입니다')
    elif s == 5:
        for x in range(1, n+1):
            if n % x == 0:
                print(n,'의 약수는 ',x,'입니다')
                  
        
        
    

    
   
