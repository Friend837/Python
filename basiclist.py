Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
cars = ['toyota','honda','benz']
car.append('byd')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    car.append('byd')
NameError: name 'car' is not defined. Did you mean: 'cars'?
cars.append('byd')
print(cars)
['toyota', 'honda', 'benz', 'byd']
cars.remove('honda')
print(cars)
['toyota', 'benz', 'byd']
cars.insert(0,'tesla')
print(cars)
['tesla', 'toyota', 'benz', 'byd']
print(cars[0])
tesla
print(cars[1])
toyota
for c in cars:
    print(c)

    
tesla
toyota
benz
byd
print(*cars)
tesla toyota benz byd
for i,c in enumerate(cars):
    print(i,c)

    
0 tesla
1 toyota
2 benz
3 byd
for i,c in enumerate(cars, start=0):
    print('ลำดับ {} {}'.format(i,c))

    
ลำดับ 0 tesla
ลำดับ 1 toyota
ลำดับ 2 benz
ลำดับ 3 byd
for i,c in enumerate(cars, start=1):
    print('ลำดับ {} {}'.format(i,c))

    
ลำดับ 1 tesla
ลำดับ 2 toyota
ลำดับ 3 benz
ลำดับ 4 byd
car[1] = 'isuzu'
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    car[1] = 'isuzu'
NameError: name 'car' is not defined. Did you mean: 'cars'?
\
cars[1] = 'isuzu'
del cars[2]
len(cars)
3
ord('ก')
3585
ord('ข')
3586
ord('ฃ')
3587
chr(3587)
'ฃ'
chr(3589)
'ฅ'
for i in range(10)
SyntaxError: incomplete input
>>> for i in range(10):
...     print(chr(3585+i))
... 
...     
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
>>> for i in range(3585,3595):
...     print(chr(i))
... 
...     
ก
ข
ฃ
ค
ฅ
ฆ
ง
จ
ฉ
ช
>>> number = {'1001':'สมชาย':'1002':,'1003':'สมศุกดิ์'}
SyntaxError: invalid syntax
>>> number = {'1001':'สมชาย','1002':'สมศรี','1003':'สมศุกดิ์'}
>>> number = {'1001':'สมชาย','1002':'สมศรี','1003':'สมศุกดิ์'}
>>> print(number['1001'])
สมชาย
>>> for n in number:
...     print(n)
... 
...     
1001
1002
1003
for n in number.item():
    print(n)

    
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for n in number.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
for n in number.items():
    print(n)

    
('1001', 'สมชาย')
('1002', 'สมศรี')
('1003', 'สมศุกดิ์')
for n in number.items():
    print(n[1])

    
สมชาย
สมศรี
สมศุกดิ์
for n in number.keys():
    print(n)

    
1001
1002
1003
for n in number.values():
    print(n)

    
สมชาย
สมศรี
สมศุกดิ์

def hello:
    
SyntaxError: incomplete input
def hello():
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')
    print('hello world')

    
hello()
hello world
hello world
hello world
hello world
hello world
def hello(q):
    for i in range(q):
        print('hello world')

        
hello(1)
hello world
hello(10)
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
hello world
