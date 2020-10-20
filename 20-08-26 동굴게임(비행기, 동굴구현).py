import pygame as p

import copy as c

import time as t

import random as r

p.init()#초기화

b=(0,0,0)

g = (0,255,0)

w=(255,255,255)

size = (800,600)

sc = p.display.set_mode(size)

p.display.set_caption("게임판")

playing = True

a = p.image.load("airplane.png")
a_rect = a.get_rect(left = 0, top = 150)
a_y = 5

clock = p.time.Clock()

#동굴
rects = []

for x in range(80):
    rect = p.Rect(x*10,100,10,400)
    rects.append(rect)
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
                
    sc.fill(g)
    #동굴 업로드
    for rect in rects:
        p.draw.rect(sc,b,rect)
    for rect in rects:
        rect.left = rect.left - 10
    del rects[0]
    #동굴 그리기
    new_rect = c.deepcopy(rects[-1])
    new_rect.left = new_rect.left +10
    rects.append(new_rect)
    
    
    sc.blit(a,(a_rect))
    a_rect.top += a_y
    p.display.flip() #화면 업데이트
    
