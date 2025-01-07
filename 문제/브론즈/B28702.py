import sys

array = []
for _ in range(3) :
    array.append(sys.stdin.readline().rstrip())

def answer_print(answer) :
    if answer % 3 == 0 and answer % 5 == 0 :
        print('FizzBuzz')

    elif answer % 3 == 0 :
        print('Fizz')

    elif answer % 5 == 0 :
        print('Buzz')

    else :
        print(answer)

if array[2].isdigit() :
    answer = int(array[2]) + 1
    answer_print(answer)

else :
    for i in range(1,-1,-1) :
        if array[i].isdigit() :
            answer = int(array[i]) + (3-i)
            answer_print(answer)
            break

        else :
            continue
