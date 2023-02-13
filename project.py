#Этот код писал я, Масленицын Роман Игоревич
from pygame import *
import random 
def startgame():
    screensize = [1280, 720]

    def attack():
        randSprite = random.choice(Enemies.sprites())
        randSprite.shoot()

    class GameSprite(sprite.Sprite):
        def __init__(self, picture, w, h, x ,y):
            sprite.Sprite.__init__(self)
            self.image = transform.scale(image.load(picture), (w, h))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

    class player(GameSprite):
        def __init__(self, picture, w, h, x ,y):
            GameSprite.__init__(self, picture, w, h, x ,y)
            self.x_speed = 0
            self.y_speed = 0

        def update(self):
            ''''''
            touch = sprite.spritecollide(self, bulletsE, False)
            

            self.rect.x += self.x_speed
            
            if self.rect.right > screensize[0]:
                self.rect.right = screensize[0]
            if self.rect.left < 0:
                self.rect.left = 0

            
            self.rect.y += self.y_speed
            
            if self.rect.bottom > screensize[1]:
                self.rect.bottom = screensize[1]
            if self.rect.top < screensize[1]//2:
                self.rect.top = screensize[1]//2

            
        def shoot(self):
            bulletH = BulletH(
                'Energyball.png', 
                self.rect.top, 
                self.rect.centerx, 
                (self.rect.x // 4), 
                (self.rect.x // 4), 
                10
                ) 
            bulletsH.add(bulletH)



    class Enemy(GameSprite):
        def __init__(self, picture, w, h, x , y, x_speed):
            GameSprite.__init__(self, picture, w, h, x ,y)
            self.x_speed = x_speed
            self.stopPointR = x + int(screensize[0]//12 * 1.45)
            self.stopPointL = x - screensize[0]//12
        
        def update(self):
            if self.rect.x < self.stopPointL:
                self.x_speed = 3
            if self.rect.x > self.stopPointR:
                self.x_speed = -3
            
            self.rect.x += self.x_speed

        def shoot(self):
            bulletE = BulletE(
                'Blaster.png', 
                (self.rect.centerx), 
                (self.rect.bottom), 
                (self.rect.x // 6), 
                (self.rect.y // 6), 
                4
                )
            bulletsE.add(bulletE)
    
    class BulletE(GameSprite): 
        def __init__(self, picture, x, y, width, height, speed): 
            super().__init__(x, y, width, height, picture) 
            self.speed = speed 
        def update(self): 
            self.rect.y += self.speed 
            if self.rect.y >= screensize[1]: 
                self.kill()
    
    class BulletH(GameSprite): 
        def __init__(self, picture, x, y, width, height, speed): 
            super().__init__(x, y, width, height, picture) 
            self.speed = speed 
        def update(self): 
            self.rect.y -= self.speed 
            if self.rect.y <= 0: 
                self.kill()

    window = display.set_mode(screensize)
    display.set_caption('MegaMakson9000 Cosmic Adventures')
    window.fill((255, 255, 255))
    bg = transform.scale(image.load('cosmos.jpg'), screensize)
    window.blit(bg, (0, 0))

    Enemies = sprite.Group()
    bulletsE = sprite.Group()
    bulletsH = sprite.Group()

    Hero = player(
        'MegaMakson.png', 
        int(screensize[0]*0.07), 
        int(screensize[0]*0.07), 
        ((screensize[0]//2) - int(screensize[0]*0.1) // 2), 
        (screensize[1] - screensize[1]//5)
    )

    fool0 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 1), (screensize[0]//11 * 0), 3)
    fool1 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 2), (screensize[0]//11 * 0), 3)
    fool2 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 3), (screensize[0]//11 * 0), 3)
    fool3 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 4), (screensize[0]//11 * 0), 3)
    fool4 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 5), (screensize[0]//11 * 0), 3)
    fool5 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 6), (screensize[0]//11 * 0), 3)
    fool6 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 7), (screensize[0]//11 * 0), 3)
    fool7 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 8), (screensize[0]//11 * 0), 3)
    fool8 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 9), (screensize[0]//11 * 0), 3)
    fool9 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 10), (screensize[0]//11  * 0), 3)
    fool10 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 1), (screensize[0]//11  * 1), 3)
    fool11 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 2), (screensize[0]//11  * 1), 3)
    fool12 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 3), (screensize[0]//11  * 1), 3)
    fool13 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 4), (screensize[0]//11  * 1), 3)
    fool14 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 5), (screensize[0]//11  * 1), 3)
    fool15 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 6), (screensize[0]//11  * 1), 3)
    fool16 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 7), (screensize[0]//11  * 1), 3)
    fool17 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 8), (screensize[0]//11  * 1), 3)
    fool18 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 9), (screensize[0]//11  * 1), 3)
    fool19 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 10), (screensize[0]//11  * 1), 3)
    fool20 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 1), (screensize[0]//11  * 2), 3)
    fool21 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 2), (screensize[0]//11  * 2), 3)
    fool22 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 3), (screensize[0]//11  * 2), 3)
    fool23 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 4), (screensize[0]//11  * 2), 3)
    fool24 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 5), (screensize[0]//11  * 2), 3)
    fool25 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 6), (screensize[0]//11  * 2), 3)
    fool26 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 7), (screensize[0]//11  * 2), 3)
    fool27 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 8), (screensize[0]//11  * 2), 3)
    fool28 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 9), (screensize[0]//11  * 2), 3)
    fool29 = Enemy('Enemy.png', int(screensize[0]*0.05), int(screensize[0]*0.05), (int(screensize[0] // 12) * 10), (screensize[0]//11  * 2), 3)
    Enemies.add(fool0)
    Enemies.add(fool1)
    Enemies.add(fool2)
    Enemies.add(fool3)
    Enemies.add(fool4)
    Enemies.add(fool5)
    Enemies.add(fool6)
    Enemies.add(fool7)
    Enemies.add(fool8)
    Enemies.add(fool9)
    Enemies.add(fool10)
    Enemies.add(fool11)
    Enemies.add(fool12)
    Enemies.add(fool13)
    Enemies.add(fool14)
    Enemies.add(fool15)
    Enemies.add(fool16)
    Enemies.add(fool17)
    Enemies.add(fool18)
    Enemies.add(fool19)
    Enemies.add(fool20)
    Enemies.add(fool21)
    Enemies.add(fool22)
    Enemies.add(fool23)
    Enemies.add(fool24)
    Enemies.add(fool25)
    Enemies.add(fool26)
    Enemies.add(fool27)
    Enemies.add(fool28)
    Enemies.add(fool29)

    

    recharge = 0
    peew = True
    run = True
    while run:
        time.delay(50)
        for i in event.get():
            if i.type == QUIT:
                run = False
            elif i.type == KEYDOWN:
                if i.key == K_a:
                    Hero.x_speed = -10
                elif i.key == K_d:
                    Hero.x_speed = 10
                elif i.key == K_s:
                    Hero.y_speed = 10
                elif i.key == K_w:
                    Hero.y_speed = -10
            if i.type == MOUSEBUTTONDOWN:
                Hero.shoot()

            elif i.type == KEYUP:
                if i.key == K_a:
                    Hero.x_speed = 0
                elif i.key == K_d:
                    Hero.x_speed = 0
                elif i.key == K_s:
                    Hero.y_speed = 0
                elif i.key == K_w:
                    Hero.y_speed = 0
            
                    

        window.fill((255, 255, 255))
        window.blit(bg, (0, 0))
        Hero.update()
        Hero.reset()
        for i in Enemies:
            i.update()
            i.reset()
        for i in bulletsE:
            i.update()
            i.reset()
        for i in bulletsH:
            i.update()
            i.reset()

        '''if peew == False:
            attack()
            peew = True
        elif peew:
            recharge += 1
        if recharge >= 70:
            peew = False'''
        
  
        display.update()