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

# Testing the Car class
def testCarInitialDirection():
    mustang = Car()
    assert mustang.direction == Direction.STOPPED

def testIsMovingFalse():
    mustang = Car()
    assert mustang.isMoving() == False

def testIsMovingTrue():
    mustang = Car()
    mustang.moveForward()
    assert mustang.isMoving() == True

def testIsMoveForwardTrue():
    mustang = Car()
    mustang.moveForward()
    assert mustang.direction == Direction.FORWARD

def testIsMoveForwardFalse():
    mustang = Car()
    mustang.moveForward()
    assert mustang.direction != Direction.REVERSE
    assert mustang.direction != Direction.STOPPED

def testIsMoveBackwardTrue():
    mustang = Car()
    mustang.moveBackward()
    assert mustang.direction == Direction.REVERSE

def testIsMoveBackwardFalse():
    mustang = Car()
    mustang.moveBackward()
    assert mustang.direction != Direction.FORWARD 
    assert mustang.direction != Direction.STOPPED

def testIsStopTrue():
    mustang = Car()
    mustang.moveBackward()
    mustang.moveForward()
    mustang.stop()
    assert mustang.direction == Direction.STOPPED

def testIsStopFalse():
    mustang = Car()
    mustang.moveBackward()
    mustang.moveBackward()
    mustang.stop()
    assert mustang.direction != Direction.FORWARD