from gpiozero import OutputDevice


class LowLevelDriver:
    heaterState = ""
    fanState = ""

    def __init__(self):
        global heaterState
        heaterState = "OFF"
        global fanState
        fanState = "OFF"

    def heaterON(self):
        heater = OutputDevice(27)
        global heaterState
        if (heaterState == "OFF"):
            heater.on()
            heaterState = "ON"

    def heaterOFF(self):
        heater = OutputDevice(27)
        global heaterState
        if (heaterState == "ON"):
            heater.off()
            heaterState = "OFF"

    def fanON(self):
        fan = OutputDevice(17)
        global fanState
        if (fanState == "OFF"):
            fan.on()
            fanState = "ON"

    def fanOFF(self):
        fan = OutputDevice(17)
        global fanState
        if (fanState == "ON"):
            fan.off()
            fanState = "OFF"

    def getHeaterState(self):
        return heaterState

    def getFanState(self):
        return fanState

