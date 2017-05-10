import RPi.GPIO as GPIO
from time import sleep
import pygame

#initialize  the pygame library
pygame.init()
#set the GPIO pin numbers
#the LEDs(from L to R)
sounds = [ pygame.mixer.sound("explosion-01.wav"),
           pygame.mixer.sound("happy.wav"),]
sounds [i].play()
#wait a bit, then turn the LED off
sleep (1)
