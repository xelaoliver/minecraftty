# Alex Oliver 2025
# Program that captures an area on the screen, converts it into text and displays on a terminal

from PIL import ImageGrab
from math import floor
from time import sleep
from os import system

# setup window capture variables
screen = {
    "captureWidth": 640, "captureHeight": 480, "resolution": 7, "screenWidth": ImageGrab.grab().size[0], "screenHeight": ImageGrab.grab().size[1]
}

GRADIENT = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'. "
ESCAPE = "\033[0m"

print("\033[?25l", end="") # hide cursor

while 1:
    # output buffer
    screenBuffer = []

    # get pixel colour of capture area
    image = ImageGrab.grab()
    px = image.load()
    for y in range(0, screen["captureHeight"], screen["resolution"]):
        line = ""

        for x in range(0, screen["captureWidth"], floor(screen["resolution"]/1.75)):
            # get pixel colour: colour = (r, g, b)
            colour = px[
                (screen["screenWidth"]/2)-(screen["captureWidth"]/2)+x, (screen["screenHeight"]/2)-(screen["captureHeight"]/2)+y
            ]

            greyscale = (colour[0]*.299)+(colour[1]*.587)+(colour[2]*.114) # or just find the mean
            greyscale = (greyscale*len(GRADIENT))//255
            greyscale = min(max(0, floor(greyscale)), len(GRADIENT)-1)
            character = GRADIENT[int(len(GRADIENT)-1-floor(greyscale))]

            line += f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m{character}{ESCAPE}"
        
        # new output buffer line
        screenBuffer.append(line)
    
    print("\033[H", end="")

    for y in range(len(screenBuffer)):
        print(screenBuffer[y])
        
    sleep(.003)

