#/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import subprocess as cmd

import fasttext as ft
from natto import MeCab

def main(text):
    """
    MeCabで分かち書きした後に作成したモデルを読み込み、判定
    MeCabのneologdの保存されているpathはmacなら大抵ここになるはずではあるが、エラーが出た際は調べて修正してください。
    """
    nm = MeCab("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    words = nm.parse(text)
    print('\n', words)

    classifier = ft.load_model('./model.bin')
    estimate = classifier.predict([words], k=2)
    estimate_2 = classifier.predict_proba([words], k=2)
    print('estimate:', estimate_2[0][0][1])
    if estimate[0][0] == '__label__2,':
        return ['ネガティブ', str(estimate_2[0][0][1])]
    elif estimate[0][0] == '__label__1,':
        return ['ポジティブ', str(estimate_2[0][0][1])]

if __name__ == '__main__':
    print(main('テラス限定のBBQを予約していましたが、同僚から外はいやとの声が上がり当日に席とコースを急きょ変更対応して頂きました。転送で昼から電話がつながり助かりました。ありがとうございました！'))
