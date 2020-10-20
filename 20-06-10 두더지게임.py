
import pygame as p

import random as r

p.init()#초기화

b=(0,0,0)

w=(255,255,255)

size = (800,400)

sc = p.display.set_mode(size)

p.display.set_caption("게임판")

playing = True

clock = p.time.Clock()

font = p.font.SysFont('malgungothic',20)

score = 0

do = p.image.load("개굴딱이.png")

do_list = []

for x in range(10): #10번 반복하기
    do_rect = do.get_rect(left = r.randint(0,720), top = r.randint(0,320))
    do_list.append(do_rect)

while playing:
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
        if event.type == p.MOUSEBUTTONDOWN:
            for do_rect in do_list:
                if do_rect.collidepoint(event.pos[0], event.pos[1]):
                    do_list.remove(do_rect)
                    do_rect = do.get_rect(left = r.randint(0,720), top = r.randint(0,320))
                    sc.blit(do,do_rect)
                    do_list.append(do_rect)
                    score = score + 1
                    
            
            
    sc.fill(w)
    for do_rect in do_list:
        sc.blit(do,do_rect)
    text = font.render("점수 : {}".format(score),True,(0,0,0))
    sc.blit(text,(350,0))
    p.display.flip() #화면 업데이트
    
