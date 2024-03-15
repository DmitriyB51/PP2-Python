from pygame import mixer


mixer.init()


mixer.music.load(r"C:\Users\OmeN_HP\Downloads\FinikFinya_ALEKS_ATAMAN_-_Snezhinki_73461611.mp3")


mixer.music.set_volume(0.7)


mixer.music.play()


while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")

    if query == 'p':


        mixer.music.pause()
    elif query == 'r':


        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break

