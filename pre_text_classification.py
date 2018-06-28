#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
头文件
'''
import jieba
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

'''
函数stopwordslist
加载停用词表，产生停用词组成的列表
m为结果
'''

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords
m=stopwordslist('C:/Users/Tina/Desktop/stopwords.txt')


'''
提取文本中的文字
其中标签存在于label_list,内容存在corpus_list
'''
##################方法1，使用jieba分词#######################
#f=open('C:/Users/Tina/Desktop/samples/train_set.txt').read()
#ff=open('C:/Users/Tina/Desktop/samples/test_set.txt').read()
f1=open('C:/Users/Tina/Desktop/hey.txt','a')#用来在后面存储测试数据
#jieba.enable_parallel(5)
#mf=[x for x in jieba.cut(f)]
#测试作用
label_list=[] #用来存标签
corpus_list=[] #用来存句子
with open('C:/Users/Tina/Desktop/samples/train_set.txt') as f:
    for line in f:
        label_list.append(line.split('\t')[0])#tab前的数字标签数字部分
        data=line.split('\t')[1]#tab后的数据部分
        ddata=[x for x in jieba.cut(data)]#用jieba分割句子
        #print(ddata)
        dddata=''#这里使用字符串存储每个句子是为了方便后面tfidf的得出
        for i in range(len(ddata)): #去停用词
            if ddata[i] not in m:
                dddata+=ddata[i]+' '

        corpus_list.append(str(dddata))#讲每个句子存入list中

print(label_list)
######################方法2：使用pyltp分词#################
# from pyltp import Segmentor
# segmentor=Segmentor()#定义分词函数
# segmentor.load()
#
# with open('C:/Users/Tina/Desktop/train5.txt') as f:
#     for line in f:
#         label_list.append(line.split('\t')[0])#tab前的数字标签数字部分
#         data=line.split('\t')[1]#tab后的数据部分
#         ddata=[x for x in list(segmentor.segment(data))]#用jieba分割句子
#         #print(ddata)
#         dddata=''#这里使用字符串存储每个句子是为了方便后面tfidf的得出
#         for i in range(len(ddata)): #去停用词
#             if ddata[i] not in m:
#                 dddata+=ddata[i]+' '
#
#         corpus_list.append(str(dddata))#讲每个句子存入list中


#下面是对测试集的处理，方法与前面相同
test_label_list=[] #存测试标签
test_corpus_list=[] #存测试句子
with open('C:/Users/Tina/Desktop/samples/test_set.txt') as ff:
    for line in ff:
        test_label_list.append(line.split('\t')[0])
        data=line.split('\t')[1]
        ddata=[x for x in jieba.cut(data)]
        #print(ddata)
        dddata=''
        for i in range(len(ddata)):
            if ddata[i] not in m:
                dddata+=ddata[i]+' '

        test_corpus_list.append(str(dddata))

print(test_corpus_list)
print(test_label_list)

'''
tfidf
用于计算词的重要程度
这里使用了sklearn自带的方法
'''
words={} #够一个word字典
corpus_list=test_corpus_list+corpus_list #合并
vectorizer=CountVectorizer(min_df=1e-5) #构造存储句子的容器，并从中选择大于1e-5的
transformer=TfidfTransformer() #计算方法
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus_list)) #*****这里的结果不是list
word=vectorizer.get_feature_names() #获取提取处的总的词
label_list=test_label_list+label_list
print(label_list)
#print("tf-idf shape: ({0},{1})".format(test_tfidf.shape[0], test_tfidf.shape[1]))
#print(len(test_label_list))
test_tfidf=tfidf[:1000]
test_label_list=label_list[:1000]

test1=tfidf[:1000]
print('label1',label_list[0])
print('label2',label_list[1])


tfidf=tfidf[1000:]
label_list=label_list[1000:]
'''
训练模型阶段
这里采取的是两种方法
分别为svc和randomforest
'''
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
classify_model=RandomForestClassifier(n_estimators=200,random_state=1080)
#classify_model=SVC()
classify_model.fit(tfidf,label_list)
print('训练完成')

print( "val mean accuracy: {0}".format(classify_model.score(test_tfidf, test_label_list)))
y_pred=classify_model.predict(test1)
print(y_pred)
for i in range(len(y_pred)):
    f1.write(y_pred[i]+'\n')

#################使用管道方法，简化操作########################
# from sklearn.svm import SVC
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.pipeline import Pipeline
# text_clf=Pipeline([('vect',CountVectorizer()),
#                    ('tfidf',TfidfTransformer()),
#                    ('clf',SVC)])
#
# text_clf.fit(corpus_list,label_list)


