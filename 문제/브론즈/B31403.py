array = [ str(input()) for _ in range(3) ]
print(eval(f'{array[0]} + {array[1]} - {array[2]}'))

ab = array[0] + array[1]
print(eval(f'{ab} - {array[2]}'))