# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:45:38 2020

@author: MSI-PC
"""

import yaml
import os
import re

def gettext(a):
 glist=[]
 blist=[]
 recl=[]
 for i in range(len(a)):
    m = re.findall(r'(?<=").*?(?=")', a[i])
    if m:
        g = re.findall(r'(?<= \$).*?(?=\$)',m[0])
        for j in range(len(g)):   
            m[0]=m[0].replace(g[j], ' BBB%dB '%j)
        b=(re.findall(r'§\w{1}',m[0]))
        for j in range(len(b)):   
            m[0]=m[0].replace(b[j], ' AAA%dA '%j)
        c=(re.findall(r'§',m[0]))
        for j in range(len(c)):   
            m[0]=m[0].replace(c[j], '^^^')
        m[0]=m[0].replace('\n', '***')
        glist.append(g)
        blist.append(b)

    else:
        glist.append([])
        blist.append([])
    recl.append(m)
 return recl,glist,blist



def recov(recl,blist,glist):
    for i in range(len(recl)):
        for j in range(len(blist[i])):
                recl[i][0]=recl[i][0].replace('AAA%dA'%j, blist[i][j])
        for j in range(len(glist[i])):
                    recl[i][0]=recl[i][0].replace('BBB%dB'%j, glist[i][j])
        try:
                    recl[i][0]=recl[i][0].replace('^^^', '§')
                    recl[i][0]=recl[i][0].replace('***', '\n')
        except:
                    pass
    return recl

from googletrans import Translator

#实例化
def trans(recl):   
    translator = Translator(service_urls=['translate.google.cn'])
    for i in range(len(recl)):
        for j in range(len(recl[i])):
         try:
            title = recl[i][j]
            title_alternative = translator.translate(title, dest='zh-CN').text
            recl[i][j]=title_alternative
            print(title_alternative)
         except:
            pass
    return recl

def kiss(a):
    recl,glist,blist=gettext(a)
    m=[]    
    recl=recov(trans(recl),blist,glist)
    for i in range(len(a)):
        m=(re.findall(r'(?<=").*?(?=")', a[i]))
        # print('m====',m)
        # print('a=====',a[i])
    # aa=['BOR_mass_propaganda_desc:0 "With the appointment of the new Reichsminister for Propaganda and Public Enlightenment, Herr Leopold Gutterer, an overwhelmingly huge propaganda campaign will begin. The printed press, the radio, television, plays and cinema will all exalt the Reich, the Führer and the strength of orthodox conservative National Socialism.\n\n"People can be made to see paradise as hell, and to consider the most wretched sort of life as paradise.""']
    
    # mm=['With the appointment of the new Reichsminister for Propaganda and Public Enlightenment, Herr Leopold Gutterer, an overwhelmingly huge propaganda campaign will begin. The printed press, the radio, television, plays and cinema will all exalt the Reich, the Führer and the strength of orthodox conservative National Socialism.\n\n', 'People can be made to see paradise as hell, and to consider the most wretched sort of life as paradise.']
   
    # print(']'*100)
    # print(mm[0])
    # print(']'*100)
    # cc=aa[0].replace(mm[0],recl[3][0])
    # print(cc)
    # cc=cc.replace(mm[1],recl[3][1])
    # print(cc)
        # try:
        #     print('a=======------------------====',a[i].replace(m[i], recl[i][0]))
        # except:
        #     pass
        # print(a[i],m[i][0], recl[i][0])
        for j in range(len(m)):
          # for k in range(len(recl[i])):
            try:
                a[i]=a[i].replace(m[j], recl[i][j])
            except:
                pass
    return a



def w_file(filepath,t):
    with open(filepath,'w',encoding='utf-8') as wf:
        # t=kiss(a)
        for i in range(len(t)):         
            wf.write(t[i])
            wf.write('\n')
            
            
def deal(path):    
    with open(path,'r',encoding='utf-8') as f :
        a=f.read().splitlines()

        t=kiss(a)

        w_file(path,t)
        
        
rootdir='./TNO/'       
list1 = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
for i in range(len(list1)):
        path = os.path.join(rootdir, list1[i])
        print(path)
        deal(path)