# Mocking
A repo to hold all python testing exercises.

# Resourse

[Brian Getting Started Mocking](https://myadventuresincoding.wordpress.com/2011/02/26/python-python-mock-cheat-sheet/)

# Wish List - in order from easiest to hardest
* Patch a single function.
  Be able to assign a return value, check if it's been called, check
  if any Exceptions were raised, etc.
* Patch a function that is within another function.
* To test only the functions of a Class.
  Can you do this without calling the __init__?

* To verify high-level execution of a Context Manager.
  Is __enter__ called? Did it exit correctly?

* Test a class function and also mock class attributes, which the function uses.

# Mock attributes
assert_any_call
assert_called
assert_called_once
assert_called_once_with
assert_called_with
assert_has_calls
assert_not_called
attach_mock
call_args
call_args_list
call_count
called
configure_mock
method_calls
mock_add_spec
mock_calls
reset_mock
return_value
side_effect

Scenario #1

```python

# app.py
class Base():
    def __init__(self):
        self.attr = 'original_value'
        
    def show(self):
        print('\nasdfasdfasdf', self.attr)        

class App():
    def __init__(self):  
        self.base = Base()

# test_app.py
from app import App

def test_mock_inherited_class_instance():
    """ With mocking. Change app.base.attr from 'original_value' to 'new_value'.
    """
    app = App()
    app.base = Mock()
    app.base.attr = 'new_value'
    app.base.show() # I'd like this to show 'new_value', NOT 'original_value'

```
