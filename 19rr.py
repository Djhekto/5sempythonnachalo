# Вводятся в столбик пары натуральных чисел через запятую. 
# Каждая пара M, N обозначает взаимное знакомство людей под номерами M и N. 
# Ввод заканчивается парой 0, 0 (не учитывается, и вообще человек N считается незнакомым с человеком N ;) ). 
# Вывести через пробел в порядке возрастания номера тех, 
# кто знаком со всеми остальными, или пустую строку, если таких нет.

from collections import Counter

allconnect = {1:2, 2:3}

while(1):
    a, b = eval(input())
    if a==0:
        if b==0:
            break;
    if a<=b:
        allconnect[a] = b
    else:
        allconnect[b] = a
        
print(allconnect)    
print(allconnect.keys())    

