#!/usr/bin/python3
import sys


# initiates and prints out estimates for expert and calculator
def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Need file with operators\n")
        sys.exit(1)
    operators = get_operators(sys.argv[1])
    time_exp = calculate(operators, 'e')
    time_calc = calculate(operators, 'l')
    sys.stdout.write('Time estimate according to Card, Moran, Newell and Kieras: ' + str(time_exp) + ' seconds\n')
    sys.stdout.write('Time estimate according to Calculator: ' + str(time_calc) + ' seconds\n')


# gets the operators from the file
def get_operators(filename):
    operator = []
    file = open(filename).readlines()
    for line in file:
        op = ''
        line = line.replace('\n', ' ').replace(' ', '').lower()
        for char in line:
            if char == '#':
                break
            else:
                op += char
        if op != '':
            operator.append(op)
    return operator


# calculates the time needed for the operations dependent on mode
def calculate(operators, mode):
    if mode == 'e':
        k, p, h, m, b = get_time_expert()
    if mode == 'l':
        k, p, h, m, b = get_time_calc()
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    chars = ['k', 'p', 'h', 'm', 'b']
    calc_time = 0
    for operator in operators:
        num = ''
        val = False
        for char in operator:
            if char in numbers:
                num += char
                val = True
            elif char in chars:
                time = 0
                if char == 'k':
                    time = k
                elif char == 'p':
                    time = p
                elif char == 'h':
                    time = h
                elif char == 'm':
                    time = m
                elif char == 'b':
                    time = b
                if val:
                    calc_time += float(num) * time
                    val = False
                    num = ''
                else:
                    calc_time += time
    return round(calc_time, 2)


# returns the operator time for Card, Moran, Newell and Kieras ( M was chosen after Kieras)
def get_time_expert():
    k = 0.20  # used 0.20 because we consider us as average typing strength as we do a lot of typing (55wmp)
    p = 1.1
    h = 0.4
    m = 1.2
    b = 0.1
    return k, p, h, m, b


# returns the operator time for our calculator ( M is the same as with expert)
def get_time_calc():
    k = 0.2  # 0.198
    p = 1.02
    h = 0.85  # 0.845
    m = 1.2
    b = 0.1  # 0.099
    return k, p, h, m, b


if __name__ == '__main__':
    main()
