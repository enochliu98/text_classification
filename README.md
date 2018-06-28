# classification
## Requirements

- Python 3.5
- pyltp || jieba
- Numpy

## corpus
  We use the----ACE corpus, which is commonly used in event extraction, as our original dataset.

The 9 types of corresponding labels are as follows:

|Notanyclass|	Life|Movement|Transaction|Business|Conflict|Contact	|Personnel|Justice|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|2|3|4|5|6|7|8|
<p align="center">type dictionary</p>

## Extract samples
[out.txt](:storage\3cb00c28-f19b-4703-bfdb-baa843b33176\ec4b2bcc.txt) 
   66 articles were selected as the test set, the remaining 567 as training set, and 33 articles selected randomly from the training set as the validation set.
   
   **dataset**：
   [train_set(https://github.com/EnochMHforever/text_classification/tree/master/data/raw_dataset/trainset.txt) ／
   [test_set](https://github.com/EnochMHforever/text_classification/tree/master/data/raw_dataset/testset.txt) ／
   [validation set](https://github.com/EnochMHforever/text_classification/tree/master/data/raw_dataset/valid.txt)
   
    The way is to read the XML file from "etree", find the corresponding tag by "Find", and "XPath" return the content that needs to be tagged.
	There's also three main ways to analyse the XML file for python which are dom,sax and etree.In all these ways,etree is the most convinent,so that I choose etree and dom to analyse.
	
## Pre Processing
  1. text processing as the format required by the model. <br>
  2. participle. <br>
  3. go to the discontinuation of the word.<br>
Participle: 
1.use the CWS segmentation model of Pyltp to process the whole text set and return a list of finished words.
2.use jieba segmentation which is a simpler way to cope with it.
Get stop words: expand the scope of the stop words, and remove the strange words that appear only once in the whole training set.
<!-- code：[c.py](:storage\7baa3ef0-d75e-4c64-bedc-f451dda79824\43150200.py)
 预处理的结果：[build_set.txt](:storage\3cb00c28-f19b-4703-bfdb-baa843b33176\cad4251d.txt) -->

## Feature Engineering
### Transforming text into vector, feature processing, feature selection and feature dimension reduction
	Text variable vector: TF_IDF, 
	TF is the sample word frequency, 
	IDF is the inverse document frequency, 
	the word vector of a word is determined by these two data.

The larger the TF, the greater the weight in the sample. The larger the IDF, the greater the number of times in the whole document.



## Classification algorithms
### SVM
### RandowForest

## Evaluation
### precision and recall
### classification report
### test_result
.