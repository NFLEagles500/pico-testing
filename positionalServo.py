'''
This is a good script for a 180 degree positional servo
Change the Pin to whatever you plug into.  Feel free to run
the servo on a 5v and the signal pin to a PWM pin (must share
ground)
'''

import machine
import utime

servo = machine.PWM(machine.Pin(15))
servo.freq(50)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    pin.duty_u16(duty)

#while True:
for angle in range(180):
    servo_write(servo,angle)
    utime.sleep_ms(20)
for angle in range(180,-1,-1):
    servo_write(servo,angle)
    utime.sleep_ms(20)

