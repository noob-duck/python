import pygame as p
import random as r
import time as t

p.init()#초기화

b=(0,0,0)

yellow = (255,255,0)

w=(255,255,255)

size = (800,400)

sc = p.display.set_mode(size)

p.display.set_caption("게임판")

playing = True

c1 = p.image.load("1c.png")
c1_rect = c1.get_rect(left = r.randint(50,750), top = r.randint(50,350))

c2 = p.image.load("2c.png")
c2_rect = c2.get_rect(left = r.randint(50,750), top = r.randint(50,350))

c3 = p.image.load("3c.png")
c3_rect = c3.get_rect(left = r.randint(50,750), top = r.randint(50,350))

c4 = p.image.load("4c.png")
c4_rect = c4.get_rect(left = r.randint(50,750), top = r.randint(50,350))

c5 = p.image.load("5c.png")
c5_rect = c5.get_rect(left = r.randint(50,750), top = r.randint(50,350))

c_3 = p.image.load("-3c.png")
c_3_rect = c_3.get_rect(left = r.randint(50,750), top = r.randint(50,350))

rc = p.image.load("rc.png")
rc_rect = rc.get_rect(left = r.randint(50,750), top = r.randint(50,350))


#배경음
cs = p.mixer.Sound("coin.wav")
p.mixer.music.load("hope.mp3")
p.mixer.music.play(1)

c = p.image.load("개굴딱이.png")
c_rect = c.get_rect(left = 200, top = 300)

x = 0

y = 0

score = 0
font = p.font.SysFont("malgungothic",30)
font1 = p.font.SysFont("malgungothic",20)
font2 = p.font.SysFont("malgungothic",50)

bg = p.image.load("다운로드.png")

#멈춘 시간
t1 = t.time()

#먹이
meat = 1

while playing:
    t2 = t.time()
    time = 60 - int(t2 - t1)
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
    
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                y = -2
            if event.key == p.K_DOWN:
                y = 2
            if event.key == p.K_LEFT:
                x = -2
            if event.key == p.K_RIGHT:
                x = 2
        if event.type == p.KEYUP:
            if event.key == p.K_UP:
                y = 0
            if event.key == p.K_DOWN:
                y = 0
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
    c_rect.top += y
    c_rect.left += x
    if c_rect.left <= 0:
        x = 0
    if c_rect.left >= 730:
        x = 0
    if c_rect.top <= 0:
        y = 0
    if c_rect.top >= 320:
        y = 0
    if c_rect.colliderect(c1_rect):
        c1_rect.left = r.randint(50,750)
        c1_rect.top = r.randint(50,350)
        p.mixer.Sound.play(cs)
        score += 1*meat
    if c_rect.colliderect(c2_rect):
        c2_rect.left = r.randint(50,750)
        c2_rect.top = r.randint(50,350)
        p.mixer.Sound.play(cs)
        score += 2*meat
    if c_rect.colliderect(c3_rect):
        c3_rect.left = r.randint(50,750)
        c3_rect.top = r.randint(50,350)
        p.mixer.Sound.play(cs)
        score += 3*meat
    if c_rect.colliderect(c4_rect):
        c4_rect.left = r.randint(50,750)
        c4_rect.top = r.randint(50,350)
        p.mixer.Sound.play(cs)
        score += 4*meat
    if c_rect.colliderect(c5_rect):
        c5_rect.left = r.randint(50,750)
        c5_rect.top = r.randint(50,350)
        p.mixer.Sound.play(cs)
        score += 5*meat
    if c_rect.colliderect(rc_rect):
        rc_rect.left = r.randint(50,750)
        rc_rect.top = r.randint(50,350)
        p.mixer.Sound.play(cs)
        score += meat*r.choice([-5,-5,-5,-3,-3,-3,-1,-1,-1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,100])
    if c_rect.colliderect(c_3_rect):
        c_3_rect.left = r.randint(50,750)
        c_3_rect.top = r.randint(50,350)
        p.mixer.Sound.play(cs)
        score += -3*meat
    

    text = font.render("현재 점수: {}".format(score),True,(255,255,0))
    text1 = font1.render("남은 시간: {}".format(time),True,(0,0,0))
    text2 = font2.render("결과 점수: {}".format(score),True,(141,203,47))
    
    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(text,(50,350))
    sc.blit(text1,(350,50))
    sc.blit(c,(c_rect))
    sc.blit(c1,(c1_rect))
    sc.blit(c2,(c2_rect))
    sc.blit(c3,(c3_rect))
    sc.blit(c4,(c4_rect))
    sc.blit(c5,(c5_rect))
    sc.blit(rc,(rc_rect))
    sc.blit(c_3,c_3_rect)
    if time <= 30:
        sc.blit(text2,(275,150))
        p.mixer.music.stop()
        playing = False
    if time <= 35:
        meat = 2
        p.draw.line(sc,yellow,[0,0],[800,0],20)
        p.draw.line(sc,yellow,[0,0],[0,400],20)
        p.draw.line(sc,yellow,[0,400],[800,400],20)
        p.draw.line(sc,yellow,[800,400],[800,0],20)
        p.mixer.music.pause()
        fever = p.mixer.Sound("fever.wav")
        fever.play()
        
    
    p.display.flip() #화면 업데이트

