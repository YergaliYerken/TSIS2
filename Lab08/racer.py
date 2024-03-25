import pygame
from pygame.locals import *
import random
pygame.init()

pygame.display.set_caption('Racer')
screen = pygame.display.set_mode((840, 650))
done = False

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,650-40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (420, 325)

def update(self):
    pressed_keys = pygame.key.get_pressed()

    if self.rect.left > 0:
          if pressed_keys[K_LEFT]:
              self.rect.move_ip(-5, 0)
    if self.rect.left > 0:       
          if pressed_keys[K_RIGHT]:
              self.rect.move_ip(5, 0)

def move(self):
  self.rect.move_ip(0,10)
  if (self.rect.top > 600):
      self.rect.top = 0
      self.rect.center = (random.randint(30, 370), 0)              

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    image = pygame.image.load('asphalt.png')
    image_rect = image.get_rect(center=(420, 325))
    screen.blit(image, image_rect)
    
    pygame.display.update()

    FPS = pygame.time.Clock()
    FPS.tick(60)