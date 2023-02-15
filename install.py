ver = ('0.95')
import pygame
print('Init...')
pygame.init()
pygame.mixer.music.load('f85988897063659.mp3')
pygame.mixer.music.play(-1)
print('Welcome to Calc Installer!')
input('PRESS_ENTER...')
upd = input('Do you want to check for updates? (yes/no): ')
if upd == 'yes':
    import os
    import platform
    a = platform.system()
    if platform.system() == 'Windows':
        rm = 'del'
        insop = 'install.py'
    else:
        rm = 'rm'
        insop = 'python3 install.py'
    os.system(rm + ' install.py')
    import requests
    f = open(r'install.py',"wb")
    ufr = requests.get("http://calc.makkate.ru/install.py")
    f.write(ufr.content)
    f.close()
    print('reboot')
    os.system(insop)
    exit()
print('Installing...')
print('Installing moduls')
import os
import platform
a = platform.system()
if platform.system() == 'Windows':
    cls = 'cls'
    rm = 'del'
    pera = 'pip install -r requirements.txt'
    pip = 'timeout 1'
    pipr = 'pip install requests'
    pstart = 'calc.py'
else:
    cls = 'clear'
    rm = 'rm'
    pip = 'sudo apt install python3-pip'
    pera = 'python3 pip install -r requirements.txt'
    pipr = 'python3 pip install requests'
    pstart = 'python3 calc.py'
os.system(pipr)
try:
    f = open('requirements.txt')
    f.close()
    print('requirements success!')
except FileNotFoundError:
    print('Downloading requirements.txt')
    import requests
    f = open(r'requirements.txt',"wb")
    ufr = requests.get("http://calc.makkate.ru/requirements.txt")
    f.write(ufr.content)
    f.close()
os.system(pip)
os.system(pera)
print('Checking...')
while True:
    try:
        from colorama import Fore, Back, Style
        import os
        import time
        import sys
        import itertools
        import threading
        import math
        import platform
        from asciimatics import *
        from russian import *
        from english import *
        from datetime import date
        from datetime import datetime
        import requests
        break
    except ModuleNotFoundError:
        print('ERROR import modules, trying installing...')
        os.system(pera)
        break
print('Check files...')
try:
    f = open('calc.py')
    f.close()
    print('calc.py success!')
except FileNotFoundError:
    print('Downloading calc.py')
    import requests
    f = open(r'calc.py',"wb")
    ufr = requests.get("http://calc.makkate.ru/calc.py")
    f.write(ufr.content)
    f.close()
try:
    f = open('english.py')
    f.close()
    print('english.py success!')
except FileNotFoundError:
    print('Downloading english.py')
    import requests
    f = open(r'english.py',"wb")
    ufr = requests.get("http://calc.makkate.ru/english.py")
    f.write(ufr.content)
    f.close()
try:
    f = open('russian.py')
    f.close()
    print('russian.py success!')
except FileNotFoundError:
    print('Downloading russian.py')
    import requests
    f = open(r'russian.py',"wb")
    ufr = requests.get("http://calc.makkate.ru/russian.py")
    f.write(ufr.content)
    f.close()
try:
    f = open('shutdown.mp3')
    f.close()
    print('shutdown.mp3 success!')
except FileNotFoundError:
    print('Downloading shutdown.mp3')
    import requests
    f = open(r'calc.py',"wb")
    ufr = requests.get("http://calc.makkate.ru/shutdown.mp3")
    f.write(ufr.content)
    f.close()
try:
    f = open('start.wav')
    f.close()
    print('start.wav success!')
except FileNotFoundError:
    print('Downloading start.wav')
    import requests
    f = open(r'start.wav',"wb")
    ufr = requests.get("http://calc.makkate.ru/start.wav")
    f.write(ufr.content)
    f.close()
print('Install ended! Start calc.py')
os.system(rm + ' install.py')
os.system(cls)
pygame.mixer.music.stop()
os.system(pstart)
exit()
