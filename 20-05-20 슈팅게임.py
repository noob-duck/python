import pygame as p

p.init()
w = (255,255,255)
size = (740,370)
bg = p.image.load("bg1.png")
h = p.image.load("4.png")
sc = p.display.set_mode(size)

p.display.set_caption("슈팅겜")

playing = True

while playing:
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            quit()
    sc.fill(w)
    sc.blit(bg,(0,0))
    sc.blit(h,(50,50))
    p.display.flip() #화면 업데이트
