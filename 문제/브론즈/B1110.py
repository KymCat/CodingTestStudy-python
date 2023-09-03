start = int(input())
ing = start
result = 0
while True :
    ing = ((ing%10)*10) + ((ing//10 + ing%10)%10)
    result+=1
    if start == ing :
        break

print(result)