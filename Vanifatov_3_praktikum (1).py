import pandas as pd, csv, pickle
import sys

# используется метод pandas, потому что в нем гораздо удобнее введено представление файла в виде структурированной таблицы, с которой также удобно рабоать

def save_table(*arg):
    dd = pd.DataFrame(arg)
    nam = input('введите название файла')
    check = input('введите в каком формате хотите сохарнить')
    if check == 'csv':
        dd.to_csv(nam)
    if check == 'pickle':
        dd.to_pickle(nam)
    if check == 'txt':
        dd.to_txt(nam) #дерево для сохранения файла

# вся обработка файла происходит в функции load_table, там же пользователь и выбирает операции, которые необходимо выполнить с файлом. Функции, которые вызваются в данной функции прописаны после нее

def load_table():
    name = input('введите название файла')
    check = input('введите тип файла')
    if check.lower() == 'csv':
        try:
            file = pd.read_csv(name+'.'+check, sep = ',', encoding = 'CP866')
        except FileNotFoundError:
            print('не найдено')
    if check.lower() == 'pickle':
        try:
            file = pd.read_pickle(name+'.'+check)
        except FileNotFoundError:
            print('не найдено')
    if check.lower() == 'txt':
        try:
            file = pd.read_txt('output_list.txt', sep = ' ', header = None)
        except FileNotFoundError:
            print('не найдено')
    while True: #бесконечный цикл, чтобы выполнить все функции
        saver = input('хотите ли сохранить файл?')
        if saver.lower() == 'no': 
            print(spisok)
            data = input('выберете команду из списка')
            if data.lower() == 'get_rows_by_number':
                booler = input('вы будете копировать таблицу?')
                if booler.lower() == 'yes':
                    copy_table = True
                elif booler.lower() == 'no':
                    copy_table = False
                print('введите интервал')
                start, stop = int(input()),int(input())
                get_rows_by_number(file, start, stop, copy_table)
            elif data.lower() == 'get_rows_by_index':
                try:
                    name1 = input('введите название файла')
                    file2 = pd.read_csv(name1, sep = ',', encoding = 'CP866')
                except FileNotFoundError:
                    print('не найдено')
                get_rows_by_index(file,file2)
            elif data.lower() == 'get_column_types':
                get_column_types(file, by_number = True)
            elif data.lower() == 'set_column_types':
                set_column_types(by_number = True)
            elif data.lower() == 'get_values':
                get_values(file)
            elif data.lower() == 'set_value':
                column = int(input('какой столбец'))
                get_value(file.column)
            elif data.lower() == 'set_values':
                cou = int(input('введите количество занчений'))
                values = []
                for i in range(cou):                                           
                    vals = input('введите значения').split()
                    values.append(vals)
                set_values(values, file, column = 0)
            elif data.lower() == 'set_value':
                set_value(file, column = 0)
            elif data.lower() == 'print_table':
                print_table(file)
            elif data.lower() == 'concat':
                concat(file)
            elif data.lower() == 'split':
                delimiters = input('по какой строке разделить')
                split(file,delimiters)
            elif data.lower() == 'add':
                stroka1, stolbec1, stroka2, stolbec2 = int(input('введите первую строку')), int(input('введите первый столб')), int(input('введите вторую строку')), int(input('введите второй столбик'))
                add(file, stroka1, stolbec1, stroka2, stolbec2)
            elif data.lower() == 'sub':
                stroka1, stolbec1, stroka2, stolbec2 = int(input('введите первую строку')), int(input('введите первый столб')), int(input('введите вторую строку')), int(input('введите второй столбик'))
                sub(file, stroka1, stolbec1, stroka2, stolbec2)
            elif data.lower() == 'mul':
                stroka1, stolbec1, stroka2, stolbec2 = int(input('введите первую строку')), int(input('введите первый столб')), int(input('введите вторую строку')), int(input('введите второй столбик'))
                mul(file, stroka1, stolbec1, stroka2, stolbec2)
            elif data.lower() == 'div':
                stroka1, stolbec1, stroka2, stolbec2 = int(input('введите первую строку')), int(input('введите первый столб')), int(input('введите вторую строку')), int(input('введите второй столбик'))
                div(file, stroka1, stolbec1, stroka2, stolbec2)
            elif data.lower() == 'exit':
                break
            else:
                print('вы ввели неправильно написали функцию, проверьте еще раз')
                print(spisok)
        elif saver.lower() == 'yes':
            print(type(file))
            save_table(pd.DateFrame(file))
            break

# список всех используемых функций
spisok = ['get_rows_by_number','get_rows_by_index','get_column_types','set_column_types','get_values','get_value','set_values','set_value','print_table','concat','split','add','sub','mul','div']

def get_rows_by_number(file, start, stop, copy, copy_table = False): #получение таблицы из строк по ее номеру или интервалу
    if copy_table == True:
        print(file.loc[start:stop]) #разделяем по индексам
    else:
        n = stop-start                                                   
        a = []
        c = file.columns.to_list() #переводим в список
        for i in range(n):
            stroki = input('введите стоку').split()
            a.append(stroki)
        datafr = pd.DataFrame(a, columns = c) #создаем DataFrame
        file = file.append(datafr, ignore_index = True) #добавляем в таблицу

def get_rows_by_index(file, file2): # получение таблицы из строк. из элементов совпадающих с переданными элементами
    fst = file.loc[0]
    fst1 = file2.loc[0]
    try:
        if fst == fst1:
            point = pd.contact(file, file2)
    except ValueError:
        print('значения не сравнимы')
    to = print('сохранить в таблицу')
    if to.lower() == 'yes':
        save_table(point)

def get_column_types(file, by_number = True): # получение словаря вида столбец:тип значений
    d = file.to_dict() #переводим таблицу в словарь
    print(d)

def set_column_types(by_number = True): # задания словаря типа столбец:тип_значений
    a = []
    b = []
    str1 = int(input('введите количество строк'))
    str2 = int(input('введите количество столбцов'))
    for i in range(str1):
        a.append(input())
    for i in range(str2):
        if by_number == True:
            b.append(input())
        else: 
            b.append(int(input()))
    dic = dict(zip(b, a)) #объединяем в один словарь
    print(dic)
    new_df = pd.DataFrame(dic, index = [0]) #создаем датафрейм
    to = input('сохранить в таблицу?')
    if to.lower() == 'yes':
        save_table(new_df)

def get_values(file): # получение списка значений(типизированных согласно типу столбца), либо по номеру столбца
    d = file.to_dict() #переводим таблицу в словарь
    print(type(d))
    for i in d.values():
        print(i) #выводим значения

def get_value(file,column): #для представления таблицы с одной строкой
    print(file.iloc[:,column]) #срезами берем из таблицы значения

def set_values(values,file,column = 0): #задние списка значений для столбца значений, либо по номеру столбца
    sval = pd.DataFrame(values,columns = file.columns.to_list()) #вводим новые значения, создаем список и новую таблицу
    file = file.append(sval)
    print(file)

def set_value(file, column = 0): #представляет таблицу одной строкой
    stolb = input('введите столбец')
    file.loc[0,stolb] = input('введите новое значение') #вводим значение для одной ячейки
    print(file)

def print_table(file):
    print(file) #выводим файл

def concat(file1,file2):
    c = pd.concat(file1,file2) #соединяем в таблицу
    print(c)

def split(file,delimiters):
    first = file.loc[0:delimiters] #берем первую половину таблицы
    second = file.loc[delimiters:len(file)] #берем вторую половину таблицы
    print(first,second)

def add(file,stroka1,stolb1,stroka2,stolb2): #СУММА
    x1 = int(file.iloc[stroka1][stolb1]) #берем значения первой строки
    x2 = int(file.iloc[stroka2][stolb2]) #берем значения второй строки
    try:
        otv = x1+x2
    except ValueError:
        print('значения не вычисляются')
    print(otv)

def sub(file,stroka1,stolb1,stroka2,stolb2): #ВЫЧИТАНИЕ
    x1 = int(file.iloc[stroka1][stolb1]) #берем значения первой строки
    x2 = int(file.iloc[stroka2][stolb2]) #берем значения второй строки
    try:
        otv = x1-x2
    except ValueError:
        print('значения не вычисляются')
    print(otv)

def mul(file,stroka1,stolb1,stroka2,stolb2): #УМНОЖЕНИЕ
    x1 = int(file.iloc[stroka1][stolb1]) #берем значения первой строки
    x2 = int(file.iloc[stroka2][stolb2]) #берем значения второй строки
    try:
        otv = x1*x2
    except ValueError:
        print('значения не вычисляются')
    print(otv)

def div(file,stroka1,stolb1,stroka2,stolb2): #ДЕЛЕНИЕ
    x1 = int(file.iloc[stroka1][stolb1]) #берем значения первой строки
    x2 = int(file.iloc[stroka2][stolb2]) #берем значения второй строки
    try:
        otv = x1/x2
    except ValueError:
        print('значения не вычисляются')
    print(otv)

data = input('выберите команду: load or save')
if data.lower() == 'load':
    load_table()
elif data.lower() == 'save':
    save_table()
else:
    print('try again')