# -*- coding: utf-8 -*-
# Импорт
from colorama import Fore, Back, Style
import os
import time
import wave
import sys
import itertools
import threading
import math
import platform
from playsound import playsound
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
# Загрузка
i = 1
print(cls)
os.system(cls)
print(Back.CYAN)
print(Fore.BLACK)
os.system(cls)
print(present)
def function_sound():
    playsound("start.wav", block=False)
function_sound()
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
# Сам калькулятор
time.sleep(1)
while i <= 2:
    print(Back.GREEN)
    os.system(cls)
    print(Back.YELLOW)
    print(Fore.BLACK)
    print(version)
    print(Back.GREEN)
    what = input(tut)
    if what == 'clang':
            f.close()
            os.system(rm + ' config.txt')
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
            time.sleep(0.5)
            done = True
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system(cls)
            os.system(pera)
            break
    if what == 'reboot':
        print(Back.BLACK)
        print(Fore.WHITE)
        os.system(cls)
        os.system(pera)
        break
    #сложение
    if what == "+":
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
                d = a * c / b
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
        d = a * c / b
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
