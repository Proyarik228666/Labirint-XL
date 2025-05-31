from pygame import *

class GameSpite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSpite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSpite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super(). __init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 900
win_height = 800
window = display.set_mode((win_width, win_height))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

player = Player('hero.png', 5, win_width - 80, 4)
monster1 = Enemy('cyborg.png', 500, 500, 25)
monster2 = Enemy('cyborg.png', 350, 200, 15)
monster3 = Enemy('cyborg.png', 200, 100, 20)
final = GameSpite('treasure.png', win_width - 100, 50, 0)

w1 = Wall(154, 205, 50, 100, 20, 675, 20)
w2 = Wall(154, 205, 50, 100, 750, 650, 20)
w3 = Wall(154, 205, 50, 750, 120, 20, 650)
w4 = Wall(154, 205, 50, 100, 20, 20, 650)
w5 = Wall(154, 205, 50, 200, 120, 20, 550)
w6 = Wall(154, 205, 50, 200, 120, 450, 20)
w7 = Wall(154, 205, 50, 630, 20, 20, 100)
w8 = Wall(154, 205, 50, 200, 650, 150, 20)
w9 = Wall(154, 205, 50, 450, 650, 200, 20)
w10 = Wall(154, 205, 50, 630, 370, 20, 300)
w11 = Wall(154, 205, 50, 630, 370, 120, 20)
w12 = Wall(154, 205, 50, 450, 220, 300, 20)
w13 = Wall(154, 205, 50, 200, 220, 120, 20)
w14 = Wall(154, 205, 50, 300, 230, 20, 300)
w15 = Wall(154, 205, 50, 300, 530, 150, 20)
w16 = Wall(154, 205, 50, 530, 220, 20, 330)


game = True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 150)
win = font.render('ты победил!', True, (255, 215, 0))
lose = font.render('ты проиграл:(', True, (180, 0, 0))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        player.update()
        monster1.update()
        monster2.update()
        monster3.update()

        player.reset()
        monster1.reset()
        monster2.reset()
        monster3.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()

        if sprite.collide_rect(player, monster1) or sprite.collide_rect(player, monster2) or sprite.collide_rect(player, monster3) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w14) or sprite.collide_rect(player, w15) or sprite.collide_rect(player, w16):
            finish = True
            window.blit(lose, (100, 350))
            kick.play()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (100, 350))
            money.play()
    display.update()
    clock.tick(FPS)