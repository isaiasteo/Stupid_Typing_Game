import pygame
import os

audio_available = True

try:
    pygame.mixer.init()

except pygame.error as e:
    print(f"Audio system unavailable: {e}")
    audio_available = False


def sfx(audio_path):

    if not audio_available:
        return False

    if not os.path.isfile(audio_path):
        return False

    try:
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        return True

    except pygame.error:
        return False
