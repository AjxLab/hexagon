# -*- coding: utf-8 -*-
from gensim.models.word2vec import Word2Vec

model = Word2Vec.load('model/wiki.model')

print(model.wv.most_similar(positive=['テスト']))


