import func
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import logistic
from sklearn.metrics import classification_report
from sklearn.model_selection import  GridSearchCV

train_label_list,train_corpus_list=func.part_jieba('C:/Users/Tina/Desktop/samples/train_set.txt')
test_label_list,test_corpus_list=func.part_jieba('C:/Users/Tina/Desktop/samples/test_set.txt')

corpus_list=test_corpus_list+train_corpus_list #构造处理完的句子
label_list=test_label_list+train_label_list #构造标签

##pipeline方法一般只使用sklearn中已经封装了的函数
text_clf = Pipeline([('vect', CountVectorizer()),
                      ('tfidf', TfidfTransformer()),
                      ('clf',RandomForestClassifier())
])
parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
               'tfidf__use_idf': (True, False),
               'clf__alpha': (1e-2, 1e-3),
 }
text_clf.fit(corpus_list,label_list)
print(text_clf.score(test_corpus_list,test_label_list))

