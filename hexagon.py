# -*- coding: utf-8 -*-

import os
import shutil
import engine

logo = \
'''
H    H  EEEEEE  X   X   AAAA    GGGG    OOOO   N   N
H    H  E        X X   AA  AA  G    G  O    O  NN  N
HHHHHH  EEEEEE    X    AAAAAA  G       O    O  N N N
H    H  E        X X   AA  AA  G  GGG  O    O  N  NN
H    H  EEEEEE  X   X  AA  AA   GGGGG   OOOO   N   N
'''
len_logo = len(logo.split('\n')[1])
width = shutil.get_terminal_size()[0]
logo = [' '*((width-len(line))//2) + line for line in logo.split('\n')]
logo = '\n'.join(logo)

os.system('clear')
print('''
     Welcome to

%s


     HEXAGON is an interactive chatbot.
     This implementation by Tatsuya Abe 2020.



''' % logo)


msg = '話しかけてください。'
while True:
    print('   HEXAGON： %s' % msg)
    text = input('   You：     ')
    msg = engine.make_reply(text)
