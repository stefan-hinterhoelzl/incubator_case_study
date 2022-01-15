from email.errors import FirstHeaderLineIsContinuationDefect


heaterState = ""
fanState = ""

def init():
    global heaterState
    global fanState

    heaterState = "OFF"
    fanState = "OFF"



