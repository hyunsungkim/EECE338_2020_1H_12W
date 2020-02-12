import RPi.GPIO as GPIO
import time

#set pin map as BCM setting
GPIO.setmode(GPIO.BCM)

#set GPIO18 pin as output
GPIO.setup(18, GPIO.OUT)

#set GPIO pin as PWM output with freq 1kHz
myPwm = GPIO.PWM(18, 1000)

#Change PWM frequency to 2kHz
#myPwm.ChangeFrequency(2000)

#enable pwm output with duty ratio 50% 
myPwm.start(50)

print("PWM output enabled for 5 seconds")

#remain PWM on for 5 seconds
start = time.time()
while (time.time()-start) < 5:
	continue

#terminate the program
myPwm.stop()
GPIO.cleanup()
