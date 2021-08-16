#from functools import reduce
#my_list=[1,2,3]
#your_list=[7,8,9]
#def two_times(item):
#    return item*2
#def only_even(item):
#    return item%2==0
#def accumulator(acc, item):
#    print(acc, item)
#    return acc+item
#print(list(map(two_times, my_list)))#ORprint(list(map(lambda item: item*2, my_list))) #No need of two_times function then
#print(list(filter(only_even, my_list)))
#print(list(zip(my_list, your_list)))
#print(reduce(accumulator, my_list, 0))
#print(my_list)

#a=[(0,2),(4,3),(10,-1),(9,7),(8,5)]
#a.sort()
#print(a)
#a.sort(key=lambda i: i[1])#sort by 2nd value
#print(a)

#my_list1 = [char for char in 'ANIMESH']
#my_list2 = [num for num in range(1,101)]
#my_list3 = [num**2 for num in range(1,101)]
#my_list4 = [num**2 for num in range(1,101) if num%2==0]
#diction = {'a':2,'b':3}
#my_dict1 = {key:val**2 for key,val in diction.items() if val%2!=0}
#my_dict2 = {n:n**3 for n in (1,2,3)}
#print(my_dict2)

# some_list=['a','b','c','b','d','n','e','n']
# duplicates=[]
# for value in some_list:
#    if some_list.count(value)>1:
#        if value not in duplicates:
#            duplicates.append(value)
# duplicates = list(set([x for x in some_list if some_list.count(x)>1]))
# print(duplicates)

#def my_decorator(func):
#    def wrap_func(*args, **kwargs):
#        print('**********')
#        func(*args, **kwargs)
#        print('**********')
#    return wrap_func
#@my_decorator
#def hi(greet='Hi', emoji=':)'):
#    print(greet, emoji)
#hi('Hello anni', '🤗')

#from time import time
#def performance(fn):
#    def wrap(*args, **kwargs):
#        t1 = time()
#        result = fn(*args, **kwargs)
#        t2 = time()
#        print(f'It took {t2-t1} sec')
#        return result
#    return wrap
#@performance
#def LongTime():
#    for i in range(100000000):
#        i*5
#LongTime()

#while True:
#    try:
#        age=int(input("Enter Your Age:"))
#        print(f'You are {age} years old.')
#        1/age
#    except ValueError:
#        print('Please enter a number!')
#    except ZeroDivisionError:
#        print('Please enter age other than zero(0)')
#    else:
#        print('Thank You!')
#        break
#    finally:
#        print('Okay')

#def operate(n1, n2):
#    try:
#        return (n1 + n2)/n2
#    except (TypeError, ZeroDivisionError) as err:
#        print(f'Something went wrong, {err}')
#print(operate(1,0))
#print(operate('1','2'))
#print(operate(2,2))

#while True:
#    try:
#        age=int(input('Your age?'))
#        2/age
#        raise Exception('Hey, end it right now!')
#    except ZeroDivisionError:
#        print('Please enter age other than zero(0)')
#        break
#    else:
#        print('Thanks!')
#    finally:
#        print('Okay')
#    print('Hear this?')