Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'Somsak'
age = 12
age == 12
True
if age == 12:
    print('สามารถเรียนห้อง ป.5')

    
สามารถเรียนห้อง ป.5
if age != 12:
    print("ต้องไปเรียนห้องอื่น")

    
agr != 12
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    agr != 12
NameError: name 'agr' is not defined. Did you mean: 'age'?
age !=12
False
age = 15
if age != 12:
        print("ต้องไปเรียนห้องอื่น")

        
ต้องไปเรียนห้องอื่น
age = 18
if age > 12:
    print('คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง')

    
คุณต้องไปถามครูว่าเรียนชั้นไหนได้บ้าง
age = 12
if age > 12
SyntaxError: incomplete input
if age > 12:
    print('ห้องนี้รับอายุ 12 ขวบขึ้นไป คุณเข้าได้')

    
if age >= 12:
    print('ห้องนี้รับอายุ 12 ขวบขึ้นไป คุณเข้าได้')

    
ห้องนี้รับอายุ 12 ขวบขึ้นไป คุณเข้าได้
age = 7
if age < 12:
    print('ต้องเรียน ป.4 ลงไปเท่านั้น')

    
ต้องเรียน ป.4 ลงไปเท่านั้น
if age <= 12:
    print('ต้องเรียน ป.4 ลงไปเท่านั้น')

    
ต้องเรียน ป.4 ลงไปเท่านั้น
age = 12
if age <= 12:
    print('ต้องเรียน ป.4 ลงไปเท่านั้น')

    
ต้องเรียน ป.4 ลงไปเท่านั้น
garage = ['toyota','isuzu','benz']
car = 'toyota'
car in garage
True
if car in garage:
    print('รถคันนี้อยู่ในโรงรถลุง')

    
รถคันนี้อยู่ในโรงรถลุง
car = bmw
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    car = bmw
NameError: name 'bmw' is not defined
car = 'bmw'

if car in garage:
        print('รถคันนี้อยู่ในโรงรถลุง')

        

student = True
check = False
mobile = {'loong':'0801234455','somsak':'081111'}
'loong' in mobile
True
listcheck = mobile.value()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    listcheck = mobile.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
listcheck = mobile.valuse()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    listcheck = mobile.valuse()
AttributeError: 'dict' object has no attribute 'valuse'. Did you mean: 'values'?
listcheck = mobile.values()
print(listcheck)
dict_values(['0801234455', '081111'])
'0801234455' in listcheck
True
'Audi' ==  'audi'
False
'Audi'.lower() == 'audi'
True
True and True
True
>>> True and False
False
>>> True or False
True
>>> True or True
True
>>> money = 200
>>> style = 'japanese'
>>> if money >= 200 and style == 'japanese':
...     print('คุณสามารถเข้าร้านได้จ้า')
... 
...     
คุณสามารถเข้าร้านได้จ้า
>>> stylecheck = ['japanese','thai','chinese']
>>> if money >= 200 and style in stylecheck:
...     print('คุณสามารถเข้าร้านได้จ้า')
... 
...     
คุณสามารถเข้าร้านได้จ้า
>>> 
>>> def checkstyle(style,money):
...     stylecheck = ['japanese','thai','chinese']
...     if money >= 200 and style in stylecheck:
...         print('คุณสามารถเข้าร้านได้จ้า')
...     elif syle not in stylecheck and money >= 300:
...         print('ตุณต้องซื้อชุดร้านเราในราคา 100 บาทถึงจะเข้าได้')
...     else:
...         print('ขออภัยค่ะ ทางเราไม่สามารถให้เข้าได้')
... 
...         
>>> checkstyle('japanese',400)
คุณสามารถเข้าร้านได้จ้า
>>> checkstyle('thai',400)
คุณสามารถเข้าร้านได้จ้า
>>> checkstyle('western',400)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    checkstyle('western',400)
  File "<pyshell#79>", line 5, in checkstyle
    elif syle not in stylecheck and money >= 300:
NameError: name 'syle' is not defined. Did you mean: 'style'?
>>> checkstyle('western',600)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    checkstyle('western',600)
  File "<pyshell#79>", line 5, in checkstyle
    elif syle not in stylecheck and money >= 300:
NameError: name 'syle' is not defined. Did you mean: 'style'?
>>> def checkstyle(style,money):
...     stylecheck = ['japanese','thai','chinese']
...     if money >= 200 and style in stylecheck:
...         print('คุณสามารถเข้าร้านได้จ้า')
...     elif style not in stylecheck and money >= 300:
...         print('ตุณต้องซื้อชุดร้านเราในราคา 100 บาทถึงจะเข้าได้')
...     else:
...         print('ขออภัยค่ะ ทางเราไม่สามารถให้เข้าได้')
... 
...         
>>> checkstyle('western',600)
ตุณต้องซื้อชุดร้านเราในราคา 100 บาทถึงจะเข้าได้
