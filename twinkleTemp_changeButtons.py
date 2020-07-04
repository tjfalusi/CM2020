from microbit import *
import music

twinkle = ['C', 'C', 'G', 'G', 'A', 'A', 'G',
            'F', 'F', 'E', 'E', 'D', 'D', 'C',
            'G', 'G', 'F', 'F', 'E', 'E', 'D',
            'C', 'C', 'G', 'G', 'A', 'A', 'G',
            'F', 'F', 'E', 'E', 'D', 'D', 'C']



while True:
    if button_a.is_pressed():
        music.set_tempo()
        music.play(twinkle)

    if button_b.is_pressed():
        music.set_tempo(ticks=4, bpm=240)
        music.play(twinkle)
