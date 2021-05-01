from machine import I2C, Pin, PWM
# Import the DS3231_I2C class from ds3231_i2c (This is light driver with limited functionalities)
from ds3231_i2c import DS3231_I2C
import tm1637
from utime import sleep
import dayofyear

# Pin setup
mydisplay = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

buzzer = PWM(Pin(18))

led1 = Pin(25, Pin.OUT)
led1.value(0)

button1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(11, Pin.IN, Pin.PULL_DOWN)
button4 = Pin(10, Pin.IN, Pin.PULL_DOWN)



alarm = False
done = False
alarm_file = open('alarm.txt', 'r')
alarm_time = alarm_file.read()
global alarm_hr
global alarm_min
alarm_hr = int(alarm_time[:2])
alarm_min = int(alarm_time[2:])


# Set DS I2C ID, SDA, SCL respective pins and uses default frequency (freq=400000)
ds_i2c = I2C(0,sda=Pin(12), scl=Pin(13))
print("RTC I2C Address : " + hex(ds_i2c.scan()[0]).upper()) # Print the I2C device address in the command line
print("RTC I2C Configuration: " + str(ds_i2c))              # Display the basic parameters of I2C device in the command line
ds = DS3231_I2C(ds_i2c)

def alarm_signal():
    tones = [659,831,880,659,831,988]
     
    for tone in tones:
        print(tone)
        buzzer.duty_u16(1000)
        buzzer.freq(tone)
        sleep(0.3)
        buzzer.duty_u16(0)
        
def give_dayofyear():
    date = "20%02r %02s %02d" %(yr, month, day)
    #print(dayofyear.dayofyear(date))
    daynr = dayofyear.dayofyear(date)
    print(daynr)
    #mydisplay.numbers(hr, min, colon=False)
    mydisplay.number(daynr)
    sleep(1.5)
    
def give_date():
    
    print('{:02}'.format(day),"-",'{:02}'.format(month),"-20",'{:02}'.format(yr),sep='')
    mydisplay.numbers(day, month, colon=False)
    sleep(1.5)
    
def go_alarm():
    global alarm_hr
    global alarm_min
    global done
    global alarm
    #print("real time",hr,min)
    #print("alarm time", alarm_hr,alarm_min)
    print("real time",'{:02}'.format(hr),'{:02}'.format(min)) 
    print("alarm time",'{:02}'.format(alarm_hr),'{:02}'.format(alarm_min)) 
    if hr == alarm_hr and min == alarm_min:
        alarm_signal()
        done = True
    if (done == True) and (hr != alarm_hr or min != alarm_min):      
        done = False
        alarm = False
        led1.value(0)
    return

def set_alarm():
    global alarm
    global alarm_hr
    global alarm_min
    alarm_file = open('alarm.txt', 'r')
    alarm_time = alarm_file.read()
    
    alarm_hr = int(alarm_time[:2])
    
    alarm_min = int(alarm_time[2:])
    mydisplay.numbers(alarm_hr, alarm_min, colon=False)
    sleep(1)
    #print(alarm_hr + ':' + alarm_min)
    while True:
        mydisplay.numbers(alarm_hr, alarm_min, colon=False)
        sleep(0.5)
        if button1.value() == 1:
            print("button1_al")
            break
        if button2.value() == 1:
            global alarm_hr
            alarm_hr = alarm_hr + 1
            if alarm_hr > 24:
                alarm_hr = 00
                print("button2_al")
        if button3.value() == 1:
            global alarm_min
            alarm_min = alarm_min + 1
            if alarm_min > 59:
                alarm_min = 00
                print("button3_al")
        if button4.value() == 1:
            print("button4_al")
            alarm_file = open('alarm.txt', 'w')
            alarm_file.write('{:02}'.format(alarm_hr))
            alarm_file.write('{:02}'.format(alarm_min))
            alarm_file.close()
           
            if alarm == True:
                alarm = False
                led1.value(0)
            else:
                alarm = True
                led1.value(1)
                sleep(2)
            return



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
 
while True:
    # Retrun current time in hex
    t = ds.read_time()
    # Split time into decimal
    hr=(int(Hex2Digit(t[2])))
    min=(int(Hex2Digit(t[1])))
    sec=(int(Hex2Digit(t[0])))
    day=(int(Hex2Digit(t[4])))
    month=(int(Hex2Digit(t[5])))
    dow=(int(Hex2Digit(t[3])))
    yr=(int(Hex2Digit(t[6])))
    # See if it's daylight saving time 
    dst=DST()
    if dst == True:
        hr = hr + 1
    # a small correction ;)
    if hr == 24:
        hr = 00
         
    if alarm == True:
        print(alarm)
        print('alarm on')
        go_alarm()    
    else:
        print('alarm off')
       
    # Time display with blinking colon
    mydisplay.brightness(7)
    mydisplay.numbers(hr, min, colon=True)
    sleep(1)
    mydisplay.numbers(hr, min, colon=False)
    sleep(1)
    
    if button1.value() == 1:
        print("Set alarm")
        set_alarm()
    if button2.value() == 1:
        print("Give day and month")
        give_date()
    if button3.value() == 1:
        print("Day of year")
        give_dayofyear()
    if button4.value() == 1:
        print("Set alarm off")
        alarm
        alarm = False
        led1.value(0)
        