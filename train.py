# -*- coding: utf-8 -*-
from janome.tokenizer import Tokenizer
import os, re, json, random, glob
from tqdm import tqdm


# マルコフ連鎖の辞書を作成 --- (※1)
def make_dic(words):
    tmp = ['@']
    dic = {}
    for i in words:
        word = i.surface
        if word == '' or word == '\r\n' or word == '\n': continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word == '。':
            tmp = ['@']
            continue
    return dic


# 三要素のリストを辞書として登録 --- (※2)
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1


# 作文する --- (※3)
def make_sentence(dic):
    ret = []
    if not '@' in dic: return 'no dic'
    top = dic['@']
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == '。': break
        w1, w2 = w2, w3
    return ''.join(ret)


def word_choice(sel):
    keys = sel.keys()
    return random.choice(list(keys))


dict_file = 'model/dict.json'

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


