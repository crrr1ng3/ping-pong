from pygame import *
font.init()

win_width, win_height = 700, 500
window = display.set_mode((win_width, win_height))
window.fill((51, 255, 255))
clock = time.Clock()
FPS = 60

run = True
finish = False


class GameSprite(sprite.Sprite):
    def __init__(self, imageName, speed, x, y, width, lenght):
        super().__init__()
        self.image = transform.scale(image.load(imageName), (width, lenght))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        return
    
player1 = Player('rocket.png', 15, 60, 250, 35, 150)
player2 = Player('rocket.png', 15, 600, 250, 35, 150)
ball = Ball('ball.png', 10, 305, 205, 50, 50)

while run:
    window.fill((51, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:

        player1.reset()
        player1.update_l()

        player2.reset()
        player2.update_r()


        clock.tick(FPS)
        display.update()