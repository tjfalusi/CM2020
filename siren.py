# Add your Python code here. E.g.
from microbit import *
import music

tune = ['F#4:6','R1','D#4:6','R3','B4:4','F#4:4','E4:4', 'R1', 'G#4:2', 'B4:1', 'R1', 'B4:2', 'B4:1', 'R1', 'G#4:2',
        'B4:1', 'R1', 'B4:2', 'B4:1', 'R1', 'B4:4','F#4:4','B4:4','R1','G#4:2','B4:2', 'B4:2', 'B4:2', 'G#4:2',
        'B4:2', 'B4:2', 'C#5:4', 'B4:4', 'B4:4', 'F#4:4', 'E4:4', 'R1', 'G#4:1', 'R1', 'B4:2', 'B4:1', 'R1', 'B4:2',
        'G#4:1', 'R1', 'B4:2', 'B4:1', 'R1', 'B4:3']





music.set_tempo(ticks=4, bpm = 125)
while True:
    if button_a.was_pressed():
        music.play(tune)
    if button_b.was_pressed():
        music.stop()
