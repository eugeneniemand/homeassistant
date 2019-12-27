from ctypes import Structure, windll, c_uint, sizeof, byref
import threading
import requests
import json

prevMillis = 0
timeout = 10.0
# Print out every n seconds the idle time, when moving mouse, this should be < 10
def startPolling():
    global timeout
    threading.Timer(timeout, startPolling).start()
    idleDuration = get_idle_duration()
    print(idleDuration)
    PushHass(idleDuration)

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def PushHass(idleDuration):
    global timeout
    url = '<WEBHOOK_URL>'
    headers = {'content-type': 'application/json'}
    data = json.dumps({"idle": 1 if idleDuration == timeout else 0})
    response = requests.post(url, data, headers=headers)
    print(data) 

def get_idle_duration():
    global prevMillis
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = (windll.kernel32.GetTickCount() - lastInputInfo.dwTime) / 1000.0    
    activityMillis = millis - prevMillis
    prevMillis = millis
    return activityMillis

startPolling()