# Alarm clock with date and day of year  #
(for EU member states) 

**Simple Driver for the DS3231 and the basic for manual-setup.py.**      
Written by Rodrigo Nascimento. (https://github.com/rodrigocmn)   
ds3231_i2c.py   
Setup_RCT-DC3231.py

**How to use.**     
Only on the first run uncomment the two lines below to set time in manual-setup.py.  
current_time = b'\x38\x09\x12\x07\x14\x03\x21' # sec min hour weekday day month year   
ds.set_time(current_time)

-------------------------------------------------------------------------------------
**Drivers:**  
ds3231_i2c.py RTC  
tm1637.py     Display  
alarm.txt (needed for save alarm time)

-------------------------------------------------------------------------------------
**How do the buttons work**  

In time mode   
Button1 go to alarm time mode  
Button2 gives day and month  
Button3 day of the year  
Button4 set alarm off  

In alarm time mode  
Button1 go to time mode  
Button2 set alarm hours  
Button3 set alarm minutes  
Button4 alarm on/off (led on pico-board) 
