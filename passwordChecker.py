#! python3
# -*- coding: cp1251 -*-
# PasswordChecker - ��������, ����� �� ������
import re, pyperclip

#��������� ������ �� ������ ������
text = str(pyperclip.paste())

#����������� �������
passwordRegex = re.compile(r'.{8,}')
haveNumber = re.compile(r'\d')
haveUpper = re.compile(r'[A-Z]')
haveLower = re.compile(r'[a-z]') 

#��������
password = passwordRegex.search(text)
if password != None:
    if haveUpper.search(password.group(0)) == None :
        print('������ ������, �� ������� ��������� ����')
    elif haveLower.search(password.group(0)) == None :
        print('������ ������, �� ������� ��������� ����')
    elif haveNumber.search(password.group(0)) == None :
        print('������ ������, �� ������� ����')
    else:
       print('������ �������')
