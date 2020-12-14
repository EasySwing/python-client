from api_wrapper import APIWrapper
from config import Config

import Adafruit_BBIO.GPIO as GPIO
import time

api = APIWrapper(Config)
tag_uuid = '2b2f48c2-74e6-4d6b-98c1-111630bfa7ae'
user = api.sign_in(tag_uuid)

name_length = len(user.get('first_name'))

out = "P8_8"
GPIO.setup(out, GPIO.OUT)

print(name_length, user.get('first_name'))

for i in range(0, name_length):
    GPIO.output(out, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(out, GPIO.LOW)
    time.sleep(0.1)


# print(user.get('last_name'))

# for club in user.get('clubs'):
#     print(club.get("name"), club.get("tee_height"), 'mm')
