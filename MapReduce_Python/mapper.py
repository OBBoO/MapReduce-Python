# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
def mapper():
    text = sys.stdin.readline()
    
    while text:
        words=text.split()
        for word in words:
            if len(word)>0:
                print(word+"\t"+"1")
        text=sys.stdin.readline()
            
    


    
if __name__=="__main__":
    mapper()    
