
# Simple Driver for the DS3231 and the basic for manual-setup.py. #  
Written by Rodrigo Nascimento. (https://github.com/rodrigocmn)   
ds3231_i2c.py   
manual-setup.py

# how to use #  
only on the first run uncomment the two lines below to set time in manual-setup.py.  
current_time = b'\x38\x09\x12\x07\x14\x03\x21' # sec min hour weekday day month year   
ds.set_time(current_time)

