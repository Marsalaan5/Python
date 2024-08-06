import time

def cache(func):
    cache_dict = {}
    print(cache_dict)
    def wrapper(*args):
       if args in cache_dict:
           return cache_dict[args]
       result =  func(*args)
       cache_dict[args] = result
       return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(4,3))
