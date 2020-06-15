#!/usr/bin/env python
#-*- coding = utf-8 -*-
import jieba
txt = open("threekingdoms.txt","r",encoding="utf-8").read()
words = jieba.lcut(txt)   #返回列表类型的分析结果
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1   #计数
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse=True)
for i in range(15):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

