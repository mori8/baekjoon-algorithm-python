# 귀도 반 로썸은 크리스마스날 심심하다고 파이썬을 만들었다
# 그리고 이 문제를 파이썬으로 푸는 것은 미친짓이다
# 파이썬으로 풀다가 C 로 바꿨으니 Xcode 한번 뒤져봐라

import sys

command_line = []
pc = adder = 0


def parsing_command(cmd):
    return cmd[:3]


def sta(cmd):
    global command_line, adder
    command_line[int(cmd[3:], 2)] = adder
    print("adder = ", adder)


def lda(cmd):
    global command_line, adder
    adder = int(command_line[int(cmd[3:], 2)])
    print("adder = ", adder)


def beq(cmd):
    global adder, pc
    if adder == 0:
        pc = int(bin(int(cmd[3:], 2)))
        print("adder = ", adder)


def nop():
    print("adder = ", adder)
    pass


def dec():
    global adder
    adder -= 1
    print("adder = ", adder)


def inc():
    global adder
    adder += 1
    print("adder = ", adder)


def jmp(cmd):
    global pc
    pc = int(bin(int(cmd[3:], 2)))
    print("adder = ", adder)


for line in sys.stdin:
    command_line.append(line.rstrip())

while parsing_command(command_line[pc]) != '111':
    if parsing_command(command_line[pc]) == '000':
        sta(command_line[pc])
    elif parsing_command(command_line[pc]) == '001':
        lda(command_line[pc])
    elif parsing_command(command_line[pc]) == '010':
        beq(command_line[pc])
    elif parsing_command(command_line[pc]) == '011':
        nop()
    elif parsing_command(command_line[pc]) == '100':
        dec()
    elif parsing_command(command_line[pc]) == '101':
        inc()
    elif parsing_command(command_line[pc]) == '110':
        jmp()
    pc += 1

print(format(int(format(adder, 'b')) & 0xff, 'b'))