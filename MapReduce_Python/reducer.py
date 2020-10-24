# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:57:31 2020

@author: Real-
"""
import sys
def reducer():
    text = sys.stdin.readline()
    
    wordcount = dict()
    while text:
        words = text.split("\t")
        wordcount[words[0]]=wordcount.get(words[0],0)+1
        text=sys.stdin.readline()
    
    for i,j in wordcount.items():
        print(i+"\t",j)
    


if __name__=="__reducer__":
    reducer()    
