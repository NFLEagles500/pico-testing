'''
Example of using the Pico to control a stepper motor through a 4 pin controller
'''

from machine import Pin
from utime import sleep
# Define the pin and set it to input mode
stepper_pins = [Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT), Pin(13, Pin.OUT)] #Pins to activate stepper motor

def step(direction, steps, delay):
    # Use the global step_index variable so that it can be modified by this function
    global step_index
    global stepsPosition
    # Loop through the specified number of steps in the specified direction
    for i in range(steps):
        if stepsPosition == 'unknown':
            # Add the specified direction to the current step index to get the new step index
            step_index = (step_index + direction) % len(step_sequence)
            # Loop through each pin in the motor
            for pin_index in range(len(stepper_pins)):
                # Get the value for this pin from the step sequence using the current step index
                pin_value = step_sequence[step_index][pin_index] 
                # Set the pin to this value
                stepper_pins[pin_index].value(pin_value)
            # Delay for the specified amount of time before taking the next step
            sleep(delay)
        elif stepsPosition >= 0:
            # Add the specified direction to the current step index to get the new step index
            step_index = (step_index + direction) % len(step_sequence)
            # Loop through each pin in the motor
            for pin_index in range(len(stepper_pins)):
                # Get the value for this pin from the step sequence using the current step index
                pin_value = step_sequence[step_index][pin_index] 
                # Set the pin to this value
                stepper_pins[pin_index].value(pin_value)
            stepsPosition = stepsPosition + direction
            # Delay for the specified amount of time before taking the next step
            sleep(delay)

stepsPosition = 'unknown'
step_index = 0
step_speed = 0.005
# Define the sequence of steps for the motor to take
step_sequence = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
]
#A full rotation is 2048 steps
step(1, 2048, 0.05)
