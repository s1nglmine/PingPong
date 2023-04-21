from pygame import *
from random import randint

win_wight = 600
win_height = 500
window = display.set_mode((win_wight, win_height))
display.set_caption("пинг понг")
back = (75, 75, 75)
window.fill(back)

clock = time.Clock()

game = True
finish = False
FPS = 120

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#class Enemt(GameSprite):
#    def update(self):
#        self.rect.y += self.speed
#        global lost
#        if self.rect.y > win_height:
#            self.rect.x = randint(80, win_wight - 80)
#            self.rect.y = 0
#            lost = lost + 1
#
#class Asteroid(GameSprite):
#    def update(self):
#        self.rect.y += self.speed
#        if self.rect.y > win_height:
#            self.rect.x = randint(80, win_wight - 80)
#            self.rect.y = 0

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed() 

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_wight - 80:
            self.rect.y += self.speed

    def update_right(self):
        keys_pressed = key.get_pressed() 
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_wight - 80:
            self.rect.y += self.speed

ball = Player("ball.png", 300, 250, 50, 50, 5)
platform1 = Player("platforma.jpeg", 0, 250, 30, 150, 5)
platform2 = Player("platforma.jpeg", 570, 250, 30, 150, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(back)
    
    ball.reset()
    platform1.reset()
    platform2.reset()
    platform1.update_left()
    platform2.update_right()

#    if finish == False:
#        ship.update()
#        ship.reset()
#        monsters.update()
#        monsters.draw(window)
#        bullets.draw(window)
#        bullets.update()
#        asteriods.update()
#        asteriods.draw(window)
#        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
#        for i in sprites_list:
#            score = score + 1
#            monster = Enemt("ufo.png", randint(80, win_wight - 80), -40, 80, 50, randint(1, 5))
#            monsters.add(monster)
#
#        if sprite.spritecollide(ship, monsters, False) or sprite.spritecollide(ship, asteriods, False) or lost >= max_lost:
#            finish = True
#            window.blit(lose, (250, 250))
#
#        if rel_time and time.time - timer >= 3:
#            rel_time = False
#
#
#
#        text = font.render("Счёт: " + str(score), 1, (255, 255, 255))
#        window.blit(text, (10, 20))
#
#        text_lose = font.render("Пропущено: " + str(lost), 1, (255, 255, 255))
#        window.blit(text_lose, (10, 65))
#
#        if score >= max_score:
#            finish = True
#            window.blit(win, (250, 250))
#
# 
# 
# 
# 
# 
# 
    display.update()
    clock.tick(FPS)