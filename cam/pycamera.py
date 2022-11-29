import sys
import serial
import pygame
import os
import pygame.camera
from sys import argv
from os import getenv
from pygame.locals import*
from datetime import datetime as dt

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640,480))

cam = pygame.camera.Camera("/dev/video0",(640,480))

home_dir = getenv('Home')
range = 300


def capture_image():
    file_name = home_dir + '/image_captured/image_' + str(dt.now()) + '.jpg'
    cam.start()
    image = cam.get_image()
    pygame.image.save(image, file_name)
    cam.stop()

arduino_board  = serial.Serial(sys,argv[1], 9600)

while True:
    if arduino_board.inWaiting() > 0:
        data = arduino_board.readline().strip()

        try:
            data = int(float(data))
            if data <= range:
                capture_image()
                print (data)

        except BaseException as be:
            print (be.message)
        