
import pygame as p
import random as r

p.init()#초기화

b=(0,0,0)

w=(255,255,255)

size = (600,800)

sc = p.display.set_mode(size)

p.display.set_caption("슈팅게임")

playing = True

#우주선
x = 0
y = 0
s_image = p.image.load("비행기.png")
s_rect = s_image.get_rect(left = 260, top = 700)

#배경
bg = p.image.load("배경.png")

#미사일
b_image = p.image.load("미사일.png")
b_list = []

#운석

stone = p.image.load("stone.png")
st_list = []

for a in range(10):
    st_rect = stone.get_rect(left = r.randint(0,500), top = 10)
    st_list.append(st_rect)




while playing:
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                y = -3
            if event.key == p.K_DOWN:
                y = 3
            if event.key == p.K_LEFT:
                x = -3
            if event.key == p.K_RIGHT:
                x = 3
            if event.key == p.K_SPACE:
                b_rect = b_image.get_rect(left = s_rect.left + 30, top = s_rect.top)
                b_list.append(b_rect)
        if event.type == p.KEYUP:
            if event.key == p.K_UP:
                y = 0
            if event.key == p.K_DOWN:
                y = 0
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
    s_rect.top += y
    s_rect.left += x
    sc.fill(w)
    sc.blit(bg,(0,0))
    for b_rect in b_list:
        sc.blit(b_image,b_rect)
    for b_rect in b_list:
        b_rect.top -= 10
        if b_rect.top <= 0:
            b_list.remove(b_rect)
    sc.blit(s_image,s_rect)

    for st_rect in st_list:
        sc.blit(stone,st_rect)
    for st_rect in st_list:
        st_rect.top+= 5
        if st_rect.top >= 800:
            st_list.remove(st_rect)
            st_rect = stone.get_rect(left = r.randint(0,500), top = 10)
            st_list.append(st_rect)
    for st_rect in st_list:
        for b_rect in b_list:
            if b_rect.colliderect(st_rect):
                b_list.remove(b_rect)
                st_list.remove(st_rect)
                st_rect = stone.get_rect(left = r.randint(0,500), top = 10)
                st_list.append(st_rect)

    
    p.display.flip() #화면 업데이트
    
