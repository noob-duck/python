import pygame as p

p.init()#초기화

b=(0,0,0)

w=(255,255,255)

size = (600,800)

sc = p.display.set_mode(size)

p.display.set_caption("게임판")

playing = True

pan = p.image.load("pan.png")

p_rect = pan.get_rect(left = 240, top = 720)
x = 0

bg = p.image.load("배경화면.png")

b = p.image.load("ball.png")
b_rect = b.get_rect(left = 270, top = 680)
b_x = 10
b_y = 10

score = 0



#game over
font = p.font.SysFont("malgungothic", 50)
font1 = p.font.SysFont("malgungothic", 30)

#벽돌생성
block = p.image.load("brick.png")
block_list = []

for x1 in range(20):
    for y1 in range(10):
        blo_rect = block.get_rect(left = 30*x1, top = 40*y1)
        block_list.append(blo_rect)
while playing:
    for event in p.event.get(): #무슨 키를 눌렀는지 감지
        if event.type == p.QUIT: #게임창에 x버튼 눌렀을 때
            playing == False #계속 반복하기 종료
            p.quit() #게임창 종료
            quit # sell  창 종료
        if event.type == p.KEYDOWN:  #키보드 눌렀을 때 감지
            if event.key == p.K_LEFT:
                x = -20
            if event.key == p.K_RIGHT:
                x = 20
        if event.type == p.KEYUP:  #키보드 눌렀을 때 감지
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
    p_rect.left += x
    if p_rect.left >= 500:
        p_rect.left = 500
    if p_rect.left <= 0:
        p_rect.left = 0
        
                
                
            
    sc.fill(w)

    sc.blit(bg,(0,0))
    
    sc.blit(pan,(p_rect))
    sc.blit(b,(b_rect))

    #공 움직이기
    b_rect.top += b_y
    b_rect.left += b_x
    if b_rect.top >= 780:
        playing = False
        sc.blit(text,(170,350))
        pass
    if b_rect.top <= 0:
        b_y = 10
    if b_rect.left >= 560:
        b_x = -10
    if b_rect.left <= 0:
        b_x = 10
    if p_rect.colliderect(b_rect):
        b_y = -10
    text = font.render("Game Over", True, (255,0,0))

    for blo_rect in block_list:
        sc.blit(block,blo_rect)
    for blo_rect in block_list:
        if b_rect.colliderect(blo_rect):
            block_list.remove(blo_rect)
            b_y = 10
            score += 10
    text1 = font1.render("점수: {}".format(score),True,(255,255,0))
    sc.blit(text1,(0,750))
            
    text2 = font1.render("남은 갯수: {}".format(len(block_list)),True,(255,255,0))
    text3 = font.render("CLEAR",True,(0,255,0))
    if len(block_list) <= 180:
        sc.blit(text3,(220,350))
        playing = False
    sc.blit(text2,(400,750))
    p.display.flip() #화면 업데이트

    
