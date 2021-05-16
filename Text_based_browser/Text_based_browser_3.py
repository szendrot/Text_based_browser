
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here

import sys
import os
from  collections import deque

dir = sys.argv[1]
lista = ['bloomberg.com', 'nytimes.com']
my_stack = deque()

if os.path.isdir(dir):
    None
else:
    os.mkdir(dir)

while True:
    URL = input()
    URL_m = URL.replace('.com','')
    if URL == 'nytimes.com':
        with open(f'{dir}/{URL_m}', 'w') as file:
            file.write(nytimes_com)
            my_stack.append(URL_m)
            print(nytimes_com)
    elif URL == 'nytimes':
        if 'nytimes.txt' in os.listdir(dir):
            file = open(f'{dir}/{URL_m}', 'r')
            for line in file:
                print(line.strip())
            my_stack.append(URL_m)
        else:
            print('Error: Incorrect URL')
    elif URL == 'bloomberg.com':
        with  open(f'{dir}/{URL_m}', 'w') as file:
            file.write(bloomberg_com)
            my_stack.append(URL_m)
            print(bloomberg_com)
    elif URL == 'bloomberg':
        if 'bloomberg.txt' in os.listdir(dir):
            with open(f'{dir}/{URL_m}', 'r') as file:
                for line in file:
                    print(line.strip())
                my_stack.append(URL_m)
        else:
            print('Error: Incorrect URL')
    elif URL == 'back':
        if my_stack != deque([]):
            my_stack.pop()
            back = my_stack.pop()
            with open(f'{dir}/{back}', 'r') as file:
                for line in file:
                    print(line.strip())
        else:
            None
    elif URL == 'exit':
        break
    elif URL not in lista:
        print('Error: Incorrect URL') 
  

