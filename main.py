a = input("Введите вашу строку: ") #Ввод строки с клавиатуры
print("Ваша строка: ", a) #Вывод строки
print("Длина вашей строки: ", len(a)) #Вывод длины строки на консоль с помощью функции len()
g = 0 #Переменная для подсчета гласных
s = 0 #Переменная для подсчета согласных
str_g = str("аоеэюяиыёуи")
for i in a: #Цикл for для перебора элементов строки
    #Цикл if для определения является ли символ гласным
    if i in str_g or i in str_g.upper(): 
        g += 1 #Увеличение переменной на 1 при верности условия
    elif i.isalpha() == True: #еlif для проверки является ли символ согласной буквой
        s += 1 #Увеличение переменной на 1 при верности условия
print("Количество гласных в вашей строке: ", g) #Вывод на консоль количества гласных
print("Количество согласных в вашей строке: ", s) #Вывод на консоль количества согласных
