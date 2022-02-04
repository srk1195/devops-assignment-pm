from app import Car,Direction

# Testing the Direction class
def testDirectionForward():
    direction = Direction.FORWARD
    assert direction.value == 1

def testDirectionNotForward():
    direction = Direction.FORWARD
    assert direction.value != 2

def testDirectionReverse():
    direction = Direction.REVERSE
    assert direction.value == 2

def testDirectionNotReverse():
    direction = Direction.REVERSE
    assert direction.value != 3

def testDirectionStopped():
    direction = Direction.STOPPED
    assert direction.value == 3

def testDirectionNotStopped():
    direction = Direction.STOPPED
    assert direction.value != 1