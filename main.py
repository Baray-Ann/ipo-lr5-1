a=input("Введите вашу строку: ")
print("Ваша строка: ", a)
print("Длина вашей строки: ", len(a))
g=0
s=0
for i in a:
    if i=="а" or i=="о" or i=="э" or i=="ю" or i=="я" or i=="у" or i=="е" or i=="ё" or i=="ы" or i=="и":
        g+=1
    elif i!=" ":
        s+=1
print("Количество гласных в вашей строке: ", g)
print("Количество согласных в вашей строке: ", s)