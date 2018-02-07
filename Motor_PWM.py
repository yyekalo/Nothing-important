# Untitled - By: yikealo - Sun Feb 4 2018

from pyb import Pin, Timer
import pyb

s = pyb.Servo(2)
INB = pyb.Pin("P3",pyb.Pin.OUT_PP)
INA = pyb.Pin("P4",pyb.Pin.OUT_PP)
INA.high()
INB.low()

p = Pin('P5')
Motor_Timer = Timer(2,freq=1000)
ch = Motor_Timer.channel(4,Timer.PWM, pin=p)
#ch.pulse_width_percent(50)
temp = 12
s.angle(0)
#pyb.delay(5000)
s.angle(40)
ch.pulse_width_percent(temp)
pyb.delay(5000)
ch.pulse_width_percent(0)
INA.low()
INB.high()
s.angle(-40)
ch.pulse_width_percent(temp)
pyb.delay(5000)
ch.pulse_width_percent(0)


