from machine import Pin, PWM
from utime import sleep

#The pwm0 object is the continuous rotation servo
pwm0 = PWM(Pin(28), freq=50, duty_u16=0)
pwm0.duty_u16()

#Testing suggests 4800 is the stop point for the continuous rotation servo
cycleStop = 4800

#The servo object is the 180 degree position servo
servo = machine.PWM(machine.Pin(15))
servo.freq(50)

#First hall effect sensor for blinds position
hallSense = Pin(16, Pin.IN, Pin.PULL_UP)

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
            
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    pin.duty_u16(duty)


#run the two servos
servo_write(servo,15)
sleep(1)
pwm0.duty_u16(2000)
sleep(1)
while hallSense.value() == 1:
    pwm0.duty_u16(4900)
sleep(1)
pwm0.duty_u16(8090)
sleep(1)
pwm0.duty_u16(2158)
slowToStop()
servo_write(servo,90)
sleep(0.2)
servo.deinit()


