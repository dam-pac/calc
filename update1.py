import math
from update1_russian import *

def calc_u1():
    while True:
        try:
            print(calc_u1_1)
            calc_u1_input = input(calc_u1_input_msg)
            if calc_u1_input == 'cos':
                calc_u1_input_cos_a = int(input(calc_u1_cos_msg))
                calc_u1_cos_ans = math.cos(calc_u1_input_cos_a)
                print(f'Cos: {calc_u1_cos_ans}')
            elif calc_u1_input == 'sin':
                calc_u1_input_sin_a = int(input(calc_u1_sin_msg))
                calc_u1_sin_ans = math.sin(calc_u1_input_sin_a)
                print(f'Sin: {calc_u1_sin_ans}')
            elif calc_u1_input == 'tg':
                calc_u1_input_tg_a = int(input(calc_u1_tg_msg))
                calc_u1_tg_ans = math.tan(calc_u1_input_tg_a)
                print(f'Tan: {calc_u1_tg_ans}')
            elif calc_u1_input == 'stop':
                return 0
            else:
                print(calc_u1_error_msg)
        except ValueError:
            print('CALC:VALUE_ERROR:ONLY_NUMBERS')
