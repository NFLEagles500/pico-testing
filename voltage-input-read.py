'''
This is how I used an ADC (analog to digital pin) along with a voltage divider
circuit to estimate the voltage of the 4 AA NiMH cells in series.  I was testing
microcontroller sleeping to see how long the batteries might last using various
sleep modes and controllers.  In this example, I was using a Pico W
'''

from machine import Pin
from utime import sleep

# Define variables
voltage_battery = 5.4  # Battery voltage in volts when fully charged
#Need to divide the voltage, so the microcontroller Pin.IN will NOT be
#exposed to a voltage higher than 3.3.
voltage_adc_max = 3.3  # Maximum ADC input voltage in volts
#Before testing the pin in the voltage divider I used my voltmeter to make sure it
#wasn't higher
voltage_adc = 1.76  # Actual ADC voltage in volts (measured with voltmeter)
#Resistor 1 was going from 5.4v + to the voltage reading Pin
resistor_1 = 10000  # Resistor 1 value in ohms
#Resistor 2 was going from the voltage reading Pin to Ground
resistor_2 = 5000  # Resistor 2 value in ohms
voltage_warn = 4.4  # Warning voltage level in volts
adc_warn = 29300
oneVolt = 19859
# Calculate actual voltage based on voltage divider formula
actual_voltage = voltage_battery * resistor_2 / (resistor_1 + resistor_2)

# Calculate ADC reading at warning voltage
adc_warn = voltage_warn * (resistor_1 + resistor_2) / resistor_2

#This is the ADC pin I used to read to voltage between resistor 1 and 2
battery_adc = machine.ADC(28) #Was using this in a voltage divider to read NiMH batt voltage
buzzer = machine.PWM(machine.Pin(15)) #Added a buzzer to chime when voltage was low enough to warrant a charge

#Reading the adc value.  _u16 returns a 16 bit address meaning a number between
# 0 and 65535.  0 would be 0 volts and 65535 would be 3.3 volts
readVoltage = battery_adc.read_u16()
#Tried to calculate the correct return value to print and/or log
actual_voltage = (readVoltage / oneVolt) * (resistor_1 + resistor_2) / resistor_2
logVoltage = f'Actual voltage = {actual_voltage:.2f}'
with open('log.txt','a') as file:
    file.write(f"{logVoltage}\n")
if readVoltage < adc_warn:
    buzzer.freq(262)
    buzzer.duty_u16(30000)
    sleep(2)
    buzzer.duty_u16(0)
    with open('log.txt','a') as file:
        file.write(f"Time to charge {actual_voltage:.2f}\n")
