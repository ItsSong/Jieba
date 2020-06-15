#!/usr/bin/env python
#-*- coding = utf-8 -*-
def getText():   #获取文本
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()   #将所有字母变成小写
    for ch in '|"#$%&()*+,-./:;<=>?@[\\]^_‘{|}':    #查找特殊符号替换掉
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()   #分隔，并以列表形式返回
counts = {}  #定义空字典
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))