
import pygame as p
import random as r

p.init()#초기화

b=(0,0,0)

w=(255,255,255)

size = (800,400)

sc = p.display.set_mode(size)

p.display.set_caption("게임을 시작하지")

playing = True

b = p.image.load("100.png")

b_rect = b.get_rect(left = 600, top = 40)

c = p.image.load("1000.png")

c_rect = b.get_rect(left = 600, top = 175)

m = p.image.load("10000.png")

m_rect = b.get_rect(left = 600, top = 310)

re = p.image.load("get money.png")

r_rect = re.get_rect(left = 0, top = 300)

bg = p.image.load("dobak.png")

don = 10000

font = p.font.SysFont("malgungothic",20)

s1 = p.mixer.Sound("coin.wav")
s2 = p.mixer.Sound("getmoney.wav")
s3 = p.mixer.Sound("losemoney.wav")

#확률변수
box = 0

while playing:
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
        if event.type == p.MOUSEBUTTONDOWN:
            if b_rect.collidepoint(event.pos):
                if don >= 100:
                    box = r.choice([1,1,2,1,1])
                    if box == 1:
                        don += 200
                        s2.play()
                    else:
                        s3.play()
                        don -= 100
                        
                
            if c_rect.collidepoint(event.pos):
                if don >= 1000:
                    box = r.choice([1,2,1,2,1])
                    if box == 1:
                        don += 2000
                        s2.play()
                    else:
                        s3.play()
                        don -= 1000
                        
                
            if m_rect.collidepoint(event.pos):
                if don >= 10000:
                    box = r.choice([1,2,2,2,2])
                    if box == 1:
                        don += 20000
                        s2.play()
                    else:
                        s3.play()
                        don -= 10000
                        
                
            if r_rect.collidepoint(event.pos):
                print("환전 버튼")
                don += 100
                s1.play()
    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(b,(b_rect))
    sc.blit(c,(c_rect))
    sc.blit(m,(m_rect))
    sc.blit(re,(r_rect))
    text = font.render("돈 : {}".format(don),True,(255,255,0))
    sc.blit(text,(30,30))
    
    p.display.flip() #화면 업데이트
    
