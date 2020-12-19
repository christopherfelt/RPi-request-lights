import requests
import os
import RPi.GPIO as gpio
import time

ec2 = os.getenv("LIGHT_EC2")

blue_pin = 23
red_pin = 24
green_pin = 5
yellow_pin = 6


gpio.setmode(gpio.BCM)
gpio.setup(blue_pin, gpio.OUT)
gpio.setup(red_pin, gpio.OUT)
gpio.setup(green_pin, gpio.OUT)
gpio.setup(yellow_pin, gpio.OUT)

def get_lights():

    barbra_sanders = True

    while(barbra_sanders):
        r = requests.get(ec2)
        print(r.status_code)
        r_json = r.json()
        barbra_sanders = r_json[0]['active']
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
            gpio.output(red_pin, gpio.LOW)

        if(green):
            print("green is active")
            gpio.output(green_pin, gpio.HIGH)
        else:
            print("green is inactive")
            gpio.output(green_pin, gpio.LOW)

        if(yellow):
            print("yellow is active")
            gpio.output(yellow_pin, gpio.HIGH)
        else:
            print("yellow is inactive")
            gpio.output(yellow_pin, gpio.LOW)

        time.sleep(5)

    gpio.cleanup()  





if __name__ == "__main__":
    get_lights()