'''
This is a good script for a continuous servo
Change the Pin to whatever you plug into.  Feel free to run
the servo on a 5v and the signal pin to a PWM pin (must share
ground)
'''

from machine import Pin, PWM
from utime import sleep

pwm0 = PWM(Pin(28), freq=50, duty_u16=0)

pwm0.duty_u16()
cycleStop = 4800

#duty_u16(2000) appears to be top speed going clockwise
#duty_u16(4800) stops it
#duty_u16(8000) appears to be top speed going counter clockwise

def slowToStop():
    currentCycle = pwm0.duty_u16()
    
    while currentCycle != cycleStop: #4900:
        if currentCycle > cycleStop: #4900:
            if currentCycle - cycleStop < 100:
                currentCycle = cycleStop
            else:
                currentCycle = currentCycle - 100
            pwm0.duty_u16(currentCycle)
            sleep(0.02)
        elif currentCycle < cycleStop:
            if cycleStop - currentCycle < 100:
                currentCycle = cycleStop
            else:
                currentCycle = currentCycle + 100
            pwm0.duty_u16(currentCycle)
            sleep(0.02)
            
        
iter = start
pwm0.duty_u16(2000)
sleep(1)
pwm0.duty_u16(4900)
sleep(1)
pwm0.duty_u16(8090)
sleep(1)
pwm0.duty_u16(2158)
slowToStop()
print(pwm0.duty_u16())

