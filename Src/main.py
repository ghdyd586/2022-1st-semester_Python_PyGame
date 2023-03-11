from turtle import goto
import pygame
from player import Player
from bullet import Bullet
import random as rnd
import time 


#총알과 충돌했을 때의 함수
def collision(obj1, obj2):
    dist = ((obj1.pos[0] - obj2.pos[0]) ** 2 + (obj1.pos[1] - obj2.pos[1]) **2) **0.5
    return dist < 20

#텍스트 출력하기 위한 함수
def draw_text(txt, size, pos, color):
    font = pygame.font.Font('freesansbold.ttf',size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)


#생명력 저장하는 정수형 변수와 배열
lifecnt = 10
lcarr = [1,1,1,1,1,1,1,1,1,1]



#게임 초기화
pygame.init()
#윈도우 크기 설정
WIDTH, HEIGHT = 800, 600

#윈도우 제목 설정
pygame.display.set_caption("총알 피하기")

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60

#배경음악 설정
pygame.mixer.music.load('bgm.wav')
pygame.mixer.music.play(-1)


#순서대로 배경 이미지, 폭발 이미지, 생명력 막대기 이미지
bg_image = pygame.image.load('bg.jpg')
bg_pos = (-150,-150)
boom_image = pygame.image.load('boom.png')
life_image = pygame.image.load('life.png')
sparkle_image = pygame.image.load('sparkle.png')

#생명력 막대기 이미지 크기조절
life_image = pygame.transform.scale(life_image, (25,50))
sparkle_image = pygame.transform.scale(sparkle_image, (40,40))


#플레이어 아이콘의 위치를 설정
player = Player(WIDTH/2, HEIGHT/2)

bullets = []

#총알 추가하는 변수
for i in range(1):
    bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
    
time_for_adding_bullets = 0

#시작 시간을 변수로 설정
start_time = time.time()

score = 0

gameover = False
running = True
while running:

    dt = clock.tick(FPS)
    time_for_adding_bullets +=dt



    # 이벤트 받는 부분
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #키를 눌렀을 때 행동
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)
                
            elif event.key == pygame.K_RIGHT:
                player.goto(1, 0)
                
            elif event.key == pygame.K_UP:
                player.goto(0, -1)
                
            elif event.key == pygame.K_DOWN:
                player.goto(0, 1)
                

        #키를 누르지 않았을 때 행동
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1, 0)
                
            elif event.key == pygame.K_RIGHT:
                player.goto(-1, 0)
                
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
                
            elif event.key == pygame.K_DOWN:
                player.goto(0, -1)
                

    player.update(dt, screen)
    #텍스트 파일을 읽는 것을 변수로 저장
    read_scoreboard = open("score.txt", "r", encoding ="UTF8")
    readline = read_scoreboard.readline()
    read = read_scoreboard.read()
    readlines = read_scoreboard.readlines()
    scorearr = []
    
    #텍스트 파일을 읽는 것을 변수로 저장
    append_scoreboard = open("score.txt", "a", encoding = "UTF8")
    #최종 점수를 소수점 3자리 반올림 한 형태로 저장
    final_score = "{:.3f}".format(score)
        
    #배경 위치 변수를 시간이 흐름에 따라 조금씩 위치가 증가하도록 설정
    
    bg_goto = player.get_to()

    bg_pos = (bg_pos[0] + bg_goto[0] * -0.01 * dt, bg_pos[1] + bg_goto[1] * -0.01 * dt)
    bg_pos = (max(min(bg_pos[0], 0), -2053 + WIDTH), max(min(bg_pos[1], 0), -1500 + HEIGHT))

    #배경 출력
    screen.blit(bg_image, bg_pos)
    player.update(dt, screen)
    player.draw(screen)

    #총알에 대한 반복문
    for b in bullets:
        b.bullet1(dt,screen)
        bulife = -1
        #점수가 5점 이상일 경우 총알 바뀜
        if score > 5 :
            b.bullet2(dt,screen)
            bulife = -1
        #점수가 10점 이상일 경우 총알 바뀜
        #bullet3은 생명력 1씩 증가
        if score > 10:
            b.bullet3(dt,screen)
            bulife = 1
        #점수가 15점 이상일 경우 총알 바뀜
        #bullet4는 생명력 2씩 차감
        if score > 15:
            b.bullet4(dt,screen)
            bulife = -2
        
    
    for b in bullets:
        if collision(b,player):
            #총알에 닿았을 때 소리를 재생하게 함
            soundObj = pygame.mixer.Sound('boom.wav')
            soundObj.play()
            #총알에 닿았을 때 그림을 출력하게 함
            screen.blit(boom_image, (50,50))
            player.draw(screen)
            
            #생명력 카운트가 0보다 클 때 충돌한 경우, 생명력을 1 또는 2 감소하거나 1 증가
            if lifecnt > 0 :
                if bulife == -1:
                    lcarr[lifecnt-1] = 0
                    lifecnt -=1
                    Player.mujeok = True
                    Player.mujeoktime = 2000
                elif bulife == 1:
                    if lifecnt >= 10 :
                        lifecnt = 10
                    elif lifecnt < 10 :
                        lcarr[lifecnt] = 1
                        lifecnt +=1
                elif bulife == -2:
                    for i in range(2):
                        lcarr[lifecnt-1] = 0
                        lifecnt -=1
                    Player.mujeok = True
                    Player.mujeoktime = 2000    
                    
            
            #생명력 카운트가 0일경우, 현재 점수를 텍스트 파일로 저장
            if lifecnt == 0:
                lifecnt = -1
                fin = append_scoreboard.write(final_score+ '\n')
                scorearr.append(fin)
                append_scoreboard.close()
                gameover = True
                
                
    if gameover :
        #게임오버 문구 및 점수, 총알 개수 출력
        
        draw_text("GAME OVER", 100, (WIDTH/2 - 300, HEIGHT/2 - 50), (255, 255, 255))
        txt = f"Time : {score:.3f}, Bullets : {len(bullets)}"
        draw_text(txt, 32, (WIDTH/2 -150,HEIGHT/2 + 50), (255, 255, 255))
        
        
        #점수 출력
        tmpwid = WIDTH/2-40
        tmphei = HEIGHT/2+100
        
        draw_text(read, 32, (tmpwid, tmphei), (255, 255, 255))
        read_scoreboard.close()
        
    
            
    else:
        #점수 계산법은 끝난 시간에서 시작 시간 뺀 것
        score = time.time() - start_time

        #게임오버가 아닐 경우 위쪽에 점수와 총알 개수, 생명력을 출력
        txt = f"Time : {score:.3f}, Bullets : {len(bullets)}, Life : {lifecnt}"
        draw_text(txt, 32, (10,10), (255, 255, 255))

        

        #생명력을 막대기 형태로 출력
        if lcarr[0] == 1:
            screen.blit(life_image, (520,540))
        if lcarr[1] == 1:
            screen.blit(life_image, (545,540))
        if lcarr[2] == 1:
            screen.blit(life_image, (570,540))
        if lcarr[3] == 1:
            screen.blit(life_image, (595,540))
        if lcarr[4] == 1:
            screen.blit(life_image, (620,540))
        if lcarr[5] == 1:
            screen.blit(life_image, (645,540))
        if lcarr[6] == 1:
            screen.blit(life_image, (670,540))
        if lcarr[7] == 1:
            screen.blit(life_image, (695,540))
        if lcarr[8] == 1:
            screen.blit(life_image, (720,540))
        if lcarr[9] == 1:
            screen.blit(life_image, (745,540))
            



        if time_for_adding_bullets > 1000:
            bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))
            time_for_adding_bullets -= 1000

    pygame.display.update()