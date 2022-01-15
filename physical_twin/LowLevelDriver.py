from gpiozero import OutputDevice

heater = OutputDevice(27)
fan = OutputDevice(17)

def heaterON():
    heater.on()
       

def heaterOFF():
    heater.off()
       
def fanON():
    fan.on()
        

def fanOFF():
    fan.off()


