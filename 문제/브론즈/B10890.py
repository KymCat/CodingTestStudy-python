alphabet = []
for i in range(26) :
    alphabet.append(chr(97+i))

s = input()
for i in alphabet :
    if i not in s :
        print(-1, end= " ")
    else :
        print(s.index(i), end= " ")