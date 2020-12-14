import requests
import os
# import Rpi.GPIO as gpio

ec2 = os.getenv("LIGHT_EC2")

# blue_pin = 23
# red_pin = 24


# gpio.setmode(gpio.BCM)
# gpio.setup(blue_pin, gpio.OUT)
# gpio.setup(red_pin, gpio.OUT)

def get_lights():
    
    r = requests.get(ec2)
    print(r.status_code)
    r_json = r.json()
    blue = r_json[1]['active']
    red = r_json[2]['active']
    green = r_json[3]['active']
    yellow = r_json[4]['active']

    if(blue):
        print("Blue is active")
        gpio.output(blue_pin, gpio.HIGH)
    else:
        print("Blue is inactive")
        gpio.output(blue_pin, gpio.LOW)


    if(red):
        print("Red is active")
        gpio.output(red_pin, gpio.HIGH)
    else:
        print("Red is inactive")
        gpio.output(blue_pin, gpio.LOW)





if __name__ == "__main__":
    get_lights()