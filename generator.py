# -*- coding: utf-8 -*-

def generate_caption(filename):
    ind1=filename.index("_")
    ind2=filename.rfind("-")
    target_word=filename[ind1:ind2+1]
    
    try:
        file =  open('captions1.txt', 'r')
        line=" "
        while(True):
            line=file.readline()
            if target_word in line:                 
                sentences = line.split('.png')
                return sentences[-1]
                            
    except FileNotFoundError:
        #print("File not found.")
        return ''
    return None

