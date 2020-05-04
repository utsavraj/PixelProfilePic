#!/usr/bin/env python3

## pip install Pillow

from PIL import Image, ImageDraw
import background_pattern

if __name__ == '__main__':
    # Size of the image
    side = 660
    text = raw_input( "Enter your Given Name and Family Name OR SKIP: ")

    #Creates a square white image of size
    background = Image.new(mode='RGB', size=(side, side), color='#FFF')

    #Creates the pattern on the blank white square
    background_pattern.createPattern(background, side, text, 30)

    background.show()

    #Saves the image as ProfilePic.PNG
    background.save("ProfilePic.PNG") 


