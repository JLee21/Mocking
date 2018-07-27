from __future__ import print_function

class SerialFLIR():

    def __init__(self):
        print('Initing')
        self.attr = 'Hello'

    @classmethod
    def _decorator(func):
        def magic( self ) :
            print ("start magic")
            func( self )
            print(dir(self))
            print ("end magic")
        return magic

    # _decorator = staticmethod(_decorator)
