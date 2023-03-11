import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.pos = [x, y]
        self.to = [0, 0]
        self.angle = 0
        self.mujeok = False
        self.mujeoktime = 0

    #플레이어의 이동경로를 저장하는 함수
    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y

    #플레이어가 맵 안에 위치하도록 설정하는 함수
    def update(self, dt, screen):
        width, height = screen.get_size()
        phw = self.image.get_width() / 2
        phh = self.image.get_height() / 2
        self.pos[0] = self.pos[0] + dt * self.to[0]
        self.pos[1] = self.pos[1] + dt * self.to[1]
        self.pos[0] = min(max(self.pos[0], phw), width-phw)
        self.pos[1] = min(max(self.pos[1], phh), height-phh)

        self.mujeoktime -=dt
        if self.mujeoktime < 0 :
            self.mujeok = False



    def draw(self, screen):
       

        
        #플레이어가 이동하는 방향에 따라 각도 설정
        if self.to == [-1,-1]:  self.angle = 45
        elif self.to == [-1,0]:  self.angle = 90
        elif self.to == [-1,1]:  self.angle = 135
        elif self.to == [0,1]:  self.angle = 180
        elif self.to == [1,1]:  self.angle = 225
        elif self.to == [1,0]:  self.angle = 270
        elif self.to == [1,-1]:  self.angle = 315
        elif self.to == [0,-1]:  self.angle = 0

        rotated = pygame.transform.rotate(self.image, self.angle)
        

        calib_pos = (self.pos[0] - rotated.get_width()/2, 
                     self.pos[1] - rotated.get_height()/2)
        screen.blit(rotated, calib_pos)

        if self.mujeok :
            if self.mujeoktime :
                screen.blit(rotated, calib_pos)
        else :
            screen.blit(rotated,calib_pos)

    def get_pos(self):
        return self.pos
    def get_to (self):
        return self.to