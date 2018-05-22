# myserial.py

# A module to write and read to a serial/UART buffer

from functools import wraps
import serial

class SerialConnection():

        def __init__(self):
            """ Initilize the Serial instance. """

            self.ser = serial.Serial(port=2, baudrate=9600)

        def decorator(self, func):
            @wraps(func)
            def wrapper_func(*args):
                return func(*args)
            return wrapper_func
