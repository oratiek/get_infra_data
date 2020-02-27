import picamera
import os
import time
import sys

def ver1():
    interval = int(sys.argv[1])
    filenum = 0
    while True:
        with picamera.PiCamera as camera:
            filename = "image_data/" + str(filenum) + ".jpg"
            camera.capture(filename)
            camera.start_preview()
            time.sleep(interval)
            camera.stop_preview()
            print(filename)
            filenum += 1

ver1()
