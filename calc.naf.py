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
from playsound import playsound
from asciimatics import *
# Загрузка
i = 1
os.system('cls')
print(Back.CYAN)
print(Fore.BLACK)
os.system('cls')
print("\n\n\n\n\n\n\n\n\n\n\n\n\n                                                  dam_pac представляет\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nНаберите команду 'help', чтобы узнать какие включены команды и как работать.")
def function_sound():
    playsound("start.wav", block=False)
function_sound()
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rЗагрузка ' + c)
        sys.stdout.flush()
        time.sleep(0)
    sys.stdout.write('\rУспешно!     ')
t = threading.Thread(target=animate)
t.start()
time.sleep(0)
done = True
# Сам калькулятор
time.sleep(0)
while i <= 2:
    print(Back.GREEN)
    os.system('cls')
    print(Back.YELLOW)
    print(Fore.BLACK)
    print("                                             Калькулятор v1.0 prerelease                                                ")
    print(Back.GREEN)
    what = input( "Что делаем?: ")
    #сложение
    if what == "+":
        a = float( input("Первое число: ") )
        b = float( input("Второе число: ") )
        c = a + b
        print("Ответ:" + str(c))
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #выход
    elif what == "exit":
        print(Back.BLACK)
        print(Fore.WHITE)
        os.system('cls')
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
                sys.stdout.write('\rЗагрузка ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rУспешно!     ')
        t = threading.Thread(target=animate)
        t.start()
        time.sleep(0.5)
        done = True
        time.sleep(2)
        print("Код: 1485опрcaptnskg1638")
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #Путь к секрету №2
    elif what == "1485опрcaptnskg1638":
        os.sleep(2)
        print("Ты попался! XD")
        os.sleep(0.5)
        i += 0
    #Дискриминант
    elif what == "d":
        print("Введите коэффициенты для уравнения \n ax^2 + bx + c = 0")
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        discr = b ** 2 - 4 * a * c
        print("Дискриминант = %.2f" % discr)
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif discr == 0:
            x = -b / (2 * a)
            print("x = %.2f" % x)
        else:
            print("Корней нет")
        e = input("Продолжить?: ")
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
            os.system('cls')
    #пранк 112
    elif what == "112":
        print("Вызываю...")
        time.sleep(2)
        input("Что у вас случилось?: ")
        time.sleep(2)
        print("Ожидайте...")
        time.sleep(2)
        print("Высылаю отряд на ваш адрес...")
        time.sleep(2)
        print("Удачи, досвидания!")
        time.sleep(2)
        print("Спасибо за участие в пранке! Код: Зда%64№намбернAпPимерАбсд97")
        time.sleep(2)
        print(Back.BLACK)
        print(Fore.WHITE)
        os.system('cls')
        break
    #custom
    elif what == "custom":
        fg = input("Сколько чисел?: ")
        if fg == "1":
            что = input("Мы можем: \n-- 'Унарный минус'\n~ 'округление'\nПи 'Показать число Пи' \nЧто делаем?: ")
            if что == "--":
                a = float(input("Число: "))
                a = -a
                print("Ответ: " + str(a))
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
            elif что == "Пи":
                print(math.pi)
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
            elif что == "~":
                выбор = input("Обычно или в большую сторону, или в меньшую сторону '=, <, >': ")
                if выбор == "=":
                    a = float(input("Введите число: "))
                    print(round (a))
                    d = input("Продолжить?: ")
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
                        os.system('cls')
                        break
                elif выбор == "<":
                    a = float(input("Введите число: "))
                    print(math.floor(a))
                    d = input("Продолжить?: ")
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
                        os.system('cls')
                        break
                elif выбор == ">":
                    a = float(input("Введите число: "))
                    print(math.ceil(a))
                    d = input("Продолжить?: ")
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
                        os.system('cls')
                        break
                else:
                    print("Ошибка, введите в начале help для помощи")
                    d = input("Продолжить?: ")
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
                        os.system('cls')
                        break
        elif fg == "2":
            custom2 = input("На две переменных мы можем: Сложение, В степень, Деление, Умножение, Вычитание \n Для выбора напишите: \n Сложение - + \n В степень - ^ \n Деление - / \n Умножение - * \n Вычитание - - \n Что вы выбираете: ")
            if custom2 == "+":
                a = float( input("Первое число: ") )
                b = float( input("Второе число: ") )
                c = a + b
                print("Ответ:" + str(c))
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
                    time.sleep(5)
            elif custom2 == "^":
                a = float( input("Число: ") )
                b = float( input("В какую степень: ") )
                c = a ** b
                print("Ответ: " + str(c))
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
            elif custom2 == "/":
                a = float( input("Делимое: ") )
                b = float( input("Делитель: ") )
                if b != 0:
                    print("%.2f" % (a/b))
                    d = input("Продолжить?: ")
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
                        os.system('cls')
                        break
                else:
                    print("Ошибка. Деление на ноль!")
                    d = input("Продолжить?: ")
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
                        os.system('cls')
                        break
            elif custom2 == "*":
                a = float( input("Множитель: ") )
                b = float( input("На множитель: ") )
                c = a * b
                print("Ответ: " + str(c))
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
            elif custom2 == "-":
                a = float( input("Первое число: ") )
                b = float( input("Второе число: ") )
                c = a - b
                print("Ответ: " + str(c))
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
        elif fg == "3":
            custom3 = input("Мы можем на три переменные: превращение в проценты, превращение из 100% в x% и дискриминант. \n Для того, чтобы выбрать необходимо написать: \n Превращение в проценты - в % \n Превращение из 100% в x% - из 100% \n Дискриминант - d \n Выбираем: ")
            if custom3 == "d":
                print("Введите коэффициенты для уравнения \n ax^2 + bx + c = 0")
                a = float(input("a: "))
                b = float(input("b: "))
                c = float(input("c: "))
                discr = b ** 2 - 4 * a * c
                print("Дискриминант = %.2f" % discr)
                if discr > 0:
                    x1 = (-b + math.sqrt(discr)) / (2 * a)
                    x2 = (-b - math.sqrt(discr)) / (2 * a)
                    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
                elif discr == 0:
                    x = -b / (2 * a)
                    print("x = %.2f" % x)
                else:
                    print("Корней нет")
                e = input("Продолжить?: ")
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
                    os.system('cls')
            elif custom3 == "в %":
                a = float(input("Введите число: "))
                b = float(input("Это сколько процентов?: "))
                c = float(input("Превратить в сколько процентов?: "))
                d = a * c / b
                print("Ответ: " + str(d))
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
            elif custom3 == "из 100%":
                a = float(100)
                b = float( input("Число; "))
                c = float( input("В какой процент; "))
                d = b / a * c
                print("Ответ: " + str(d))
                d = input("Продолжить?: ")
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
                    os.system('cls')
                    break
    #превращение в %
    elif what == "в %":
        a = float(input("Введите число: "))
        b = float(input("Это сколько процентов?: "))
        c = float(input("Превратить в сколько процентов?: "))
        d = a * c / b
        print("Ответ: " + str(d))
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #помощь
    elif what == "help":
        print("Нелья делить на ноль!\nЕсли хотите что-то изменить или добавить, то пишите Комплект#3834 в Discord\nПисать слова полностью.\nВ строке 'Продолжить?:' пишите ,yes, для продолжения работы или любые символы для завершения.\nНе для коммерческих организаций!!!\dam_pac не несёт ответственности!\nСписок команд:\nexit\nокругление\nПи\nунарный минус\nhelp\ncustom\nв %\nиз 100%\n/\n^\n*\n-\n+")
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #число Пи
    elif what == "Пи":
        print(math.pi)
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #округление
    elif what == "округление":
        выбор = input("Обычно или в большую сторону, или в меньшую сторону '=, <, >': ")
        if выбор == "=":
            a = float(input("Введите число: "))
            print(round (a))
            d = input("Продолжить?: ")
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
                os.system('cls')
                break
        elif выбор == "<":
            a = float(input("Введите число: "))
            print(math.floor(a))
            d = input("Продолжить?: ")
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
                os.system('cls')
                break
        elif выбор == ">":
            a = float(input("Введите число: "))
            print(math.ceil(a))
            d = input("Продолжить?: ")
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
                os.system('cls')
                break
        else:
            print("Ошибка, введите в начале help для помощи")
            d = input("Продолжить?: ")
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
                os.system('cls')
                break
    #унарный минус
    elif what == "унарный минус":
        a = float( input("Число: ") )
        a = -a
        print("Ответ: " + str(a))
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #когда число это 100% и надо это число превратить в сколько-то процентов
    elif what == "из 100%":
        a = float(100)
        b = float( input("Число; "))
        c = float( input("В какой процент; "))
        d = b / a * c
        print("Ответ: " + str(d))
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #в степень
    elif what == "^":
        a = float( input("Число: ") )
        b = float( input("В какую степень: ") )
        c = a ** b
        print("Ответ: " + str(c))
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #деление
    elif what == "/":
        a = float( input("Делимое: ") )
        b = float( input("Делитель: ") )
        if b != 0:
            print("%.2f" % (a/b))
            d = input("Продолжить?: ")
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
                os.system('cls')
                break
        else:
            print("Ошибка. Деление на ноль!")
            d = input("Продолжить?: ")
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
                os.system('cls')
                break
        
    #умножение
    elif what == "*":
        a = float( input("Множитель: ") )
        b = float( input("На множитель: ") )
        c = a * b
        print("Ответ: " + str(c))
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #вычитание
    elif what == "-":
        a = float( input("Первое число: ") )
        b = float( input("Второе число: ") )
        c = a - b
        print("Ответ: " + str(c))
        d = input("Продолжить?: ")
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
            os.system('cls')
            break
    #в других случаях
    else:
        print("Ошибка, введите в начале help для помощи")
        input()
    

