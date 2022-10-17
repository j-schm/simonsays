from adafruit_circuitplayground import cp
import time

Red = (255, 0, 0)
Orange = (255, 128, 0)
Yellow = (255, 255, 0)
Green = (0, 255, 0)
LightGreen = (0, 255, 127)
LightBlue = (0, 255, 255)
Blue = (0, 0, 255)
Purple = (127, 0, 255)
Magenta = (255, 0, 255)
Pink = (255, 0, 127)
White = (255, 255, 255)
Black = (0, 0, 0)

Group0 = {"lednums": (5, 6, 7), "color": Blue, "tone": 209}
Group1 = {"lednums": (7, 8, 9), "color": Red, "tone": 310}
Group2 = {"lednums": (0, 1, 2), "color": Green, "tone": 415}
Group3 = {"lednums": (2, 3, 4), "color": Yellow, "tone": 252}


def press_button(button):
    if button == 0:
        cp.pixels[5] = Green
        cp.pixels[6] = Blue
        cp.pixels[7] = Blue
        cp.play_tone(209, 0.5)
    elif button == 1:
        cp.pixels[7] = Red
        cp.pixels[8] = Red
        cp.pixels[9] = Red
        cp.play_tone(310, 0.5)
    elif button == 2:
        cp.pixels[0] = Green
        cp.pixels[1] = Green
        cp.pixels[2] = Green
        cp.play_tone(415, 0.5)
    elif button == 3:
        cp.pixels[0] = Red
        cp.play_tone(209, 0.05)
        time.sleep(0.05)
        cp.pixels[1] = Orange
        cp.play_tone(233, 0.05)
        time.sleep(0.05)
        cp.pixels[2] = Yellow
        cp.play_tone(257, 0.05)
        time.sleep(0.05)
        cp.pixels[3] = Green
        cp.play_tone(281, 0.05)
        time.sleep(0.05)
        cp.pixels[4] = LightGreen
        cp.play_tone(305, 0.05)
        time.sleep(0.05)
        cp.pixels[5] = LightBlue
        cp.play_tone(329, 0.05)
        time.sleep(0.05)
        cp.pixels[6] = Blue
        cp.play_tone(353, 0.05)
        time.sleep(0.05)
        cp.pixels[7] = Purple
        cp.play_tone(377, 0.05)
        time.sleep(0.05)
        cp.pixels[8] = Magenta
        cp.play_tone(401, 0.05)
        time.sleep(0.05)
        cp.pixels[9] = Pink
        cp.play_tone(415, 0.05)
        time.sleep(0.05)
        cp.pixels.fill(Black)
        cp.stop_tone()


while True:
    if cp.touch_A1:
        press_button(0)
    if cp.touch_A2 or cp.touch_A3:
        press_button(1)
    if cp.touch_A4 or cp.touch_A5:
        press_button(2)
    if cp.touch_A6:
        press_button(3)

count = 0
while count < 10:
    value = random.randint(0, 3)
    print(value)

    count += 1


# define simon says logic
#       start with sequence
#           how long? 10... set count to 0, while count < 10
#

def win():
    cp.pixels[0] = Red
    cp.play_tone(209, 0.05)
    time.sleep(0.05)
    cp.pixels[1] = Orange
    cp.play_tone(233, 0.05)
    time.sleep(0.05)
    cp.pixels[2] = Yellow
    cp.play_tone(257, 0.05)
    time.sleep(0.05)
    cp.pixels[3] = Green
    cp.play_tone(281, 0.05)
    time.sleep(0.05)
    cp.pixels[4] = LightGreen
    cp.play_tone(305, 0.05)
    time.sleep(0.05)
    cp.pixels[5] = LightBlue
    cp.play_tone(329, 0.05)
    time.sleep(0.05)
    cp.pixels[6] = Blue
    cp.play_tone(353, 0.05)
    time.sleep(0.05)
    cp.pixels[7] = Purple
    cp.play_tone(377, 0.05)
    time.sleep(0.05)
    cp.pixels[8] = Magenta
    cp.play_tone(401, 0.05)
    time.sleep(0.05)
    cp.pixels[9] = Pink
    cp.play_tone(415, 0.05)
    time.sleep(0.05)
    cp.pixels.fill(Black)
    cp.stop_tone()
