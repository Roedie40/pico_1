# Alarm clock with date and day of year  #
(for EU member states) 

**Simple Driver for the DS3231 and the basic for manual-setup.py.**      
Written by Rodrigo Nascimento. (https://github.com/rodrigocmn)   
ds3231_i2c.py   
Setup_RCT-DC3231.py

**How to use.**     
only on the first run uncomment the two lines below to set time in manual-setup.py.  
current_time = b'\x38\x09\x12\x07\x14\x03\x21' # sec min hour weekday day month year   
ds.set_time(current_time)

-------------------------------------------------------------------------------------
**Drivers:**  
ds3231_i2c.py RTC  
tm1637.py     Display  
alarm.txt (needed for save alarm time)

-------------------------------------------------------------------------------------
**How do the buttons work**  

in time mode
button1 go to alarm time mode
button2 gives day and month
button3 day of the year
button4 set alarm off

in alarm time mode
button1 go to time mode
button2 set alarm hours
button3 set alarm minutes
button4 alarm on/off (led on pico-board)


