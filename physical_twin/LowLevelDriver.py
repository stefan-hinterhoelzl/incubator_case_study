from gpiozero import OutputDevice


class LowLevelDriver:
    heaterState
    fanState

    def __init__(self):
        global heaterState
        heaterState = "OFF"
        global fanState
        fanState = "OFF"

    def heaterON():
        heater = OutputDevice(27)
        global heaterState
        if (heaterState == "OFF"):
            heater.on()
            heaterState = "ON"

    def heaterOFF():
        heater = OutputDevice(27)
        global heaterState
        if (heaterState == "ON"):
            heater.off()
            heaterState = "OFF"

    def fanON():
        fan = OutputDevice(17)
        global fanState
        if (fanState == "OFF"):
            fan.on()
            fanState = "ON"

    def fanOFF():
        fan = OutputDevice(17)
        global fanState
        if (fanState == "ON"):
            fan.off()
            fanState = "OFF"

    def getHeaterState():
        return heaterState

    def getFanState():
        return fanState

