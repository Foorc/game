from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption("пинг-понг")
background = transform.scale(image.load("pole.jpg"), (700, 500))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image1), (65, 65))
        self.speed = speed    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
        


class Enemy(GameSprite):
    
    def update(self):

        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -50
            self.rect.x = randint(1,560)
            self.speed = randint(1,5)

            global lost
            lost = lost + 1