#!/usr/bin/env python
import time
import os
from trackball import TrackBall

print("""Trackball: Mouse

Use the trackball as a mouse in Raspbian, with right-click
when the switch is pressed.

Press Ctrl+C to exit!
""")

trackball = TrackBall(interrupt_pin=4)
trackball.set_rgbw(0, 0, 0, 0)

# Check for xte (used to control mouse)
use_xte = os.system('which xte') == 0

while True:
    up, down, left, right, switch, state = trackball.read()

    # Send movements and clicks to xte
    if use_xte:
        if switch:
            cmd = 'xte "mouseclick 1"'
            os.system(cmd)
        elif right or up or left or down:
            x = right - left
            x = math.copysign(x**2, x)
            y = down - up
            y = math.copysign(y**2, y)
            cmd = 'xte "mousermove {} {}"'.format(x, y)
            os.system(cmd)
    else:
        print('xte not found')

    time.sleep(0.0001)
