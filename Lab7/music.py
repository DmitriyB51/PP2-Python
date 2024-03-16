import pygame
from pygame import mixer
mixer.init()

songs = ["C:/Users/OmeN_HP/Downloads/Drake_-_Best_I_Ever_Had_48270083.mp3", "C:/Users/OmeN_HP/Downloads/Rihanna_Drake_-_Work_48112888.mp3", "C:/Users/OmeN_HP/Downloads/Drake_-_Gods_Plan_53025361.mp3"]

playing = True
i = 0
pygame.mixer.music.load(songs[0])
print(f"Press  'p' to play, 's' to pause\nPress 'n' to next song\nPress 'pr' to previous song\n PRESS 'c' TO CLOSE")
while playing:


    s = str(input())

    pygame.mixer.music.play()
    if s == 'p':

        pygame.mixer.music.unpause()

    elif s == 's':
        pygame.mixer.music.pause()
    elif s == 'n':
        i +=1
        pygame.mixer.music.load(songs[i])
        pygame.mixer.music.play()
    elif s == 'pr':
        i -= 1
        pygame.mixer.music.load(songs[i])
        pygame.mixer.music.play()
    elif s == 'c':

        playing = False















