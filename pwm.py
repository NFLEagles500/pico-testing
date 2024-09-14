'''
PWM Example on raspberry pico.  There are up to 8 different pwm
devices.  Set each starting with 0 and ending at 7.  The Pin
value is whatever pwm compatible GPIO pin you are setting.

Once you have created your pwm variable, you can set the
pwm using {variable}.set().  The value can be between -1 (off)
up to 65535 (fully on).
'''

from machine import Pin, RTC
from pwm import PIOPWM
import time

def pwm_device(stateMachineId,Pin):
    print(f'Setting pwm for StateMachine: {stateMachineId}, on Pin: {Pin}')
    return PIOPWM(stateMachineId, Pin, max_count=(1 << 16) - 1, count_freq=10_000_000)

pump = pwm_device(7,15) #The first value is the pwm channel, the second value is the GPIO pin
pump.set(-1) # turns the device off
pump.set(65535) # turns the device on 100%
