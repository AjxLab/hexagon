# -*- coding: utf-8 -*-

from janome.tokenizer import Tokenizer

# 形態素解析でトークン化
tokenizer = Tokenizer()

def make_reply(text):
    ## -----*-----  -----*----- ##
    if text[-1] != "。": text += "。"
    words = tokenizer.tokenize(text)

    # 単語毎にループ
    for w in words:
        face = w.surface                    # 単語
        ps = w.part_of_speech.split(',')[0] # 品詞
        print(w.part_of_speech.split(','))


print(make_reply('私の名前は阿部健太朗です。'))
