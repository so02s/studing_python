#! python3
# -*- coding: cp1251 -*-
# PasswordChecker - проверка, силен ли пароль
import re, pyperclip

#получение пароля из буфера обмена
text = str(pyperclip.paste())

#необходимые шаблоны
passwordRegex = re.compile(r'.{8,}')
haveNumber = re.compile(r'\d')
haveUpper = re.compile(r'[A-Z]')
haveLower = re.compile(r'[a-z]') 

#проверка
password = passwordRegex.search(text)
if password != None:
    if haveUpper.search(password.group(0)) == None :
        print('Пароль слабый, не хватает заглавных букв')
    elif haveLower.search(password.group(0)) == None :
        print('Пароль слабый, не хватает маленьких букв')
    elif haveNumber.search(password.group(0)) == None :
        print('Пароль слабый, не хватает цифр')
    else:
       print('Пароль сильный')
