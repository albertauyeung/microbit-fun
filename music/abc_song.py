"""
Play the ABC Song and display A to Z
"""
from microbit import *
import music

tempo = 1.0  # larger is faster

tune = [
    "C4:4", "C4:4", "G4:4", "G4:4", "A4:4", "A4:4", "G4:8",
    "F4:4", "F4:4", "E4:4", "E4:4", "D4:2", "D4:2", "D4:2", "D4:2", "C4:8",
    "G4:4", "G4:4", "F4:8", "E4:4", "E4:4", "D4:8",
    "G4:4", "G4:4", "F4:8", "E4:4", "E4:4", "D4:8",
    "C4:4", "C4:4", "G4:4", "G4:4", "A4:4", "A4:4", "G4:8",
    "F4:4", "F4:4", "E4:4", "E4:4", "D4:4", "D4:4", "C4:8"
]
abcs = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N", "O", "P",
    "Q", "R", "S", "T", "U", "V",
    "W", "W", "X", "Y", "Y", "Z",
    ".", ".", ".", ".", ".", ".", ".",
    ".", ".", ".", ".", ".", ".", "."
]

while True:
    for i in range(len(tune)):
        note, speed = tune[i].split(":")
        speed = int(int(speed) / tempo)
        note = note + ":" + str(speed)
        display.show(abcs[i])
        music.play(note)
    sleep(10000)
