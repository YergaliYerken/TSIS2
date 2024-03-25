import pygame
import os

pygame.init()

# Set up the Pygame window (not needed for a music player, but for event handling)
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Music Player")

# Load music files into a list
music_files = ["music1.mp3.wav", "music2.mp3.wav", "music3.mp3.wav"]
current_track = 0

def play_music():
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    play_music()

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()
            elif event.key == pygame.K_ESCAPE:  # Добавлено условие для выхода по нажатию клавиши Escape
                running = False

    # Add additional logic here if needed