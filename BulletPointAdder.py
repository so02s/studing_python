#! python3
# BulletPointAdder.py - Добавляет перед началом
# строки маркер-звездочку

import pyperclip
text = pyperclip.paste()

#TODO: разделить строки и добавить к каждой звезду

lines = text.split('\n')       #разделить текст на строки

for i in range(len(lines)):    #пройтись по всем строкам
    lines[i] = '*' + lines[i]  #и добавить маркер
    
text = '\n'.join(lines)        #объединить обратно в текст

pyperclip.copy(text)