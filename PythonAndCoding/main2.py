#li=[1,2,3.5,'A',"Hey",True](List OR ARRAY) we can have multidimensional arrays(Lists) also
#Data Structure
#amz_cart=['Laptop','mobile','tablet']
#amz_cart[0]='Notebook'
#print(amz_cart[::])

#basket=[1,2,3,4,5]
#basket.append(100)
#basket.insert(3,100)
#basket.pop()
#basket.pop(3)
#basket.remove(2)
#print(basket)

#drawer=['a','b','c','k','d','e','e']
#print('d' in drawer)
#print('f' in drawer)
#print(drawer.count('e'))
#drawer.sort() OR print(sorted(drawer))
#print(drawer)

#print(list(range(1,100)))
#print(list(range(100)))

#sent=' '
#new_sent= sent.join(['Hi',',','my','name','is','Animesh'])
#new_sent= ' '.join(['Hi',',','my','name','is','Animesh'])
#print(new_sent)

#a,b,c,d=1,2,3,4
#print(a,b,c,d)

#a,b,c,*other,d=[1,2,3,4,5,6,7,8,9]
#print(a,b,c)
#print(other)
#print(d)

#weapons=None
#print(weapons)

#dictionary={'a':[1,2,3.5],'b':"Hello buddy",'y':True,123:'1 2 3',(1,2):[1,2,3]}
#print(dictionary['b'])
#print(dictionary['a'][2])
#my_list=[{'a':[1,2,3.5],'b':"Hello buddy",123:True},{'a':[4,5,6.5],True:"Hello buddy",'y':True,(1,2):[7,8,9]}]
#print(my_list[1]['a'][1])

#user={'basket':[1,2,3],'greeting':'Hello World','age':20}
#print(user.get('age',55))
#user2=dict(name="Johny")
#print(user2)

#my_tuple=(1,'a',"Hello world!",24,'x')
#print(my_tuple[3])

#my_list=[1,2,3,4,5,5]
#my_set1=set(my_list)
#print(my_set1)
#my_set={1,3,4,5,5}
#my_set.add(100)
#my_set.add(2)
#print(my_set)

#is_old=True
#is_licenced=True
#if is_old and is_licenced:
    #print("You are eligible to drive")
#elif is_old:
    #print("You don't have license")
#else:
    #print("You are not permitted to drive")

#is_friend=True
#can_msg="Messages allowed" if is_friend else "Messages not allowed"
#print(can_msg)

#is_frnd=True
#is_user=True
#if is_frnd or is_user:
#    print("BFF")
#else:
#    print("Not BFF")

#for i in [1,2,3,4,5]:
#    for j in ['a','b','c']:
#        print(i,j)
#print(i,j)

#user={'name':'Shivam','age':999999,'can_dance':False}
#for key,value in user.items(): print(key,value)
#for value in user.values(): print(value)
#for key in user.keys(): print(key)

#for i in range(0,10,2):
#    print(i)
#    print('Animesh')

#for i,char in enumerate(list(range(20))):
#    if char == 15:
#        print(f'Index of 15 is :{i}')

#i=0
#while i<=20:
#    print(i)
#    i+=2
#    break
#    continue
#else:
#    print("End of program")

#for item in [1,2,3]:
#    pass