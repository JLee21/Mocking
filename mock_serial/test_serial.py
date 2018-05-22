# test_serial.py

# This file tests the function "myfunc" from "myapp" class.

# Patch the class and create a instance of the class. (mocked instance)
# Then, add a mock decorator to the mocked instance of the class

from __future__ import print_function

import pytest
import mock
from mock import patch, Mock, MagicMock


@patch('myserial.SerialConnection')
def test_myfunc(mock_class):
    print()

    # I want to mock a Class, but not one of its functions.

    # I can now import MyApp successfuly...
    from app import MyApp

    # ..but I need to bypass the decorator myserial.SerialConnection.decorator
    # do I add a by-pass decorator to the "mock_class"?

    # mock.patch('mock_class.decorator', mock_decorator)

    print('MyApp\n')
    [print(xx) for xx in dir(MyApp)]; print()
    print('MyApp.myfunc\n')
    [print(xx) for xx in dir(MyApp.myfunc)]; print()
    print('MyApp()\n')
    [print(xx) for xx in dir(MyApp())]; print()
    print('MyApp().myfunc')
    print(MyApp().myfunc); print()
    print('MyApp().myfunc()')
    print(MyApp().myfunc()); print()
    print('dir(MyApp().myfunc')
    print(dir(MyApp().myfunc()))



def mock_decorator(*args, **kwargs):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)
        return decorated_function
    return decorator

mock.patch('myserial.SerialConnection.decorator', mock_decorator)



"""
When I import MyApp from app.py, a instance of the SerialConnection class
is created immediately. I want to mock the SerialConnection class but I still
need a function from within this SerialConnection class.
"""
