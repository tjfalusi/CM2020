# Write your code here :-)
from microbit import *
import music
while True:
    #microbit reads input from piano
    #variables p0,p1,p2 relate to pins on microbit
    p0=pin2.read_digital()
    p1=pin8.read_digital()
    p2=pin1.read_digital()
    #nested if:pin is touched play tone
    if p0 or (p1 or p2):
      sleep(10)
      if not p2 and (not p1 and p0):
        music.playTone(262, music.beat(BeatFraction.Half))
      if not p2 and (p1 and not p0):
        music.playTone(294, music.beat(BeatFraction.Half))
      if not p2 and (p1 and p0):
        music.playTone(330, music.beat(BeatFraction.Half))
      if p2 and (not p1 and not p0):
        music.playTone(349, music.beat(BeatFraction.Half))
      if p2 and (not p1 and p0):
        music.playTone(392, music.beat(BeatFraction.Half))
      if p2 and (p1 and not p0):
        music.playTone(440, music.beat(BeatFraction.Half))
      if p2 and (p1 and p0):
        music.playTone(494, music.beat(BeatFraction.Half))