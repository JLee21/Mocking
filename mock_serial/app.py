# app.py

# A module that creates strings that is sent via SerialConnection

from myserial import SerialConnection

class MyApp():

    global ser
    ser = SerialConnection()

    def __init__(self):
        pass

    @ser.decorator
    def myfunc(self):
        return 'testing1234'
