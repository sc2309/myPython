import pygame
import os

def play_music():

    # Initialize pygame
    pygame.init()

    music_path = "TheRiseOfSkywalkerThemeEpicVersion1.mp3"

    # Check if the music file exists
    if not os.path.exists(music_path):
        print(f"Music file '{music_path}' not found.")
        exit()

    # Create a pygame mixer
    pygame.mixer.init()

    # Load the music file
    pygame.mixer.music.load(music_path)

    # Set the volume (optional)
    pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed (0.0 to 1.0)

    # Play the music in an infinite loop
    pygame.mixer.music.play()