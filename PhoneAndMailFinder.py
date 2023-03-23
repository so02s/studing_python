#!python3
# -*- coding: cp1251 -*-
#PhoneAndMailFinder - ищет все телефоны и
#электронные адреса в буфере обмена

import pyperclip, re

#вставить из буфера обмена
text = str(pyperclip.paste())

#шаблон для телефонов
phoneRegex = re.compile(r'''(
(\d?)          #регион
(\(|\s)?       #скобка
(\d{3})        #три цифры
(\)|\s)?       #скобка
(\d{3})        #три цифры
(\s|-|\.)      #разделитель
(\d{2})        #две цифры
(\s|-|\.)      #разделитель
(\d{2})        #две цифры
)''', re.VERBOSE)

#шаблон для электронных адресов
mailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+        #имя пользователя
@                        #собака
[a-zA-Z0-9-]+            #домен
\.                       #точка
[a-zA-Z]+                 #код страны
)''', re.VERBOSE)

#пройтись по тексту и записать все найденное
matches = []
for groups in phoneRegex.findall(text):
    phoneNumber = groups[1] + '(' + groups[3] + ')' + '-'.join([groups[5], groups[7], groups[9]])
    matches.append(phoneNumber)
for groups in mailRegex.findall(text):
    matches.append(groups)

if(len(matches)>0):
    text = '\n'.join(matches)
else:
    text = 'Телефонные номера и электронные адреса не найдены'

pyperclip.copy(text)     #копировать в буфер обмена