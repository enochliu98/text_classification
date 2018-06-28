#!/usr/bin/python
# -*- coding: UTF-8 -*-
#########头文件##################################
from lxml import etree
import io
import os
from xml.dom.minidom import parse
import xml.dom.minidom
#########将文件写成一个列表########################
rootdir='C:/Users/Tina/Desktop/dataset/trainset/wl/'
mlist=os.listdir(rootdir)
print(len(mlist))
#################################################

# f=open('C:/Users/Tina/Desktop/out.txt','a')##追加读写

dictionary={'Life':'1','Movement':'2','Transaction':'3','Business':'4','Conflict':'5','Contact':'6','Personnel':'7','Justice':'8'}

for i in range(int(len(mlist)/4)):
    print(i)

    print(4*i+2)
    response = []
    mdir='C:/Users/Tina/Desktop/dataset/trainset/wl/'+mlist[4*i+2]
    with open(mdir,'r',encoding='utf-8') as f:
        html = etree.parse(f)

        result = html.xpath('//POST/text()')

        for item in result:
            temp = item.replace('\n', '')  # 去除换行符
            temp = temp.split('。')  # 依据句号分割
            for j in temp:
                response.append(j)



    print(response)


    print(i)
    f=open('C:/Users/Tina/Desktop/train7.txt','a')
    print(4*i+1)
    print(mlist[4*i+1])
    ndir='C:/Users/Tina/Desktop/dataset/trainset/wl/'+mlist[4*i+1]
    DOMTree = xml.dom.minidom.parse(ndir)

    collection=DOMTree.documentElement

    events=collection.getElementsByTagName('event')

    ctype={}
    mflag={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
    bbctype=[]
    for event in events:
        if event.hasAttribute("TYPE"):
            bbtype=event.getAttribute('TYPE')
            btype=dictionary[bbtype]
            if mflag[btype]==0:
                ctype[btype]=[]
                mflag[btype]=1


        eventarguments=event.getElementsByTagName('event_mention')
        for eventargument in eventarguments:
            if eventargument.hasAttribute('ID'):
                ldc=eventargument.getElementsByTagName('ldc_scope')
                charseq=ldc[0].getElementsByTagName('charseq')
                ctype[btype].append(charseq[0].childNodes[0].data.replace('\n',''))

    for key in ctype:
        bbctype.append(key)


    for resp in response:
        flag=0
        for bbbtype in bbctype:
            for cctype in ctype[bbbtype]:
                if cctype in resp:
                    aaa=bbbtype+'\t'+resp+'\n'
                    flag=1
                    f.write(aaa)
                    break
        if flag==0:
            bbb='0'+'\t'+resp+'\n'
            f.write(bbb)

