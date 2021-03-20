# Real Time Clock with Daylight Saving Time  #
(for EU member states) 

**Simple Driver for the DS3231 and the basic for manual-setup.py.**      
Written by Rodrigo Nascimento. (https://github.com/rodrigocmn)   
ds3231_i2c.py   
manual-setup.py

**How to use.**     
only on the first run uncomment the two lines below to set time in manual-setup.py.  
current_time = b'\x38\x09\x12\x07\x14\x03\x21' # sec min hour weekday day month year   
ds.set_time(current_time)

-------------------------------------------------------------------------------------
**Simple clock script with DST.**  
Copy clock_with_dts.py to main.py

-------------------------------------------------------------------------------------
**Drivers:**  
ds3231_i2c.py RTC  
tm1637.py     Display  

-------------------------------------------------------------------------------------
**PIN setup**  
for the Real Time Clock DS3231  
sda pin 12  
slc pin 13  
vcc  
gnd  

for the Display TM1637  
clk pin 16  
dio pin 17  





