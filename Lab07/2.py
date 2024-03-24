import pygame

pygame.init()
screen = pygame.display.set_mode((333, 333))
pygame.display.set_caption("Music")
done = False

pygame.mixer.music.load("1.mp3")
pygame.mixer.music.play(0)

Pause = False
Next = False
Previous = False
current_track = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Pause = not Pause
                if Pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_6:
                Next = True
                
            elif event.key == pygame.K_4:
                Previous = True

    if Next:
        pygame.mixer.music.stop()
        current_track += 1
        if current_track > 3:
            current_track = 1
        pygame.mixer.music.load(f"{current_track}.mp3")
        pygame.mixer.music.play(0)
        Next = False
    elif Previous:
        pygame.mixer.music.stop()
        current_track -= 1
        if current_track < 1:
            current_track = 3
        pygame.mixer.music.load(f"{current_track}.mp3")
        pygame.mixer.music.play(0)
        Previous = False