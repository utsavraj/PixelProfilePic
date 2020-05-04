'''
LIBRARIES
'''
from PIL import ImageDraw, ImageFont
import random
import os


'''
generateColor
Generates the random colour for the background
    Return: hexcode of a random color 
'''
def generateColor():
    color = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    return color

'''
TexttoInitials
Converts the given Name input into Initials
    Parameter: text or name eg. John Smith
    Return: initials of the name
'''
def TexttoInitials(text):
    name_list = text.split()
    initials = ""
    for name in name_list:  # go through each name
        initials += name[0].upper()  # append the initial
        if (len(initials) == 2 ): #only two Initials
            return initials
    return initials

'''
patternGenerator
Generates the pixelated pattern based on the name given 
    Parameter: temp -  drawable background
               side - dimension of the square background
               pixel_size - size of the pixel on the image that will be colored
               color - color of used for creating the pattern
               text_input - A boolean; If the initials given, it is True
    Return: Creates a pixelated pattern in random on the given background
'''
def patternGenerator(temp,side,pixel_size,color, text_input):
    if(text_input):
        for row in range(0, side,pixel_size) :
            for col in range(0, side, pixel_size):
                if not ( (side//2 - 4*pixel_size < col ) and (side//2 + 4*pixel_size > col) and ( (side//2 - 4*pixel_size < row ) and (side//2 + 4*pixel_size > row))):
                    if (random.random() > 0.5):
                        temp.rectangle([(row,col), (row+pixel_size,col+pixel_size)], fill = color)
    else:
        for row in range(0, side,pixel_size) :
            for col in range(0, side, pixel_size):
                if (random.random() > 0.5):
                    temp.rectangle([(row,col), (row+pixel_size,col+pixel_size)], fill = color)
    return temp

'''
createPattern
Handles the pattern as well the font for our Profile Picture
    Parameter: background -  the blank image used for background
               side - dimension of the square background
               pixel_size - size of the pixel on the image that will be colored
               color - color of used for creating the pattern

    Return: Creates a pixelated pattern in random on the given background with the desired font 
    as well as the initials in the middle of the image if given
'''
def createPattern(background, side, text, pixel_size ):
    color = generateColor()
    cwd = os.getcwd()
    #Tries to loads the pixelated font. If cannot find it, loads any default font 
    try:
        font = ImageFont.truetype(cwd + r'/font/pixelated.ttf', size=pixel_size*7)
    except IOError, e:
        font = ImageFont.load_default()

    temp = ImageDraw.Draw(background)

    text = TexttoInitials(text)
    text_input = True

    # To move the position of the text, change the first two parameter (x, y respectively) of temp.text
    if(len(text) == 2):
        patternGenerator(temp,side,pixel_size,color,text_input)
        temp.text((pixel_size*1.4 + side//2-4*pixel_size, side//2-4*pixel_size), text, align ="center", fill=color , font = font) 
    elif(len(text) == 1):
        patternGenerator(temp,side,pixel_size,color,text_input)
        temp.text((pixel_size*2.8 + side//2-4*pixel_size, side//2-4*pixel_size), text, align ="center", fill=color , font = font)
    else: #No name given
        text_input = False
        patternGenerator(temp,side,pixel_size,color,text_input)
    
    return temp

