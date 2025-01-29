# python -m pip install --upgrade pip  
import eel    # pip install eel 
import os 
from engine.Command import *
from engine.OpenMSapp import *
from engine.CloseApp import *
from engine.SearchNow import *
from engine.SystemCall import *
from engine.ShortcutKey import *
from engine.ChatWithJarvis import *

eel.init("www")
os.system('start msedge.exe --app="http://localhost:8000/index.html"')
eel.start('index.html', mode=None, host='localhost', block=True)    