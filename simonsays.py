from adafruit_circuitplayground import cp
import time
import random

Red = (255, 0, 0,)
Orange = (255, 125, 0)
Yellow = (125, 125, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Black = (0, 0, 0)

def press_button(button):
    if button == 0:
        cp.pixels[7] = Red
        cp.pixels[8] = Red
        cp.pixels[9] = Red
        cp.play_tone = (310, 0.35)
    elif button == 1:
        cp.pixels[5] = Blue
        cp.pixels[6] = Blue
        cp.pixels[7] = Blue
        cp.play_tone = (209, 0.35)
    elif button == 2:
        cp.pixels[0] = Green
        cp.pixels[1] = Green
        cp.pixels[2] = Green
        cp.play_tone = (415, 0.35)
    elif button == 3:
        cp.pixels[2] = Yellow
        cp.pixels[3] = Yellow
        cp.pixels[4] = Yellow
        cp.play_tone = (252, 0.35)
    cp.pixels.fill(Black)


def play_button():
    while button is None:
        if cp.touch_A3 or cp.touch_A2:
            press_button(0)
            button = 0
        elif cp.touch_A1:
            press_button(1)
            button = 1
        elif cp.touch_A4 or cp.touch_A5:
            press_button(2)
            button = 2
        elif cp.touch_A6:
            press_button(3)
            button = 3



def play_sequence(round):
    for step in range(round):
        press_button(sequence[step])


count = 0


def lose():
    cp.pixels.fill(Red)
    time.sleep(0.25)
    cp.pixels.fill(Black)
    time.sleep(0.25)
    cp.pixels.fill(Red)
    time.sleep(1)
    cp.pixels.fill(Black)


def win():
    cp.pixels[0] = Red
    time.sleep(0.25)
    cp.pixels[1] = Red
    time.sleep(0.25)
    cp.pixels[2] = Orange
    time.sleep(0.25)
    cp.pixels[3] = Orange
    time.sleep(0.25)
    cp.pixels[4] = Yellow
    time.sleep(0.25)
    cp.pixels[5] = Yellow
    time.sleep(0.25)
    cp.pixels[6] = Green
    time.sleep(0.25)
    cp.pixels[7] = Green
    time.sleep(0.25)
    cp.pixels[8] = Blue
    time.sleep(0.25)
    cp.pixels[9] = Blue
    time.sleep(0.25)
    cp.pixels.fill(Black)


round = 0
sequence = [random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3), random.randint(0, 3)]

while True:
    round += 1
    if round > len(sequence):
        win()
        time.sleep(3)
    play_sequence(round)
    step = 0
    while step < round:
        button = None
        play_button()
    time.sleep(0.5)
    if button != sequence(step):
        lose()
        round = 0
    else:
        button = None
        cp.stop_tone()
        cp.pixels.fill(Black)
    step += 1
time.sleep(1)
