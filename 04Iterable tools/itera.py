 
# for List

# >>> myList = [1,2,3,4]
# >>> I = iter(myList)  
# >>> I
# <list_iterator object at 0x0000027AAE29B7F0>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x0000027AAE29B7F0>
# >>> I.__next__()
# 2
# >>> I
# <list_iterator object at 0x0000027AAE29B7F0>
# >>> I.__next__()
# 3
# >>> I
# <list_iterator object at 0x0000027AAE29B7F0>
# >>> I.__next__()
# 4
# >>> I
# <list_iterator object at 0x0000027AAE29B7F0>
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> 




# >>> f = open('itera.py')
# >>> iter(f) is f
# True
# >>> iter(f) is f.__iter__() 
# True
# >>> 


# >>> myList = [1,2,3]
# >>> myNewList = [1,2,3] 
# >>> iter(myNewList) is myNewList
# False
# >>> 


# for Dictionary

# >>> D = {'a':1, 'b':2}
# >>> for key in D.keys():
# ...     print(key) 
# ... 
# a
# b
# >>> 
# >>> I = iter(D)
# >>> I
# <dict_keyiterator object at 0x0000025094957290>
# >>> next(I) 
# 'a'
# >>> next(I)
# 'b'
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>> 



# >>> range(5) 
# range(0, 5)
# >>> range(0,5) 
# range(0, 5)
# >>> R = range(5) 
# >>> E
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'E' is not defined
# >>> R
# range(0, 5)
# >>> I = iter(R) 
# >>> next(I)
# 0
# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# >>>
