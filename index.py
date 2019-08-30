import keyboard
import threading
import atexit
from threading import Timer

triggerCount = 0
triggerTimer = -1

result = None

def cleanup ():
    print 'cleanup before exit'
    clearTimer()
    keyboard
    triggerCount = 0

def clearTimer ():
    global triggerTimer
    global triggerCount
    try:
        triggerTimer.isAlive()
        if triggerTimer.isAlive():
            triggerTimer.cancel()
            triggerTimer = -1
    except AttributeError:
        pass

def startTimer ():
    global triggerTimer
    triggerTimer = Timer(0.6, validTimeout)
    triggerTimer.start()

def validTimeout ():
    global triggerTimer
    global triggerCount
    clearTimer()
    triggerCount = 0

def onPresskey ():
    global triggerTimer
    global triggerCount
    triggerCount += 1
    clearTimer()

    if triggerCount == 2:
        print('CTRL+C')
        triggerCount = 0
        clearTimer()
    else:
        startTimer()
        

def registerCopyHotkey ():
    keyboard.add_hotkey('ctrl+c', onPresskey)
    keyboard.wait()

def main ():
    registerCopyHotkey()

if __name__ == '__main__':
    atexit.register(cleanup)
    main()
