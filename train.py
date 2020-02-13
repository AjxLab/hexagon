# -*- coding: utf-8 -*-
import os, re, json, random, glob
from engine import *
from janome.tokenizer import Tokenizer
from tqdm import tqdm


print('テキストを読み込み')
for file in tqdm(glob.glob('data/wiki/*')):
    text = open(file, 'r', encoding='utf-8', errors='ignore').read()
    # 不要な部分を削除
    text = re.sub(r'\*\[\[.+\]\]', '', text)
    text = re.sub(r'=+.+=+', '', text)

# 形態素解析
t = Tokenizer()
sentences = text.split('\n')
words = []
print('')
print('単語に分割')
for s in tqdm(text.split('\n')):
    words.extend(t.tokenize(s))

# 辞書を生成
dic = make_dic(words)
json.dump(dic, open(dict_file, 'w', encoding='utf-8'))


# 作文 --- (※6)
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print('---')


