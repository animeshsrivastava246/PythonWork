#import main1,main2,main3,main4,main5
#def generator_func(N):
#    for i in range(N):
#        yield i**3
#g=generator_func(10)
#next(g)
#next(g)
#print(next(g))

#def special_for(iterable):
#    iterator = iter(iterable)
#    while True:
#        try:
#            print(next(iterator)**3)
#            print(iterator)
#        except StopIteration:
#            print('End!')
#            break
#special_for([1,2,3])

#class MyGen():
#    def __init__(self, first=0, last=0):
#        self.first = first
#        self.last = last
#    def __iter__(self):
#        return self
#    def __next__(self):
#        if self.first <= self.last:
#            n=self.first
#            self.first+=1
#            return n
#        raise StopIteration
#gen=MyGen(1,2)
#for i in gen:
#    print(i**2)

#def fib(num):
#    a=0
#    b=1
#    for i in range(num):
#        yield a
#        temp=a
#        a=b
#        b+=temp
#        i+=1
#for x in fib(20):
#    print(x)

#import random
#print(random.randint(1,6))
#print(random.choice([1,2,3,4,5,6]))
#my_list=[1,2,3,4,5,6]
#random.shuffle(my_list)
#print(my_list)

#import random as xyz
#print(xyz.randint(1,6))
#print(xyz.choice([1,2,3,4,5,6]))
#my_list=[1,2,3,4,5,6]
#xyz.shuffle(my_list)
#print(my_list)

#from random import shuffle as abc
#my_list=[1,2,3,4,5,6]
#abc(my_list)
#print(my_list)

#import sys
#sys.argv
#print(sys)

#import pyjokes
#joke = pyjokes.get_joke('en','adult')
#print(joke)

#from collections import Counter,defaultdict,OrderedDict
#li=[1,4,6,7,7,8,8,8,9,10]
#sent="My name is khan and I'm not a terrorist"
#print(Counter(li))
#print(Counter(sent))
#diction=defaultdict(lambda:'Item does not exist',{'a':2,'b':4,'c':6})
#print(diction['b'])
#print(diction['x'])
#d={'c':100}#d=OrderedDict()
#d['a']=1
#d['b']=2
#d1={'c':100}#d1=OrderedDict()
#d1['b']=2
#d1['a']=1
#print(d==d1)

#import datetime
#print(datetime.time())
#print(datetime.time(23,59,51))
#print(datetime.date(2003,10,25))
#print(datetime.date.today())

#from array import array
#arr=array('i',[0,1,2,3,4,5])
#print(arr[4])