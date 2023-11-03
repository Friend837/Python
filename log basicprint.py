Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello world')
Hello world
>>> print('Hello world')
Hello world
>>> 
>>> name = 'Friend'
>>> name = 'Danaiwat'
>>> lastname = 'Sittanapong'
>>> fullname = name + '' + lastname
>>> print(fullname)
DanaiwatSittanapong
>>> fullname = name + ' ' + lastname
>>> print(fullname)
Danaiwat Sittanapong
>>> fullname = name + \n + lastname
SyntaxError: unexpected character after line continuation character
>>> type(name)
<class 'str'>
>>> age = 23
>>> type(age)
<class 'int'>
>>> name = 'Danaiwat'
>>> name.upper()
'DANAIWAT'
>>> name.lower()
'danaiwat'
>>> print(name)
Danaiwat
>>> name = name.upper()
>>> print(name)
DANAIWAT
>>> number = '1'
>>> number.zfill(5)
'00001'
>>> number = '15'
>>> number.zfill(5)
'00015'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ{} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อDANAIWAT นามสกุลSittanapong อายุ23 ขวบ
>>> print('ลุงครับผมชื่อ {} นามสกุล {} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อ DANAIWAT นามสกุล Sittanapong อายุ 23 ขวบ
>>> print(f'ลุงครับผมชื่อ {name} นามสกุล {lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อ DANAIWAT นามสกุล Sittanapong อายุ 23 ขวบ
