import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Circle game")

done = False
x = 400
y = 400
pixels = 20

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= pixels
    if keys[pygame.K_RIGHT]:
        x += pixels
    if keys[pygame.K_DOWN]:
        y += pixels
    if keys[pygame.K_UP]:
        y -= pixels

    x = max(0, min(x, screen.get_width()))
    y = max(0, min(y, screen.get_height()))

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, 'Brown', (x, y), 25)

    pygame.display.flip()

    clock.tick(4)