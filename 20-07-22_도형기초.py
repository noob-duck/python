import pygame as p

p.init()#초기화

b=(0,0,0)

w=(255,255,255)

size = (500,500)

sc = p.display.set_mode(size)

p.display.set_caption("게임판")

playing = True

while playing:
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
    sc.fill(w)
    p.display.flip() #화면 업데이트
    
