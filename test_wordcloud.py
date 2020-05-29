#-*- codeing = utf-8 -*-
#@Time : 2020/4/29 14:28
#@Author : 于璐
#@File : test_wordcloud.py
#@Software : PyCharm


import jieba                                      #分词，把一个句子分成一个个分词
from matplotlib import pyplot as plt              #绘图，数据可视化，直接生成图片
from wordcloud import WordCloud                   #词云（有遮罩效果的图片）
from PIL import Image                             #图片处理（图形虚化 验证码 图片后期处理）
import numpy as np                                #用来做矩阵运算
import sqlite3                                    #数据库


#1、准备词云所需的文字及分词
con = sqlite3.connect('hbb.db')
cur = con.cursor()
sql = 'select content from ly'        #把表中介绍查询出来
data = cur.execute(sql)

text = ""
for item in data:
    text = text + item[0]
    print(item[0])
#print(text)
cur.close()
con.close()

#分词 5660个
cut = jieba.cut(text)
string = ' '.join(cut)   #注意中间要有空格！！！！！！不然出来的形式不对
print(len(string))


#2、准备好用来遮罩的图片
img = Image.open(r'.\static\anotherheart.jpg')  #当前程序所在文件下面的路径（打开遮罩图片）
img_array = np.array(img)                          #将图片转化为数组
wc = WordCloud(                                    #封装对象
    background_color = 'white',                    #输出图片的背景色，而不是遮罩图片的颜色
    mask = img_array,
    font_path = "simhei.ttf"                       #字体在哪里
                                                   #查找本机都有什么文字：C盘，windows,fonts,
)
wc.generate_from_text(string)                      #参数为切好的词，而不是句子


#3、绘制图片
fig = plt.figure(1)
plt.imshow(wc)#安装词云的格则显示
plt.axis('off')#是否显示坐标轴

#plt.show() #显示生成的词云图片
#注意上面这个语句和下面输出词云的语句不能一起出现！！！！
#不然就会出现如word.jpg的形式！！！！只有空白


#输出词云图片到文件
#plt.savefig(r'.\static\wordcloudanptherheart1.jpg',dqi = 500)
wc.to_file(r'.\static\content2.jpg')
