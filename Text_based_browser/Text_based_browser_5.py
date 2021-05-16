import os
from collections import deque

import requests

from bs4 import BeautifulSoup

file_dir = sys.argv[1]
my_stack = deque()
if os.path.isdir(file_dir):
    None
else:
    os.mkdir(file_dir)
while True:
    URL = input().lstrip('https://')
    URL_m = URL.replace('.org', '-').replace('.com', '-')
    URL_name = URL.replace('.com', '').replace('.org', '')

    if URL == 'back':
        if my_stack != deque([]):
            my_stack.pop()
            back = my_stack.pop()
            with open(f'{file_dir}/{back}', 'r') as file:
                for line in file:
                    print(line.strip())
    elif URL == 'exit':
        break
    elif URL_m.count('-') != 1:
        print('Incorrect URL')
    elif URL_m.count('-') == 1:
        r = requests.get('https://' + URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        p_a_ul_ol_li = soup.find_all(['p', 'a', 'ul', 'ol', 'li'] )
        if r:
            if URL_name not in os.listdir(file_dir):
                with open(f'{file_dir}/{URL_name}', 'w', encoding='utf-8') as file:
                    file.write(soup.get_text('\n', True))
                    my_stack.append(URL_name)
                    print(soup.get_text('\n', True))
            elif URL in os.listdir(file_dir):
                file = open(f'{file_dir}/{URL_name}', 'r')
                for line in file:
                    print(line.strip())
                my_stack.append(URL_name)

    else:
        print('Incorrect URL')

