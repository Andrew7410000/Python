largest = None
smallest = None
# Открываем цикл
while True:
    # Если правда, то пробуем:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        n = int(num) # Перевели в число без точки
        # Можно было написать num = int(num) 
        # Работает только на первый раз. Если largest еще не задано, то присваевываем ему значение n, какое оно ни было бы
        if largest == None: 
            largest = n 
        elif largest < n: # Если при повторном круге новое значение больше предыдущего, то мы его перезаписываем, если нет, то ничего не делаем
            largest = n

        if smallest == None:
            smallest = n
        elif smallest > n:
            smallest = n

    except:
        print ("Invalid input") # Это если ввести не число 

print("Maximum is", largest)
print("Minimum is", smallest)