import pygame as p

p.init() #라이브러리 초기火

w = (255,255,255) #흰색
b = (0,0,0)
r = (255,0,0)

size = (400,400)

sc = p.display.set_mode(size) #해상도크기 설정

p.display.set_caption("컨트롤")

done = True

x=50#도형 변수

y=50




a= p.image.load('2.png')



while done:
    for event in p.event.get(): #사용자가 뭘 누르는지 감지 
        if event.type == p.QUIT:
            done = False # 계속반복 종료
            p.quit() #x버튼 누르면 게임창 사라짐
            quit() #sell 창 종료
        if event.type == p.KEYDOWN:#키보드를 눌렀을 때
            if event.key == p.K_UP: #위 방향키를 누르면
                print("위 방향키를 눌렀습니다.")
                y = y-1
            if event.key == p.K_RIGHT: #오른쪽 방향키를 누르면
                print("오른쪽 방향키를 눌렀습니다.")
                x=x+1
            if event.key == p.K_LEFT: #왼쪽 방향키를 누르면
                print("왼쪽 방향키를 눌렀습니다.")
                x=x-1
            if event.key == p.K_DOWN: #아래쪽 방향키를 누르면
                print("아래 방향키를 눌렀습니다.")
                y = y+1
            if event.key == p.K_a: #만약 단축키 a를 누르면
                w = (255,0,0)
                
        if event.type == p.KEYUP:#키보드를 땠을 때
            if event.key == p.K_UP: #위 방향키를 때면
                print("위 방향키를 땠습니다.")
            if event.key == p.K_RIGHT: #오른쪽 방향키를 때면
                print("오른쪽 방향키를 땠습니다.")
            if event.key == p.K_LEFT: #왼쪽 방향키를 때면
                print("왼쪽 방향키를 땠습니다.")
            if event.key == p.K_DOWN: #아래쪽 방향키를 때면
                print("아래 방향키를 땠습니다.")
            if event.key == p.K_a:
                w = (255,255,255)
                
    sc.fill(w) #배경색 흰색으로 설정
    sc.blit(a,(x,y))
    p.display.flip() #화면 업데이트
    
    
    
