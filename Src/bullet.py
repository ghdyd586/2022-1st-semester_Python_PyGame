import pygame

class Bullet:
    def __init__(self, x, y, to_x, to_y):
        #총알의 위치를 저장한 변수
        self.pos = [x,y]
        #총알의 이동하는 위치를 저장한 변수
        self.to = [to_x, to_y]
        #총알의 크기를 저장한 배열
        self.radius = [7,8,9,10]
        #총알의 색상을 저장한 배열
        self.color = [(255, 128 ,0),(190,0 ,0),(126,118,236),(251,255,92)]
    #총알에 대한 함수
    def bullet1(self, dt, screen):
        
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + self.to[0] * dt) %width
        self.pos[1] = (self.pos[1] + self.to[1] * dt) %height
        pygame.draw.circle(screen, self.color[0], self.pos, self.radius[0])  
        
    
    def bullet2(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + self.to[0] * dt/5 ) %width
        self.pos[1] = (self.pos[1] + self.to[1] * dt/5 ) %height
        pygame.draw.circle(screen, self.color[1], self.pos, self.radius[1])

    def bullet3(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + self.to[0] * dt/6) %width
        self.pos[1] = (self.pos[1] + self.to[1] * dt/6) %height
        pygame.draw.circle(screen, self.color[2], self.pos, self.radius[2])

    def bullet4(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + self.to[0] * dt/7) %width
        self.pos[1] = (self.pos[1] + self.to[1] * dt/7) %height
        pygame.draw.circle(screen, self.color[3], self.pos, self.radius[3])
        
