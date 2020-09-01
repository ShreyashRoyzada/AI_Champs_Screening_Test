# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 00:15:00 2020
PDF Converter
"""

import pandas as pd
import os
import pdfplumber
from collections import namedtuple

Line = namedtuple('Line','S_no Text')

comdir=os.path.normpath(os.getcwd()+os.sep+os.pardir)

os.chdir(comdir+"/Task 1/Linkedin Profiles Pdfs")
i=1
lines= []
for items in os.listdir():
    if(items.endswith('.pdf')):
        file=items
        with pdfplumber.open(file) as pdf:
            text=''
            for page in pdf.pages:
                text=text+page.extract_text()

            lines.append(Line(i,text))
            i=i+1

os.chdir(comdir+"\Task 2")
df = pd.DataFrame(lines)

df.to_csv('Task2.csv',index=False)
