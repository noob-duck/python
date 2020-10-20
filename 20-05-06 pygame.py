import pygame as py
import turtle as t

py.init() #파이게임 라이브러리초기화

Black = (0,0,0)
White = (255,255,255)
Blue = (0,0,255)
Red = (255,0,0)
Green = (0,255,0)

size = [400,400]

screen = py.display.set_mode(size)

py.display.set_caption("정말 재미있는 게임(?)")

done = False

clock = py.time.Clock()

while not done:
    clock.tick(10) #초당 10번 화면 출력

    for event in py.event.get():  #상태 체크
        if event.type == py.QUIT:  #만일 창 옆에 있는 X를 누를 경우 
            done = True

    screen.fill(White)
    py.draw.rect(screen, Black,[0,100,100,100],5) #사각형 rect
    py.draw.polygon(screen,Blue,[[50,50],[0,100],[100,100]]) #삼각형 polygon
    py.draw.circle(screen,Red,[360,50],40,2) #원 circle
    py.draw.line(screen,Green,[150,150],[200,200],5)#선 line
    py.draw.line(screen,Black,[25,150],[75,150],5)
    py.draw.line(screen,Black,[50,125],[50,175],5)
    py.draw.rect(screen,Black,[25,125,50,50],5)
    

    py.display.flip() #게임 화면 업데이트
      
