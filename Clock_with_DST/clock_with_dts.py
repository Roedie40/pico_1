from machine import I2C, Pin
# Import the DS3231_I2C class from ds3231_i2c (This is light driver with limited functionalities)
from ds3231_i2c import DS3231_I2C
import tm1637
from utime import sleep

mydisplay = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

# Set DS I2C ID, SDA, SCL respective pins and uses default frequency (freq=400000)
ds_i2c = I2C(0,sda=Pin(12), scl=Pin(13))
print("RTC I2C Address : " + hex(ds_i2c.scan()[0]).upper()) # Print the I2C device address in the command line
print("RTC I2C Configuration: " + str(ds_i2c))              # Display the basic parameters of I2C device in the command line
ds = DS3231_I2C(ds_i2c)

# Daylight Saving Time 
# DST from last sunday of March 02:00
#     to last sunday of October 02:00 
def DST():
    prevsunday = day - dow
    if (month < 3) or (month > 10):
        return False        
    if (month > 3) and (month < 10):
        return True
    if ((month == 3) and (prevsunday >= 25)) and (hr > 1):
        return True
    if (month == 10) and (prevsunday < 25) and (hr < 2):
        return True

# Set hex to digit
def Hex2Digit( number ):
    return '%02x' % number
 
while 1:
    # Retrun current time in hex
    t = ds.read_time()
    # Split time into decimal
    hr=(int(Hex2Digit(t[2])))
    min=(int(Hex2Digit(t[1])))
    sec=(int(Hex2Digit(t[0])))
    day=(int(Hex2Digit(t[4])))
    month=(int(Hex2Digit(t[5])))
    dow=(int(Hex2Digit(t[3])))
    # See if it's daylight saving time 
    dst=DST()
    if dst == True:
        hr = hr + 1
    # a small correction ;)
    if hr == 24:
        hr = 00
    # Time display with blinking colon
    mydisplay.numbers(hr, min, colon=True)
    sleep(1)
    mydisplay.numbers(hr, min, colon=False)
    sleep(1)




