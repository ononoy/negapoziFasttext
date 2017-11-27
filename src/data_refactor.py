#!/bin/env python
# -*- coding:utf-8 -*-

import os

from natto import MeCab


nm = MeCab("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
labeled = []

def main():
    """
    データの取得、ラベル付けと分かち書き
    """
    data_list = os.listdir('./../ml_data')
    for data in data_list:
        if data == 'posi.txt':
            label = '__label__1, '
        elif data == 'nega.txt':
            label = '__label__2, '
        else:
            print(data,'pass')
            continue
        with open('./../ml_data/'+data) as f:
            lines = f.readlines()
        for l in lines:
            labeled.append(refactor(label, l))
    with open('./../ml_data/label_negaposi.lst', 'w') as f:
        f.write('\n'.join(labeled))

def refactor(label, text):
    """
    分かち書きしてラベルを付して返す
    """
    wakatied = nm.parse(text)
    return label + wakatied

if __name__ == '__main__':
    main()
