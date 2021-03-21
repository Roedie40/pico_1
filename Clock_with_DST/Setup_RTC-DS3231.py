from machine import I2C, Pin
# Import the DS3231_I2C class from ds3231_i2c (This is light driver with limited functionalities)
from ds3231_i2c import DS3231_I2C 
import utime

# Set DS I2C ID, SDA, SCL respective pins and uses default frequency (freq=400000)
ds_i2c = I2C(0,sda=Pin(12), scl=Pin(13))
print("RTC I2C Address : " + hex(ds_i2c.scan()[0]).upper()) # Print the I2C device address in the command line
print("RTC I2C Configuration: " + str(ds_i2c))              # Display the basic parameters of I2C device in the command line
ds = DS3231_I2C(ds_i2c)


# Uncomment the two lines below to set time.
#current_time = b'\x00\x36\x10\x07\x20\x03\x21' # sec min hour weekday day month year
#ds.set_time(current_time)

# Define the name of week days list
w  = ["Sunday","Monday","Tuesday","Wednesday","Thurday","Friday","Saturday"];

while 1:
    # Retrun current time
    t = ds.read_time()
    print("Time: %02x:%02x:%02x" %(t[2],t[1],t[0]))
    print("Date: %02x/%02x/20%x" %(t[4],t[5],t[6]))
    print("    %s" %(w[t[3]-1]))
    utime.sleep(1)
