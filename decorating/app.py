class MySerial():
    def __init__(self):
        pass # I have to have an __init__
    def write(self):
        pass # write to buffer
    def read(self):
        pass # read to buffer
    def decorator(self, func):
        def func_wrap(*args, **kwargs):
            self.write(func(*args, **kwars))
            return self.read()
        return func_wrap

class App():
    def __init__(self):
        self.ser = MySerial()

    @self.ser.decorator  # <-- does not work here.
    def myfunc(self):
        return 'yummy bytes that are written to Serail buffer'

if __name__ == '__main__':
    app = App()
