from machine import Pin
from utime import sleep

x=0.2  # Display time

# Pin setup
on = Pin(25, Pin.OUT)  #      ###a### 
a = Pin(12, Pin.OUT)   #      #     # 
b = Pin(13, Pin.OUT)   #      f     b
c = Pin(14, Pin.OUT)   #      #     #
d = Pin(15, Pin.OUT)   #      ###g###
e = Pin(16, Pin.OUT)   #      #     #
f = Pin(17, Pin.OUT)   #      e     c
g = Pin(18, Pin.OUT)   #      #     #
                       #      ###d###
# all segments off            
digit = [a, b, c, d, e, f, g]
for segment in digit:
    segment.value(1) # segemt off

# onboard led on
on.value(1)

# sequence of numbers to count to nine
ciphers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for cipher in ciphers:
    if cipher == 0: digit = [a, b, c, d, e, f, ]  
    if cipher == 1: digit = [b, c]
    if cipher == 2: digit = [a, b, d, e, g] 
    if cipher == 3: digit = [a, b, c, d, g] 
    if cipher == 4: digit = [b, c, f, g] 
    if cipher == 5: digit = [a, c, d, f, g] 
    if cipher == 6: digit = [c, d, e, f, g] 
    if cipher == 7: digit = [a, b, c]  
    if cipher == 8: digit = [a, b, c, d, e, f, g]
    if cipher == 9: digit = [a, b, c, f, g] 

    for segment in digit:
        segment.value(0) # segment on
        
    # Display time    
    sleep(x)
    
    # all segments off   
    digit = [a, b, c, d, e, f, g]
    for segment in digit:
        segment.value(1) # segment off
        
# onboard led on
on.value(0) 
