# AI CHAMPS SCREENING TEST

The Problem statement consisted of 4 Tasks to be finished. These Tasks are described below-
1. Download 50 public profile PDFs of your connections (randomly) from LinkedIn.
2. Extract text from the above PDFs and store them in a CSV.
3. For every profile data (text), find out the most frequent words and essential words used. It shouldn’t contain stop words (like is, the, an, etc.).
4. Create two web APIs using flask/Django or another framework of your choice.
  * The first web API should take a PDF file as input and return the text in it in JSON format.
  * The second web API should take text data as input and return the most frequent words and important words (as mentioned in 3) in JSON format.

# MY SUBMISSIONS

## TASK 1.

Completed the Task 1 on 24/08/20 and added the files to the repo. Please find 51 LinkedIn Profiles in the Task 1 Folder in .pdf format. These were manually collected from LinkedIn and no bot/scrapper was used in the collection process.

## TASK 2.

Completed the Task 2 on 25/08/20 and added the files to the repo. The Files added were-
* PDFConverter.py
* Task2.csv
* trail1.csv
* trial2.csv
* trial3.csv

Among these files the **final submissions are _PDF Converter.py_  and _Task2.csv_.** 
The other files are the files created while debugging my code.

## TASK 3.

Completed the task 3 on 26/08/20. Added the files to the repo. The Files added were-
* CSV Cleaner.ipynb
* Task3.csv
* cleantrail1.csv
* tfidf.csv

Among these files the **final submissions are _CSV Cleaner.ipynb_  and _Task3.csv_.** 
The other files are the files created while debugging my code. The  _tfidf.csv_ file is a .csv file that has the values of tfidf for each word in the dataset. This was created while I was experimenting with ways to find out the most essential words. I kept it since it was usefull data and also used it to cross verify the essential words I found.