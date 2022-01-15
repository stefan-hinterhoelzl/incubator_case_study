from gpiozero import OutputDevice

heaterState = "OFF"
fanState = "OFF"

heater = OutputDevice(27)
fan = OutputDevice(17)

def heaterON():
    global heaterState
    if (heaterState == "OFF"):
        heater.on()
        heaterState = "ON"

def heaterOFF():
    global heaterState
    if (heaterState == "ON"):
        heater.off()
        heaterState = "OFF"

def fanON():
    global fanState
    if (fanState == "OFF"):
        fan.on()
        fanState = "ON"

def fanOFF():
    global fanState
    if (fanState == "ON"):
        fan.off()
        fanState = "OFF"


