# AI CHAMPS SCREENING TEST

The Problem statement consisted of 4 Tasks to be finished. These Tasks are described below-
1. Download 50 public profile PDFs of your connections (randomly) from LinkedIn.
2. Extract text from the above PDFs and store them in a CSV.
3. For every profile data (text), find out the most frequent words and essential words used. It shouldn’t contain stop words (like is, the, an, etc.).
4. Create two web APIs using flask/Django or another framework of your choice.
  * The first web API should take a PDF file as input and return the text in it in JSON format.
  * The second web API should take text data as input and return the most frequent words and important words (as mentioned in 3) in JSON format.

# MY SUBMISSIONS

I would like to preface by saying that I have no experience working with python or any frameworks for web development, I have worked with C++ in Arduino projects and practice DSA whenever I get the time. Additionally I have done some game development in Unity and processing using C# and Java respectively, but nothing very significant. The work that I have done in the submissions are highly inspired from resources I found on the web. I tried to understand the concepts wherever I could to the best of my abilities and I learned a whole lot of things :-).
I thoroughly enjoyed the process of working in this manner and found this to be very fruitful. Thank you so much for organizing this wonderful session. I tried my best to complete all the tasks but unfortunately couldn't finish the last task completely as it took me a lot of time to wrap my head around the working of flask, Nevertheless I am very happy with what I have produced as this is the first time I have actually developed something that works. :D

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
The other files are the files created while debugging my code. The  _tfidf.csv_ file is a .csv file that has the values of tfidf for each word in the dataset. This was created while I was experimenting with ways to find out the most essential words. I kept it since it was useful data and also used it to cross verify the essential words I found.

## TASK 4.

Added part (a) of Task 4 on 28/08/20 to the repository. the app.py file is the main file. The work flow of the code is such that it takes the file uploaded, saves it in the Static Folder and processes it. Once the process of conversion to json is finished, it saves it in a variable. Now the Static folder is cleaned so that in the next run of the code we have a clean work space. It finally returns the variable storing the json file to the user. The added folders are-

* Flask API 1

It contains the env(environment) folder, the Static Folder and the templates folder. It also contains the main app.py file which is the driver code.
