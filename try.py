#-*- codeing = utf-8 -*-
#@Time : 2020/5/13 14:36
#@Author : 于璐
#@File : try.py
#@Software : PyCharm

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np


def main():
    # +++your code here+++
    '''1.准备分词'''
    text = open('./weiboComment.txt', encoding= 'utf-8').read()
    cut = jieba.cut(text)
    string = ' '.join(cut)
    print(len(string))  # 显示一下有多少分词

    '''2.准备好用来遮罩的图片'''

    img = Image.open(r'.\static\anotherheart.jpg')  #当前程序所在文件下面的路径
    img_array = np.array(img)                          
    wc = WordCloud(                                    
            background_color = 'white',                
            mask = img_array,
            font_path = "simhei.ttf"                  
            )
    wc.generate_from_text(string)    


    '''3.绘制图片'''

    fig = plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')

    wc.to_file(r'.\static\WeiboWordCloud.jpg')


if __name__ == '__main__':
    main()