# app.py

# A module that creates strings that is sent via SerialConnection

from myserial import SerialConnection

class MyApp():

    ser = SerialConnection()

    def __init__(self):
        print(self.myfunc())

    @ser.decorator
    def myfunc(self):
        return 'testing1234'
