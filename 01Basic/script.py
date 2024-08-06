from hello import chai

chai("ginger tea")










# basic
# 
# PS D:\Python\Basic> python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> x=2 
>>> y=3
>>> z=4
>>> x+y
5
>>> 40+2.23     
42.23
>>> float(40)
40.0
>>> int(2.23)
2
>>> 'chai' + 'code'
'chaicode'
>>> x,y,z
(2, 3, 4)
>>> 
>>> import math
>>> math.floor(3.5
... math.floor(3.5)
  File "<stdin>", line 1
    math.floor(3.5
               ^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.trunc(2.8)
2
>>> math.trunce(-2.8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'trunce'. Did you mean: 'trunc'?
>>> math.trunc(-2.8)  
-2
>>> 999999999999999999999 * 2.1
2.1e+21
>>> 2+1j
(2+1j)
>>> 2+1j * 3
(2+3j)
>>> (2+1j) * 3 
(6+3j)
>>> 0o20
16
>>> oct(64)
'0o100'
>>> hex(64) 
'0x40'
>>> bin(64)
'0b1000000'
>>> int(3.14) 
3
>>> int(64) 
64
>>> int('64',8) 
52
>>> int('64',16) 
100
>>> int('1000',16)
4096
>>> int('1000',2)  
8
>>> import random    
>>> random.random()
0.7677009550859845
>>> random.random()
0.05621841934863758
>>> random.random()
0.47108895652580973
>>> random.random(int)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Random.random() takes no arguments (1 given)
>>> random.randint(1,10)  
9
>>> random.randint(1,10)
2
>>> random.randint(1,10)
5
>>> random.randint(1,10)
8
>>> random.randint(1,10)
6
>>> random.randint(1,10)
9
>>> random.randint(1,10)
6
>>> random.randint(1,10)
1
>>> random.randint(1,10)
10
>>> li = ['lemon','ginger','masala']  
>>> random.choice(l1) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l1' is not defined. Did you mean: 'li'?
>>> random.choice(l1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l1' is not defined. Did you mean: 'li'?
>>> l1 = ['lemon','ginger','masala']       
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'lemon'
>>> random.choice(l1)
'masala'
>>> random.choice(l1)
'ginger'
>>> random.shuffle(l1)
>>> l1
['masala', 'ginger', 'lemon']
>>> l1
['masala', 'ginger', 'lemon']
>>> l1
['masala', 'ginger', 'lemon']
>>> l1
['masala', 'ginger', 'lemon']
>>> random.shuffle(l1)
>>> l1
['masala', 'lemon', 'ginger']
>>> 0.1 + 0.1 + 0.1
0.30000000000000004
>>> 0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
>>> from decimal import Decimal  
>>>                                                                          
>>>
>>>
>>>
>>>
>>> setone ={1,2,3,4} 
>>> setone & {1,3}   
{1, 3}
>>> setone | {1,3} 
{1, 2, 3, 4}
>>> setone -{1,2,3,4} 
set()
>>> type({}) 
<class 'dict'>
>>>
>>>
>>>
>>>
>>>
>>>
>>> type(True) 
<class 'bool'>
>>> True==1
True
>>> False==0
True
>>> True is 1
<stdin>:1: SyntaxWarning: "is" with 'int' literal. Did you mean "=="?
False
>>> True + 4  
5 



# String

>>> chai 
'Masala Chai'
>>> print(chai.lower) 
<built-in method lower of str object at 0x000001AA2E0C6170>  
>>> print(chai.lower())
masala chai
>>> print(chai.upper()) 
MASALA CHAI
>>> chai                
'Masala Chai'
>>>
>>>
>>> chai = "   Masala Chai   " 
>>> print(chai.strip()) 
Masala Chai
>>> chai = "Lemon  Chai"       
>>> print(chai.replace("Lemon", "Ginger")) 
Ginger  Chai
>>> chai
'Lemon  Chai'
>>> chai = "Lemon,Ginger,Masala" 
>>> print(chai.split()) 
['Lemon,Ginger,Masala']
>>> print(chai.split(",")) 
['Lemon', 'Ginger', 'Masala']
>>>      
>>>
>>>
>>>
>>> cahi = "Masala Chai"
>>> print(chai.find("Chai")) 
-1
>>> chai = "Masala Chai"     
>>> print(chai.find("Chai"))
7
>>> print(chai.find("chai")) 
-1
>>> chai = "Masala Chai Chai Chai Chai"  
>>> print(chai.count(Chai)) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Chai' is not defined. Did you mean: 'chai'? 
>>> print(chai.count("\Chai")) 
<stdin>:1: SyntaxWarning: invalid escape sequence '\C'       
0
>>> print(chai.count("Chai"))  
4
>>>
>>>
>>>
>>> chai_type "Masala"
  File "<stdin>", line 1
    chai_type "Masala"
              ^^^^^^^^
SyntaxError: invalid syntax
>>> quantity  = 2    
>>> order = "I ordered {} cups of chai" 
>>> order
'I ordered {} cups of chai'
>>> order = "I ordered {} cups of {} chai" 
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type)) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chai_type' is not defined
>>> print(order.format(quantity,chai_type))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chai_type' is not defined
>>> chai_type= "Masala" 
>>> quantity  = 2      
>>> order = "I ordered {} cups of chai"
>>> order = "I ordered {} cups of {} chai"
>>> order
'I ordered {} cups of {} chai'
>>> print(order.format(quantity,chai_type))
I ordered 2 cups of Masala chai
>>>


>>> chai_variety = ["Lemon","Masala","Ginger"] 
>>> chai_variety                              
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety"))
  File "<stdin>", line 1
    print("".join(chai_variety"))
                              ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("".join(chai_variety))  
LemonMasalaGinger
>>> print(" ".join(chai_variety)) 
Lemon Masala Ginger
>>> print("-".join(chai_variety))  
Lemon-Masala-Ginger
>>> print(", ".join(chai_variety)) 
Lemon, Masala, Ginger
>>>
>>>
>>>
>>> chai = "Masala Chai" 
>>> print(len(chai)) 
11
>>> for letter in chai:
...     print(letter) 
...
M
a
s
a
l
a

C
h
a
i
>>>
>>>
>>> chai = "He said,\"Masala chai is awesome"" 
  File "<stdin>", line 1
    chai = "He said,\"Masala chai is awesome""
                                             ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai = "He said,\"Masala chai is awesome" "
  File "<stdin>", line 1
    chai = "He said,\"Masala chai is awesome" "
                                              ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai = "He said,\"Masala chai is awesome\" " 
>>> chai = "He said,\"Masala chai is awesome\""  
>>> chai
'He said,"Masala chai is awesome"'
>>> chai
'He said,"Masala chai is awesome"'
>>> chai = "Masala Chai" 
>>> chai
'Masala Chai'
>>> chai = "Masala\nChai" 
>>> chai
'Masala\nChai'
>>> print(chai) 
Masala
Chai
>>> chai = r"c:\user\pwd\"
  File "<stdin>", line 1
    chai = r"c:\user\pwd\"
           ^
SyntaxError: unterminated string literal (detected at line 1)
>>> chai = r"c:\user\pwd"  
>>> print(chai) 
c:\user\pwd
>>> chai = "c:\user\pwd"  
  File "<stdin>", line 1
    chai = "c:\user\pwd"
           ^^^^^^^^^^^^^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
>>> chai = "c:\\user\\pwd" 
>>> print(chai) 
c:\user\pwd
>>>
>>>
>>> chai = "Masala Chai"  
>>> print("Masala" in Chai)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Chai' is not defined. Did you mean: 'chai'? 
>>> print("Masala" in chai) 
True
>>> print("Masalaa" in chai) 
False




# list

>>> tea_varieties = ["Black","Green","Oolong","White"] 
>>> tea_varieties                                     
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varieties)  
['Black', 'Green', 'Oolong', 'White']
>>> print(tea_varieties[1])  
Green
>>> print(tea_varieties[-1])  
White
>>> print(tea_varieties[1: 3])  
['Green', 'Oolong']
>>> print(tea_varieties[:2])    
['Black', 'Green']
>>> print(tea_varieties[2:])  
['Oolong', 'White']
>>> 
>>> 
>>> tea_varieties[3] = "Herbal" 
>>> print(tea_varieties)        
['Black', 'Green', 'Oolong', 'Herbal']
>>> tea_varieties[1:2] 
['Green']
>>> tea_varieties[1:2] = "Lemon" 
>>> print(tea_varieties)  
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> tea_varieties = ["Black","Green","Oolong","White"]
>>> tea_varieties
['Black', 'Green', 'Oolong', 'White']
>>> tea_varieties[1:2]          
['Green']
>>> tea_varieties[1:2] = ["Lemon"] 
>>> tea_varieties      
['Black', 'Lemon', 'Oolong', 'White']
>>> tea_varieties[1:3]
['Lemon', 'Oolong']
>>> tea_varieties[1:3] = ["Green", "Masala"]
>>> tea_varieties
['Black', 'Green', 'Masala', 'White']
>>> tea_varieties[1:1]
[]
>>> tea_varieties[1:1] = ["test","test"]
>>> tea_varieties
['Black', 'test', 'test', 'Green', 'Masala', 'White']
>>> tea_varieties[1:2]
['test']
>>> tea_varieties[1:3]
['test', 'test']
>>> tea_varieties[1:3] = []
>>> tea_varieties
['Black', 'Green', 'Masala', 'White']
>>>
>>>
>>> tea_varieties
['Black', 'Green', 'Masala', 'White']
>>> for tea in tea_varieties:
...     print(tea) 
... 
Black
Green
Masala
White
>>> 
>>> for tea in tea_varieties:
...     print(tea,end="-") 
...
Black-Green-Masala-White->>>
>>>
>>>
>>> tea_varieties
['Black', 'Green', 'Masala', 'White']
>>> if "Oolaong" in tea_varieties: 
...     print("I have Oolong tea") 
...
>>> tea_varieties .append("Oolong tea") 
>>> tea_varieties                       
['Black', 'Green', 'Masala', 'White', 'Oolong tea']
>>> if "Oolaong" in tea_varieties:
...     print("I have Oolong tea") 
...
>>> tea_varieties
['Black', 'Green', 'Masala', 'White', 'Oolong tea']
>>> if "Oolong" in tea_varieties:  
...     print("I have Oolong tea")
...
>>> if "Oolaong tea" in tea_varieties: 
...     print("I have Oolong tea")     
...
>>> tea_varieties                  
['Black', 'Green', 'Masala', 'White', 'Oolong tea']
>>> if "Oolong tea" in tea_varieties:  
...     print("I have Oolong tea")
...
I have Oolong tea
>>>
>>>
>>> tea_varieties                      
['Black', 'Green', 'Masala', 'White', 'Oolong tea']
>>> tea_varieties .pop()
'Oolong tea'
>>> tea_varieties        
['Black', 'Green', 'Masala', 'White']
>>> tea_varieties .remove("green") 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> tea_varieties .remove("Green") 
>>> tea_varieties
['Black', 'Masala', 'White']
>>> tea_varieties .insert(1,"green")  
>>> tea_varieties
['Black', 'green', 'Masala', 'White']
>>> tea_varieties_copy = tea varieties.copy()
  File "<stdin>", line 1
    tea_varieties_copy = tea varieties.copy()
                             ^^^^^^^^^
SyntaxError: invalid syntax
>>> tea_varieties_copy = tea_varieties.copy() 
>>> tea_varieties_copy                        
['Black', 'green', 'Masala', 'White']
>>> tea_varieties_copy.append("Lemon") 
>>> tea_varieties_copy
['Black', 'green', 'Masala', 'White', 'Lemon']
>>> tea_varieties     
['Black', 'green', 'Masala', 'White']
>>>



>>> squared_num =  [x**2 for x in range(10)] 
>>> squared_num                             
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_num =  [x**3 for x in range(10)]    
>>> cube_num                             
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>>



# Dictionary(Dict)

>>> tea_shop = {
... "chai": {"Masala":"Spicy","Ginger": "Zesty"},
... "Tea": {"Green":"Mild","Black":"Strong"} 
... }
>>> tea_shop     
{'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
>>> tea_shop["chai"] 
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> tea_shop["chai"]["Ginger"] 
'Zesty'
>>>
>>>
>>>
>>> squared_num = {x:x**2 for x in range(6)} 
>>> squared_num                             
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear
<built-in method clear of dict object at 0x000002221CF82480> 
>>> squared_num.clear()
>>> squared_num        
{}
>>>
>>>
>>>
>>> keys = ["Masala","Ginger","Lemon"] 
>>> keys                              
['Masala', 'Ginger', 'Lemon']
>>> dafault_value="Delicious" 
>>> new_dict = dict.fromkeys(keys,default_value) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'default_value' is not defined. Did you mean: 'dafault_value'?
>>> new_dict = dict.fromkeys(keys,default_value)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'default_value' is not defined. Did you mean: 'dafault_value'?
>>> default_value="Delicious" 
>>> new_dict = dict.fromkeys(keys,default_value)
>>> new_dict                                    
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys,keys)           
>>> new_dict                           
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
>>>



# tuple

> tea_types = ("Black","Green","Oolong") 
>>> tea_types
('Black', 'Green', 'Oolong')
>>> tea_types[0] 
'Black'
>>> tea_types[-1] 
'Oolong'
>>> tea_types[1:] 
('Green', 'Oolong')
>>> tea_types[0]  
'Black'
>>> tea_types[0] = "Lemon" 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> 
>>> len(tea_types) 
3
>>> mpre_tea = ("Herbal","Earl Grey") 
>>> all_tea = more_tea + tea_types
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'more_tea' is not defined. Did you mean: 'mpre_tea'?
>>> more_tea = ("Herbal","Earl Grey") 
>>> all_tea = more_tea + tea_types    
>>> all_tea                           
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_tea:
...     priny("I have green tea") 
...     print("I have green tea") 
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'priny' is not defined. Did you mean: 'print'?
>>> if "Green" in all_tea:        
...     print("I have green tea") 
...
I have green tea
>>> more_tea = ("Herbal","Earl Grey","Herbal") 
>>> more_tea                                  
('Herbal', 'Earl Grey', 'Herbal')
>>> more_tea.count("Herbal")                  
2
>>>
>>>
>>> tea_types   
('Black', 'Green', 'Oolong')
>>> (black,green,oolong) = tea_types       
>>> (black,green,Oolong) = tea_types 
>>> black
'Black'
>>> green
'Green'
>>> type(tea) 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tea' is not defined
>>> type(tea_types) 
<class 'tuple'>
>>>