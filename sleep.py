'''
Example of sleeping the Raspberry Pico W.
Be sure to use help(machine) to discover available power options
References:
    https://docs.micropython.org/en/latest/rp2/quickref.html
    https://docs.micropython.org/en/latest/library/machine.html#constants
    
As of v1.21 micropython for Raspberry Pico, only machine.lightsleep() and
machine.deepsleep() are available.
NOTE: Thonny is a bit difficult to handle keeping the connection while it
sleeps and wakes, so manipulating an LED and/or logging along with saving the
script as main.py is helpful to successfully test.  In contrast, Thonny handles
the esp32 sleeping much better.  A couple lines down you'll see "wake_reason" is
not available for the Pico, so knowing whether a wake happens due to a hardware
Pin interrupt or clock timer is not available.

NOTE: deepsleep() basically just restarts the device, lightsleep() will run
an interrupt function and continue with whatever code you have after the
lightsleep line.
'''

import time
#Notice that "wake_reason" is commented out.  It is not a function available
# to the Raspberry Pico's
from machine import Pin, deepsleep, lightsleep, reset_cause#, wake_reason

#This only runs when the device is interrupted from a lightsleep
def wake_up(pin):
    #setting handler to '' for debouncing
    pin.irq(trigger=Pin.IRQ_RISING, handler='')
    with open('log.txt','a') as file:
        file.write(f"Running wake_function\n")
    iter = 20
    while iter > 0:
        led.toggle()
        time.sleep(0.2)
        iter = iter - 1
    with open('log.txt','a') as file:
        file.write(f"Finished running wake_function\n")
    #putting the handler back to trigger the function after it runs
    pin.irq(trigger=Pin.IRQ_RISING, handler=wake_up)

#In this example, hardware Pin 16 is used to wake the Pico if it gets a high signal
# This is compatible with both lightsleep() and deepsleep(), but in deepsleep() the
# function will NOT be run, the Pico will simply restart
pin = Pin(16, Pin.IN, Pin.PULL_DOWN)
pin.irq(trigger=Pin.IRQ_RISING, handler=wake_up)

led = Pin('LED',Pin.OUT) #Used the onboard LED to determine what was working

#Used logging to flush out values I'd get 
with open('log.txt','a') as file:
    file.write(f"{reset_cause()}\n")
blink_iter = 10
while blink_iter > 0:
    led.toggle()
    time.sleep(0.2)  # Pause for 0.5 seconds
    blink_iter = blink_iter - 1
led.value(0)

#During lightsleep you can let the 10000 microseconds run, or Pin interrupt
# as noted earlier in the code.
lightsleep(10000)
#If the line above was a deepsleep(10000) the code below would not run, but
# it will in a lightsleep function
with open('log.txt','a') as file:
    file.write(f"Running remaining code after lightsleep\n")
    iter = 20
    while iter > 0:
        led.toggle()
        time.sleep(1)
        iter = iter - 1


