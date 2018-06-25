import func
##########引入写的函数############


train_label_list,train_corpus_list=func.part_jieba('C:/Users/Tina/Desktop/samples/train_set.txt')
test_label_list,test_corpus_list=func.part_jieba('C:/Users/Tina/Desktop/samples/test_set.txt')

corpus_list=test_corpus_list+train_corpus_list #构造处理完的句子
label_list=test_label_list+train_label_list #构造标签

length=len(test_label_list)#便于计算完tfidf之后的划分

tfidf=func.tfidf_cop(corpus_list)#计算tfidf

classiy_model=func.model_train(tfidf,label_list) #训练模型并测试


test_tfidf=tfidf[:length]
test1=tfidf[:1000]
func.model_test(test_tfidf,test_label_list,test1,classiy_model)