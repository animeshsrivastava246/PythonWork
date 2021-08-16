#import sys
#first=sys.argv[1]
#sec=sys.argv[2]
#print(f'Hellooooo!!! {first} {sec}')

from random import randint
import sys
ans=randint(int(sys.argv[1]),int(sys.argv[2]))
while True:
    try:
        guess=int(input(f'Guess a number from {sys.argv[1]} to {sys.argv[2]}:\n'))
        if int(sys.argv[1])<= guess<= int(sys.argv[2]) :
            if guess==ans:
                print('You are the winner')
                break
        else: print('Please enter a valid number')
    except ValueError:
        print('Please enter a number')
        continue