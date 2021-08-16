# pic=[
#    [0,0,0,1,0,0,0],
#    [0,1,1,1,1,1,0],
#    [0,1,1,1,1,1,0],
#    [1,1,1,1,1,1,1],
#    [0,1,1,1,1,1,0],
#    [1,1,1,1,1,1,1],
#    [0,0,0,1,0,0,0],
#    [0,0,0,1,0,0,0]]
# for row in pic:
#    for pixel in row:
#        if pixel: print('*',end='')
#        else: print(' ',end='')
#    print('')

# some_list=['a','b','c','b','d','n','e','n']
# duplicates=[]
# for value in some_list:
#    if some_list.count(value)>1:
#        if value not in duplicates:
#            duplicates.append(value)
# print(duplicates)

# def say_hi():
#    print('Hiiiiii')
# say_hi()

# def say_hi(name,emoji,emoji2):
#    print(f'Hiiiiii {name} {emoji} {emoji2}')
# say_hi('Anni','😉','😁')
# say_hi(emoji2='😁',emoji='😉',name='Anni')

# def say_hi(name='Don',emoji='😎',emoji2='😈'):
#    print(f'Hiiiiii {name} {emoji} {emoji2}')
# say_hi('Anni','😉','😁')
# say_hi(emoji2='😁',emoji='😉',name='Anni')
# say_hi()

# def add(N1,N2):
#    def another_add(n1,n2):
#        return n1+n2
#    return another_add(N1,N2)
#    print('Hello') #Won't execute
# print(add(10,15))

# def your_name(x):
#    #Docstrings
#    '''
#    Info: This function prints your name
#    '''
#    print(x)
# print(your_name.__doc__)
# help(your_name)

# def sup_func(*args,**kwargs):
#    total=0
#    for items in kwargs.values():
#        total+=items
#    return sum(args)+total
# print(sup_func(1,2,3,4,5,N1=10,N2=3,N3=2))

# def max_even(li):
#    evens=[]̥̥̥̥
#    for item in li:
#        if item%2==0:
#            evens.append(item)
#    return max(evens)
# print(max_even([2,10,4,5,7,11,8,14,3]))

# a='Anniiiiiiiiiii'
# if ((n:=len(a))>10): #Walrus operator
#    print(f'Too long, {n} elements')
# while ((n:=len(a))>4):  #Walrus operator
#    print(a)
#    a=a[:-1]

# total=0
# def incr():
#    global total     #OR incr(total)
#    total+=1
#    return total
# print(incr())        #OR incr(total)

# def outer():
#    x = "local"
#    def inner():
#        #nonlocal x
#        x = "nonlocal"
#        print("inner:", x)
#    inner()
#    print("outer:", x)
# outer()
