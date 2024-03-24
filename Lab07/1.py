import pygame
import datetime
import math
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((600, 600))     #, flags = pygame.NOFRAME
pygame.display.set_caption("Clock")
done = False

myfont = pygame.font.SysFont('Times New Roman', 100)
text_12 = myfont.render('12', True, 'White')
text_6 = myfont.render('6', True, 'White')
text_3 = myfont.render('3', True, 'White')
text_9 = myfont.render('9', True, 'White')


while not done:

        screen.fill((100, 100, 100)) #Цвет экрана

        
        myCircle = pygame.draw.circle(screen, 'Black', (300, 300), 250) #Создание круга

        centre = pygame.draw.circle(screen, 'Red', (300, 300), 20)

        screen.blit(text_12, (250, 50))
        screen.blit(text_6, (270, 440))
        screen.blit(text_3, (490, 230))
        screen.blit(text_9, (70, 240))

        current_time = datetime.now()
        seconds = current_time.second
        minutes = current_time.minute

        angle = seconds * 6
        gradus = minutes * 6

        image = pygame.image.load('cifer.png')
        image_rect = image.get_rect(center=(0, 0))

        pygame.draw.line(screen, 'Green', (300, 300), (300 + 200 * math.sin(math.radians(angle)), 300 - 200 * math.cos(math.radians(angle))), 10)
        pygame.draw.line(screen, 'Yellow', (300, 300), (300 + 130 * math.sin(math.radians(gradus)), 300 - 130 * math.cos(math.radians(gradus))), 10)


        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        
        
        