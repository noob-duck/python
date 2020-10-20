import pygame as p

p.init() #초기화
size = (400,400)
b = (0,0,0) #(R,G,B)
w = (255,255,255)
sc = p.display.set_mode(size)
p.display.set_mode(size) #해상도설정0
p.display.set_caption('image') #창이름
x= p.image.load('1.png')
done = False
x1 = 100
y1 = 100

while not done:
    print('반복중')
    for event in p.event.get(): #사용자가 뭘 눌렀는지 감지 
        if event.type == p.QUIT: # 게임창 x 버튼을 눌렀다면
            done = True #계속 반복을 종료
        if event.type == p.KEYDOWN: #키보드를 누를 때
            if event.key == p.K_UP:
                y1 -= 10 #y1 = y1- 1
            elif event.key == p.K_DOWN:
                y1 += 10 #y1 = y1 + 1
                

    sc.fill(w)                #배경화면 색깔 설정
    sc.blit(x,(x1,y1))
    p.display.flip()
    


