number = 3 

for i in range(1,11):
    if i == 5:  # this will skip this steps in answer
        continue 
    print(number, 'x', i,'=',number * i)