#!python3
# -*- coding: cp1251 -*-
#PhoneAndMailFinder - ���� ��� �������� �
#����������� ������ � ������ ������

import pyperclip, re

#�������� �� ������ ������
text = str(pyperclip.paste())

#������ ��� ���������
phoneRegex = re.compile(r'''(
(\d?)          #������
(\(|\s)?       #������
(\d{3})        #��� �����
(\)|\s)?       #������
(\d{3})        #��� �����
(\s|-|\.)      #�����������
(\d{2})        #��� �����
(\s|-|\.)      #�����������
(\d{2})        #��� �����
)''', re.VERBOSE)

#������ ��� ����������� �������
mailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+        #��� ������������
@                        #������
[a-zA-Z0-9-]+            #�����
\.                       #�����
[a-zA-Z]+                 #��� ������
)''', re.VERBOSE)

#�������� �� ������ � �������� ��� ���������
matches = []
for groups in phoneRegex.findall(text):
    phoneNumber = groups[1] + '(' + groups[3] + ')' + '-'.join([groups[5], groups[7], groups[9]])
    matches.append(phoneNumber)
for groups in mailRegex.findall(text):
    matches.append(groups)

if(len(matches)>0):
    text = '\n'.join(matches)
else:
    text = '���������� ������ � ����������� ������ �� �������'

pyperclip.copy(text)     #���������� � ����� ������