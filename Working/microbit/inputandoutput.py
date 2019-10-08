from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.SURPRISED)
    else:
        display.show(Image.SNAKE)