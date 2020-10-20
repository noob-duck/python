import pygame as p
import random as r

p.init()#초기화

b=(0,0,0)

a = 0

w=(255,255,255)

size = (800,400)

sc = p.display.set_mode(size)

p.display.set_caption("마우스 제어")

do_image = p.image.load("python.png")

do_rect = do_image.get_rect(left = r.randint(0,750), top = r.randint(0,350))

font = p.font.SysFont('malgungothic',20)



playing = True

while playing:
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
        if event.type == p.MOUSEBUTTONDOWN:
            print("마우스를 눌렀을 때")
            if do_rect.collidepoint(event.pos[0], event.pos[1]):
                do_rect.left = r.randint(0,750)
                do_rect.top = r.randint(0,350)
                a = a+1
    
        if event.type == p.MOUSEBUTTONUP:
            print("마우스를 뗐을 때")

            
    sc.fill(w)

    sc.blit(do_image,do_rect)

    text = font.render("점수 :{}".format(a),True,b)

    sc.blit(text,(350,0))

    
    
    p.display.flip() #화면 업데이트
    
