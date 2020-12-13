import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
green_light = 11
yellow_light = 13
red_light = 15
PIN_button = 37
GPIO.setup(green_light, GPIO.OUT)
GPIO.setup(red_light, GPIO.OUT)
GPIO.setup(yellow_light, GPIO.OUT)
GPIO.setup(PIN_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def test_call(channel):
    print("Event detected")
    GPIO.output(red_light, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(red_light, GPIO.LOW)
GPIO.add_event_detect(PIN_button, GPIO.FALLING, callback=test_call)

button = GPIO.input(PIN_button)
try:
    while True:
        GPIO.input(green_light, GPIO.LOW)
        GPIO.input(red_light, GPIO.HIGH)
        if not button :
            while True:
                GPIO.input(red_light, GPIO.LOW)
                GPIO.input(yellow_light, GPIO.HIGH)
                if button:
                    break
            while True:
                GPIO.input(yellow_light, GPIO.LOW)
                GPIO.input(green_light, GPIO.HIGH)
                if not button:
                    button = not button
                    break


except KeyboardInterrupt:
    GPIO.cleanup()