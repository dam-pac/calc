# -*- coding: utf-8 -*-
# Импорт
from colorama import Fore, Back, Style
import os
import time
import pyaudio
import wave
import sys
import itertools
import threading
import math
# Загрузка
i = 1
os.system('cls')
print(Back.CYAN)
print(Fore.BLACK)
os.system('cls')
print("\n\n\n\n\n\n\n\n\n\n\n\n\n                                                  dam_pac представляет\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nНаберите команду 'help', чтобы узнать какие включены команды и как работать.")
wf = wave.open("Запуск.wav", 'rb')
p = pyaudio.PyAudio()
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
stream.start_stream()
while stream.is_active():
    time.sleep(0.1)
stream.stop_stream()
stream.close()
wf.close()
p.terminate()
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
# Сам калькулятор
time.sleep(1)
while i <= 2:
    print(Back.GREEN)
    os.system('cls')
    print(Back.YELLOW)
    print(Fore.BLACK)
    print("                                            Калькулятор v0.9 public beta                                                ")
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
        print("Загрузка ...")
        time.sleep(2)
        print("Канал Mili life это канал на ютубе. Пожалуйста подпишитесь на наш канал! http://catcut.net/ZwrL Код: 1485опрcaptnskg1638")
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
    elif what == "d":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        d = (b * b) - 4 * a * c
        print("Дискриминант : " + str(d))
        f = input("Продолжить?: ")
        if f == "yes":
            i += 0
        elif f == "y":
            i += 0
        elif f == "д":
            i += 0
        elif f == "да":
            i += 0
        else:
            print(Back.BLACK)
            print(Fore.WHITE)
            os.system('cls')
            break
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
            что = input("Мы можем: \n-- 'Унарный минус'\n~ 'округление'\nЧто делаем?: ")
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
            print("В разработке...")
            time.sleep(5)
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
        print("Нелья делить на ноль!\nЕсли есть ошибка присылать отчёт: https://vk.com/club182773289\nЕсли хотите что-то изменить или добавить, то: https://vk.com/club182773289\nНе для одноязычной Windows.\nПисать слова полностью.\nКоманда custom в разработке.\nВ строке 'Продолжить?:' пишите ,yes, для продолжения работы или любые символы для завершения.\nНе для коммерческих организаций!!!\nКанал Mililife не несёт ответственности!\nСписок команд:\nexit\nокругление\nПи\nунарный минус\nhelp\ncustom\nв %\nиз 100%\n/\n^\n*\n-\n+")
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
    
