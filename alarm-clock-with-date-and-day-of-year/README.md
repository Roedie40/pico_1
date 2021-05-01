# Real Time Clock with Daylight Saving Time, alarm, date and day of year  #
(for EU member states) 

**Simple Driver for the DS3231 and the basic for manual-setup.py.**      
Written by Rodrigo Nascimento. (https://github.com/rodrigocmn)   
ds3231_i2c.py   
manual-setup.py

**How to setup the RTC.**     
only on the first run uncomment the two lines below to set time in manual-setup.py.  
current_time = b'\x38\x09\x12\x07\x14\x03\x21' # sec min hour weekday day month year   
ds.set_time(current_time)

-------------------------------------------------------------------------------------
**Drivers:**  
ds3231_i2c.py RTC  
tm1637.py     Display  

-------------------------------------------------------------------------------------
**Other files:**   
main.py    
dayofyear.py    
alarm.txt (saved alarm time)   
rpi-pico_alarm_clock.pdf (fritzing chart)   
    
-------------------------------------------------------------------------------------
**How to use the alarm clock**
In time mode
button1 set alarm
button2 day and month
buttun3 day of year
button4 alarm off (if it was on)


In set alarm mode
button2 setting hours
button3 setting minutes
button4 set alarm on/off (see led onboard)



