from pygame import *
font.init()

win_width, win_height = 700, 500
window = display.set_mode((win_width, win_height))
window.fill((51, 255, 255))
display.set_caption('Ping-Pong')
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

speed_x, speed_y = 3, 3
    

player1 = Player('rocket.png', 15, 60, 250, 35, 150)
player2 = Player('rocket.png', 15, 600, 250, 35, 150)
ball = GameSprite('ball.png', 10, 305, 205, 50, 50)

font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))


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

        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))


        clock.tick(FPS)
        display.update()
