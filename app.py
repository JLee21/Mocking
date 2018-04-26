class Base():
    def __init__(self):
        self.attr = 'original_value'

    def show(self):
        print(self.attr)

class App():
    def __init__(self):
        self.base = Base()
