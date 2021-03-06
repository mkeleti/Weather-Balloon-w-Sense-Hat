#Sense Hat Sensor Script!
#Made By Michael Keleti
#10 Jan. 2016 
print("Starting Program")
#Importing modules
from sense_hat import SenseHat
import pygame
import time
from pygame.locals import *
from sense_hat import SenseHat
from decimal import Decimal

pygame.init()
pygame.display.set_mode((640, 480))

sense = SenseHat()
sense.clear()

print("Modules Imported")
running = True
#Setting Pixel Colors
r = [255,0,0] #red
o = [255,127,0] #orange
y = [255,255,0] #yellow
g = [0,255,0] #green
b = [0,0,255] #blue
i = [0,0,225] #indigo
v = [159,0,255] #violet
e = [0,0,0] #black(no light)
w = [255,255,255] #white
#This is the main wallpaper
wallpaper = [
e,e,e,y,y,e,e,e,
e,e,y,y,y,y,e,e,
e,i,e,w,w,e,o,e,
i,i,w,w,w,w,o,o,
i,i,w,w,w,w,o,o,
e,i,e,w,w,e,o,e,
e,e,v,v,v,v,e,e,
e,e,e,v,v,e,e,e
]
#Turning off/on animation
off1 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,e,w,w,w,w,e,e,
e,e,e,w,w,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]
off2 = [
e,e,e,e,e,e,e,e,
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,w,w,w,w,w,e,
e,w,w,w,w,w,w,e,
e,e,w,w,w,w,e,e,
e,e,e,w,w,e,e,e,
e,e,e,e,e,e,e,e
]
off3 = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,w,w,w,w,w,e,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
e,w,w,w,w,w,w,e,
e,e,w,w,w,w,e,e,
e,e,e,w,w,e,e,e
]
off = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]
sense.set_pixels(off1)
time.sleep(.1)
sense.set_pixels(off2)
time.sleep(.1)
sense.set_pixels(off3)
time.sleep(.1)
sense.set_pixels(wallpaper)
sense.set_rotation(180)
#Starting the loop
print("Loop Starting")
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
#Collecting key inputs and outputing data from sensors
            if event.key == K_DOWN:
                sense.set_rotation(180)
                sense.show_message("Humidity", scroll_speed=.1, text_colour=y, back_colour=[0,0,0])    
                print("Humidity Selected")
                time.sleep(1)
                dec = Decimal(sense.get_humidity())
                h = round(dec,2)
                for n in range(0,2):
                    sense.show_message("%s" % h, text_colour=y)
            elif event.key == K_UP:
                sense.set_rotation(180)
                sense.show_message("Pressure", scroll_speed=.1, text_colour=v, back_colour=[0,0,0])    
                print("Pressure Selected")
                time.sleep(1)
                dec = Decimal(sense.get_pressure())
                p = round(dec,2)
                for n in range(0,2):
                    sense.show_message("%s" % p, text_colour=v)
            elif event.key == K_RIGHT:
                sense.set_rotation(180)
                sense.show_message("Temperature", scroll_speed=.1, text_colour=i, back_colour=[0,0,0])    
                print("Temperature Selected")
                time.sleep(1)
                dec = Decimal(sense.get_temperature())
                t = round(dec,2)
                for n in range(0,2):
                    sense.show_message("%s" % t, text_colour=i)
            elif event.key == K_LEFT:
                sense.set_rotation(180)
                sense.show_message("Altitude", scroll_speed=.1, text_colour=o, back_colour=[0,0,0])    
                print("Altitude Selected")
                time.sleep(1)
                p = int(sense.get_pressure())
                equa = 44330 * (1-(p/1013.25)**(1/5.2550))
                dec = Decimal(equa)
                print("Altitude Calculated")
                a = round(dec,2)
                sense.show_message("%s Meters" % a, text_colour=o)
                equa2 = equa * 3.2808
                dec = Decimal(equa2)
                a1 = round(dec,2)
                sense.show_message("%s Feet" % a1, text_colour=o)
            elif event.key == K_RETURN:
                running = False
                print("Loop Ending")
                sense.set_rotation(180)
                sense.show_message("BYE ;)", scroll_speed=.05, text_colour=e, back_colour=w)
                sense.set_pixels(off3)
                time.sleep(.1)
                sense.set_pixels(off2)
                time.sleep(.1)
                sense.set_pixels(off1)
                time.sleep(.1)
                sense.set_pixels(off)
                pygame.display.quit()
                pygame.quit()
                print("Loop Ended")
                break


        sense.set_pixels(wallpaper)

