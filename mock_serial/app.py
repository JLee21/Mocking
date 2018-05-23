# app.py

# A module that creates strings that is sent via SerialConnection

from myserial import SerialConnection

class MyApp():

    global ser

    def __init__(self):
        ser = SerialConnection()

    @ser.decorator
    def myfunc(self):
        return 'testing1234'
