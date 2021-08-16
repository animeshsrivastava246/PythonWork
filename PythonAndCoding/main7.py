#import pdb
#def add(N1,N2):
#    pdb.set_trace()
#    x=4*5
#    return N1+N2
#print(add(4,'adfaf'))

#my_file=open('testfile.txt')
#print(my_file.read())
#my_file.seek(0)
#print(my_file.read())
#my_file.seek(0)
#print(my_file.read())
#my_file.close()

#my_file=open('testfile2.txt')
#print(my_file.readlines())#print(my_file.readline())
#print(my_file.readline())
#print(my_file.readline())
#my_file.close()

#with open('D:/Movies & Web Series/xyz.txt',mode='r') as my_file:
#    print(my_file.read())

#try:
#    with open('xyz.txt',mode='x') as my_file:
#        print(my_file.read())
#except FileNotFoundError as err:
#    print('File doesn\'t exist')
#    #raise err
#except IOError as err:
#    print('IO Error')
#    #raise err
#except ValueError as err:
#    print('Value Error')
#    #raise err

#import re
#pattern=re.compile('str')
#string='str means it is a string means text'
#print('str' in string)
#a=pattern.search(string)
#b=pattern.findall(string)
#c=pattern.fullmatch(string)
#d=pattern.match(string)
#print(a,'\n',b,'\n',c,'\n',d)
#a=re.search('means', string)
#print(a.span())
#print(a.start())
#print(a.end())
#print(a.group())
#pattern = re.compile(r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$')
#string=str(input('Enter email\n'))
#em=pattern.search(string)
#print(em)
#pattern1 = re.compile(r"[a-zA-Z0-9@$%#+-.,;!]{8,}\d")
#pwrd='wxyz@1234'
#check=pattern1.fullmatch(pwrd)
#print(check)

#from PIL import Image,ImageFilter
#imag=Image.open('D:/Important/Animesh Srivastava.jpg')
#-imag.thumbnail((720,400))
#-imag.show()
#imag.crop((2250,2250,4100,4100)).show()
#imag.resize((250,250)).show()
#imag.rotate(-45).show()
#imag.show()
#print(imag)
#print(imag.format)
#print(imag.size)
#print(imag.mode)
#filtered_img=imag.convert('L')#filtered_img=imag.filter(ImageFilter.BLUR)
#filtered_img.save('grey_anni.png','png')