from pygame import mixer
import pygame as pg
mixer.init()
pg.init()
screen = pg.display.set_mode((1500, 760))
songs = ["C:/Users/OmeN_HP/Downloads/Drake_-_Best_I_Ever_Had_48270083.mp3", "C:/Users/OmeN_HP/Downloads/Drake_-_Gods_Plan_53025361.mp3"]

playing = True
i = 0

pg.mixer.music.load(songs[0])
print(f"Press  'p' to play, 's' to pause\nPress 'n' to next song\nPress 'pr' to previous song\n PRESS 'c' TO CLOSE")
while playing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False

    s = str(input())

    pg.mixer.music.play()
    if s == 'p':

        pg.mixer.music.unpause()

    elif s == 's':
        pg.mixer.music.pause()
    elif s == 'n':
        i +=1
        pg.mixer.music.load(songs[i])
        pg.mixer.music.play()
    elif s == 'pr':
        i -= 1
        pg.mixer.music.load(songs[i])
        pg.mixer.music.play()
    elif s == 'c':
        playing = False















