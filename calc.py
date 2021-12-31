# -*- coding: utf-8 -*-
# Первый запуск
try:
    f = open('config-url.txt')
    f.close()
except FileNotFoundError:
    print('FIRST BOOT!')
    configurl = input('Choose repo (default/url): ')
    f = open('config-url.txt', 'w')
    f.write(configurl)
    f.close()
f = open('config-url.txt', 'r')
cfurl = f.read()
f.close()
if cfurl == 'default':
    url = 'https://calc.makkate.ru/'
else:
    url = configurl
try:
    f = open('config.txt')
    f.close()
except FileNotFoundError:
    lang = input('Choose language (ru/en): ')
    f = open('config.txt', 'w')
    f.write(lang)
    f.close()
f = open('config.txt', 'r')
lang = f.read()
f.close()
# Проверка файлов
py1 = '/english.py'
py2 = '/russian.py'
py3 = '/start.wav'
py4 = '/calc.py'
py5 = '/shutdown.mp3'
py6 = '/requirements.txt'
print('Check files...')
try:
    f = open('requirements.txt')
    f.close()
    print('requirements.txt success!')
except FileNotFoundError:
    print('requirements.txt NOT FOUND! Downloading..')
    import requests
    f = open(r'requirements.txt',"wb")
    ufr = requests.get(url + py6)
    f.write(ufr.content)
    f.close()
try:
    f = open('english.py')
    f.close()
    print('english.py success!')
except FileNotFoundError:
    print('english.py NOT FOUND! Downloading..')
    import requests
    f = open(r'english.py',"wb")
    ufr = requests.get(url + py1)
    f.write(ufr.content)
    f.close()
try:
    f = open('russian.py')
    f.close()
    print('russian.py success!')
except FileNotFoundError:
    print('russian.py NOT FOUND! Downloading..')
    import requests
    f = open(r'russian.py',"wb")
    ufr = requests.get(url + py2)
    f.write(ufr.content)
    f.close()
try:
    f = open('start.wav')
    f.close()
    print('start.wav success!')
except FileNotFoundError:
    print('start.wav NOT FOUND! Downloading..')
    import requests
    f = open(r'start.wav',"wb")
    ufr = requests.get(url + py3)
    f.write(ufr.content)
    f.close()
try:
    f = open('shutdown.mp3')
    f.close()
    print('shutdown.mp3 success!')
except FileNotFoundError:
    print('shutdown.mp3 NOT FOUND! Downloading..')
    import requests
    f = open(r'shutdown.mp3',"wb")
    ufr = requests.get(url + py5)
    f.write(ufr.content)
    f.close()
# Проверка загрузки модулей
print('Loading Check...')
try:
    from colorama import Fore, Back, Style
    import os
    import time
    import sys
    import itertools
    import threading
    import math
    import platform
    import keyboard
    import pyglet
    from asciimatics import *
    from datetime import date
    from datetime import datetime
    from russian import *
    from english import *
except ModuleNotFoundError:
    import os
    print('ERROR! Downloading/Update/Installing Modules...')
    os.system('pip install -r requirements.txt')
# Импорт
from colorama import Fore, Back, Style
import os
os.system('title calc')
import time
import sys
import itertools
import threading
import math
import platform
import keyboard
import pyglet
from asciimatics import *
a = platform.system()
if platform.system() == 'Windows':
    cls = 'cls'
    rm = 'del'
    pera = 'calc.py'
else:
    cls = 'clear'
    rm = 'rm'
    pera = 'python3 calc.py'
try:
    f = open('config.txt')
    f.close()
except FileNotFoundError:
    lang = input('Choose language (ru/en): ')
    f = open('config.txt', 'w')
    f.write(lang)
    f.close()
f = open('config.txt', 'r')
lang = f.read()
f.close()
if lang == 'ru':
    from russian import *
else:
    from english import *
from datetime import date
from datetime import datetime
# Загрузка
current_time = datetime.now().time()
current_date = str(date.today())
ct_h = str(current_time.hour)
ct_m = str(current_time.minute)
ct_s = str(current_time.second)
i = 1
print()
os.system(cls)
print(Back.CYAN)
print(Fore.BLACK)
os.system(cls)
print(present)
print(just)
print(ny)
sound = pyglet.media.load("start.wav", streaming=False)
sound.play()
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write(loading + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(success)
t = threading.Thread(target=animate)
t.start()
time.sleep(0)
done = True
# Сам калькулятор
time.sleep(1)
while i <= 2:
    print(Back.GREEN)
    os.system(cls)
    print(Back.YELLOW)
    print(Fore.BLACK)
    print(version)
    print(Back.MAGENTA)
    current_time = datetime.now().time()
    current_date = str(date.today())
    ct_h = str(current_time.hour)
    ct_m = str(current_time.minute)
    ct_s = str(current_time.second)
    print(current_date + ' ' + ct_h + ':' + ct_m + ':' + ct_s)
    print(Back.GREEN)
    what = input(tut)
    if what == 'clang':
            f.close()
            os.system(rm + ' config.txt')
            sound = pyglet.media.load("shutdown.mp3", streaming=False)
            sound.play()
            done = False
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rReboot' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write("Success!")
            t = threading.Thread(target=animate)
            t.start()
            time.sleep(5)
            done = True
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            os.system(pera)
            break
    elif what == 'update':
        os.system(rm + ' calc.py')
        try:
            f = open('calc.py')
            f.close()
            print('ERROR!!!')
        except FileNotFoundError:
            print('calc.py removed! Downloading new file...')
            import requests
            f = open(r'calc.py',"wb")
            ufr = requests.get(url + py4)
            f.write(ufr.content)
            f.close()
        sound = pyglet.media.load("shutdown.mp3", streaming=False)
        sound.play()
        time.sleep(5)
        os.system(cls)
        os.system(pera)
    elif what == 'reboot':
        sound = pyglet.media.load("shutdown.mp3", streaming=False)
        sound.play()
        time.sleep(5)

        print(Back.BLACK)
        print(Fore.WHITE)
        os.system(cls)
        os.system(pera)
        break
    elif what == 'time':
        while True:
            time.sleep(0.1)
            print(Back.GREEN)
            os.system(cls)
            print(Back.YELLOW)
            print(Fore.BLACK)
            print(version)
            print(Back.MAGENTA)
            current_time = datetime.now().time()
            current_date = str(date.today())
            ct_h = str(current_time.hour)
            ct_m = str(current_time.minute)
            ct_s = str(current_time.second)
            print(current_date + ' ' + ct_h + ':' + ct_m + ':' + ct_s)
            print(stop_key)
            try:
                if keyboard.is_pressed('esc'):
                    break
                else:
                    pass
            except:
                break
    #сложение
    elif what == "+":
        a = float( input(one_number_plus) )
        b = float( input(two_number_plus) )
        c = a + b
        print(answer + str(c))
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #выход
    elif what == "exit":
        print(Back.BLACK)
        print(Fore.WHITE)
        os.system(cls)
        break
    #часы
    elif what == "clock":
        os.system('start clock.py')
    #путь к секрету №1
    elif what == "Зда%64№намбернAпPимерАбсд97":
        done = False
        def animate():
            for c in itertools.cycle(['|', '/', '-', '\\']):
                if done:
                    break
                sys.stdout.write(loading + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write(success)
        t = threading.Thread(target=animate)
        t.start()
        time.sleep(0.5)
        done = True
        time.sleep(2)
        print(code)
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #Путь к секрету №2
    elif what == "1485опрcaptnskg1638":
        os.sleep(2)
        print(xd)
        os.sleep(0.5)
        i += 0
    #Дискриминант
    elif what == "d":
        print(d1)
        a = float(input(d_a))
        b = float(input(d_b))
        c = float(input(d_c))
        discr = b ** 2 - 4 * a * c
        print(d_answer % discr)
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            print(d_answer_1 % (x1, x2))
        elif discr == 0:
            x = -b / (2 * a)
            print(d_answer_2 % x)
        else:
            print(d_no)
        e = input(continue_operation)
        if e == "yes":
            i += 0
        elif e == "y":
            i += 0
        elif e == "д":
            i += 0
        elif e == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
    #пранк 112
    elif what == "112":
        print(code_112_1)
        time.sleep(2)
        input(code_112_2)
        time.sleep(2)
        print(code_112_3)
        time.sleep(2)
        print(code_112_4)
        time.sleep(2)
        print(code_112_5)
        time.sleep(2)
        print(code_112_6)
        time.sleep(2)
        print(Back.BLACK)
        print(Fore.WHITE)
        os.system(cls)
        break
    #custom
    elif what == "custom":
        fg = input(custom_what)
        if fg == "1":
            tu = input(custom_tu)
            if tu == "--":
                a = float(input(custom_un))
                a = -a
                print(custom_un_answer + str(a))
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
            elif tu == "pi":
                print(math.pi)
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
            elif tu == "~":
                hu = input(custom_hu)
                if hu == "=":
                    a = float(input(custom_hu_equals_a))
                    print(round (a))
                    d = input(continue_operation)
                    if d == "yes":
                        i += 0
                    elif d == "y":
                        i += 0
                    elif d == "д":
                        i += 0
                    elif d == "да":
                        i += 0
                    else:
                        print(Back.BLACK)
                        print(Fore.WHITE)
                        os.system(cls)
                        break
                elif hu == "<":
                    a = float(input(custom_hu_less_a))
                    print(math.floor(a))
                    d = input(continue_operation)
                    if d == "yes":
                        i += 0
                    elif d == "y":
                        i += 0
                    elif d == "д":
                        i += 0
                    elif d == "да":
                        i += 0
                    else:
                        print(Back.BLACK)
                        print(Fore.WHITE)
                        os.system(cls)
                        break
                elif hu == ">":
                    a = float(input(custom_hu_more_a))
                    print(math.ceil(a))
                    d = input(continue_operation)
                    if d == "yes":
                        i += 0
                    elif d == "y":
                        i += 0
                    elif d == "д":
                        i += 0
                    elif d == "да":
                        i += 0
                    else:
                        print(Back.BLACK)
                        print(Fore.WHITE)
                        os.system(cls)
                        break
                else:
                    print(custom_tu_error)
                    d = input(continue_operation)
                    if d == "yes":
                        i += 0
                    elif d == "y":
                        i += 0
                    elif d == "д":
                        i += 0
                    elif d == "да":
                        i += 0
                    else:
                        print(Back.BLACK)
                        print(Fore.WHITE)
                        os.system(cls)
                        break
        elif fg == "2":
            custom2 = input(custom2_what)
            if custom2 == "+":
                a = float( input(one_number_plus) )
                b = float( input(two_number_plus) )
                c = a + b
                print(answer + str(c))
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
                    time.sleep(5)
            elif custom2 == "^":
                a = float( input(degree_a) )
                b = float( input(degree_b) )
                c = a ** b
                print(degree_answer + str(c))
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
            elif custom2 == "/":
                a = float( input(difference_a) )
                b = float( input(difference_b) )
                if b != 0:
                    print(difference_answer % (a/b))
                    d = input(continue_operation)
                    if d == "yes":
                        i += 0
                    elif d == "y":
                        i += 0
                    elif d == "д":
                        i += 0
                    elif d == "да":
                        i += 0
                    else:
                        print(Back.BLACK)
                        print(Fore.WHITE)
                        os.system(cls)
                        break
                else:
                    print(difference_0_error)
                    d = input(continue_operation)
                    if d == "yes":
                        i += 0
                    elif d == "y":
                        i += 0
                    elif d == "д":
                        i += 0
                    elif d == "да":
                        i += 0
                    else:
                        print(Back.BLACK)
                        print(Fore.WHITE)
                        os.system(cls)
                        break
            elif custom2 == "*":
                a = float( input(multiplication_a) )
                b = float( input(multiplication_b) )
                c = a * b
                print(answer + str(c))
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
            elif custom2 == "-":
                a = float( input(minus_a) )
                b = float( input(minus_b) )
                c = a - b
                print(answer + str(c))
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
        elif fg == "3":
            custom3 = input(custom3_what)
            if custom3 == "d":
                print(d1)
                a = float(input(d_a))
                b = float(input(d_b))
                c = float(input(d_c))
                discr = b ** 2 - 4 * a * c
                print(d_answer % discr)
                if discr > 0:
                    x1 = (-b + math.sqrt(discr)) / (2 * a)
                    x2 = (-b - math.sqrt(discr)) / (2 * a)
                    print(d_answer_1 % (x1, x2))
                elif discr == 0:
                    x = -b / (2 * a)
                    print(d_answer_2 % x)
                else:
                    print(d_no)
                e = input(continue_operation)
                if e == "yes":
                    i += 0
                elif e == "y":
                    i += 0
                elif e == "д":
                    i += 0
                elif e == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
            elif custom3 == "in %":
                a = float(input(in_a))
                b = float(input(in_b))
                c = float(input(in_c))
                e = float('100')
                f = a * e / b
                h = f * c / e
                print(answer + str(h))
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
            elif custom3 == "out of 100%":
                a = float(100)
                b = float( input(out_of_b))
                c = float( input(out_of_c))
                d = b / a * c
                print(answer + str(d))
                d = input(continue_operation)
                if d == "yes":
                    i += 0
                elif d == "y":
                    i += 0
                elif d == "д":
                    i += 0
                elif d == "да":
                    i += 0
                else:
                    print(Back.BLACK)
                    print(Fore.WHITE)
                    os.system(cls)
                    break
    #превращение в %
    elif what == "in %":
        a = float(input(in_a))
        b = float(input(in_b))
        c = float(input(in_c))
        e = float('100')
        f = a * e / b
        h = f * c / e
        print(answer + str(h))
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #помощь
    elif what == "help":
        print(help)
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #число Пи
    elif what == "pi":
        print(math.pi)
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #округление
    elif what == "~":
        pipi = input(rounding_what)
        if pipi == "=":
            a = float(input(rounding_equal_a))
            print(round (a))
            d = input(continue_operation)
            if d == "yes":
                i += 0
            elif d == "y":
                i += 0
            elif d == "д":
                i += 0
            elif d == "да":
                i += 0
            else:
                print(Back.BLACK)
                print(Fore.WHITE)
                os.system(cls)
                break
        elif pipi == "<":
            a = float(input(rounding_less_a))
            print(math.floor(a))
            d = input(continue_operation)
            if d == "yes":
                i += 0
            elif d == "y":
                i += 0
            elif d == "д":
                i += 0
            elif d == "да":
                i += 0
            else:
                print(Back.BLACK)
                print(Fore.WHITE)
                os.system(cls)
                break
        elif pipi == ">":
            a = float(input(rounding_more_a))
            print(math.ceil(a))
            d = input(continue_operation)
            if d == "yes":
                i += 0
            elif d == "y":
                i += 0
            elif d == "д":
                i += 0
            elif d == "да":
                i += 0
            else:
                print(Back.BLACK)
                print(Fore.WHITE)
                os.system(cls)
                break
        else:
            print(rounding_error)
            d = input(continue_operation)
            if d == "yes":
                i += 0
            elif d == "y":
                i += 0
            elif d == "д":
                i += 0
            elif d == "да":
                i += 0
            else:
                print(Back.BLACK)
                print(Fore.WHITE)
                os.system(cls)
                break
    #унарный минус
    elif what == "--":
        a = float( input(un) )
        a = -a
        print(un_answer + str(a))
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #когда число это 100% и надо это число превратить в сколько-то процентов
    elif what == "out of 100%":
        a = float(100)
        b = float( input(out_of_b))
        c = float( input(out_of_c))
        d = b / a * c
        print(answer + str(d))
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #в степень
    elif what == "^":
        a = float( input(degree_a) )
        b = float( input(degree_b) )
        c = a ** b
        print(degree_answer + str(c))
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #деление
    elif what == "/":
        a = float( input(difference_a) )
        b = float( input(difference_b) )
        if b != 0:
            print(difference_answer % (a/b))
            d = input(continue_operation)
            if d == "yes":
                i += 0
            elif d == "y":
                i += 0
            elif d == "д":
                i += 0
            elif d == "да":
                i += 0
            else:
                print(Back.BLACK)
                print(Fore.WHITE)
                os.system(cls)
                break
        else:
            print(difference_0_error)
            d = input(continue_operation)
            if d == "yes":
                i += 0
            elif d == "y":
                i += 0
            elif d == "д":
                i += 0
            elif d == "да":
                i += 0
            else:
                print(Back.BLACK)
                print(Fore.WHITE)
                os.system(cls)
                break

    #умножение
    elif what == "*":
        a = float( input(multiplication_a) )
        b = float( input(multiplication_b) )
        c = a * b
        print(answer + str(c))
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #вычитание
    elif what == "-":
        a = float( input(minus_a) )
        b = float( input(minus_b) )
        c = a - b
        print(answer + str(c))
        d = input(continue_operation)
        if d == "yes":
            i += 0
        elif d == "y":
            i += 0
        elif d == "д":
            i += 0
        elif d == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            break
    #в других случаях
    else:
        print(error)
        input()
sound = pyglet.media.load("shutdown.mp3", streaming=False)
sound.play()
time.sleep(4)
