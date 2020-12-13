from subprocess import Popen, PIPE, STDOUT
import pty
import os

import RPi.GPIO as GPIO

from api_wrapper import APIWrapper
from config import Config
from lcd import Adafruit_CharLCD

cmd = '/home/pi/EasySwing/reader/nfcDemoApp poll'

print('starting')

master, slave = pty.openpty()

p = Popen(cmd, shell=True, stdin=PIPE, stdout=slave, stderr=slave, close_fds=True)
stdout = os.fdopen(master)

line = stdout.readline()

while line:
    # boot screen
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(12, GPIO.OUT)
    GPIO.output(12, GPIO.HIGH)

    if "Type" in stdout.readline():
        l = stdout.readline().replace(' ','').replace("'", '').replace('NFCID1:', '').replace(':','')
        tag_uuid  = ''.join(l.split())
        print(tag_uuid)
        api = APIWrapper(Config)
        user = api.sign_in(tag_uuid)

        if user:
            print(user.get('first_name'))
            print(user.get('last_name'))
            for club in user.get('clubs'):
                print(f'{club.get("name")} - {club.get("tee_height")}mm')

            lcd = Adafruit_CharLCD()
            lcd.clear()
            lcd.message(user.get('first_name') + '\n' + user.get('last_name'))

        else:
            print('User not found')
        print('\n')
