import pygame as p

import time as t

p.init()#초기화

b=(0,0,0)

w=(255,255,255)

size = (800,400)

sc = p.display.set_mode(size)

p.display.set_caption("게임판")

playing = True

a = p.image.load("airplane.png")
a_rect = a.get_rect(left = 0, top = 150)
a_y = 5

clock = p.time.Clock()

while playing:
    clock.tick(15) 
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
        if event.type == p.KEYDOWN:
            if event.key == p.K_SPACE:
                a_y = -3
        if event.type == p.KEYUP:
            if event.key == p.K_SPACE:
                a_y = 2
                
    sc.fill(w)
    sc.blit(a,(a_rect))
    a_rect.top += a_y
    p.display.flip() #화면 업데이트
    
