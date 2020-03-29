num = int(input())
number_of_answer = 0

for i in range(1, num + 1):
    if len(str(i)) == 1 or len(str(i)) == 2:
        number_of_answer += 1
    else:
        gap = int(str(i)[1]) - int(str(i)[0])
        flag = True
        for index in range(1, len(str(i))-1):
            if gap != int(str(i)[index+1]) - int(str(i)[index]):
                flag = False
                break
        if flag:
            number_of_answer += 1

print(number_of_answer)