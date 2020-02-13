# -*- coding: utf-8 -*-
import os, re, json, random, glob
from engine import *
from janome.tokenizer import Tokenizer
from tqdm import tqdm


def make_dic(words):
    ## -----*----- マルコフ連鎖の辞書を作成 -----*----- ##
    tmp = ["@"]
    dic = {}
    for i in words:
        word = i.surface
        if word == "" or word == "\r\n" or word == "\n": continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == "。":
            tmp = ["@"]
            continue

    return dic


print('テキストを読み込み')
for file in tqdm(glob.glob('data/wiki/*')):
    text = open(file, 'r', encoding='utf-8', errors='ignore').read()
    # 不要な部分を削除
    text = re.sub(r'\*\[\[.+\]\]', '', text)
    text = re.sub(r'\[\[.+\]\]', '', text)
    text = re.sub(r'=+.+=+', '', text)
    text = re.sub(r'.*\*.*\n', '', text)

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


