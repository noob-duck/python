import pygame as p

p.init() #초기화
size = (400,400)
b = (0,0,0) #(R,G,B)
w = (255,255,255)
sc = p.display.set_mode(size)
p.display.set_mode(size) #해상도설정
p.display.set_caption('image') #창이름
x= p.image.load('1.png')
y= p.image.load('2.png')
z= p.image.load('3.png')
p.mixer.music.load('1.mp3')
p.mixer.music.load('2.mp3')
p.mixer.music.play()
done = False

while not done:
    print('반복중')
    for event in p.event.get(): #사용자가 뭘 눌렀는지 감지 
        if event.type == p.QUIT: # 게임창 x 버튼을 눌렀다면
            done = True #계속 반복을 종료
            p.mixer.music.stop
            print('반복 끝남')

    sc.fill(w)                #배경화면 색깔 설정
    sc.blit(x,(200,100))
    sc.blit(y,(100,100))
    sc.blit(z,(0,100))
    p.display.flip()
    


