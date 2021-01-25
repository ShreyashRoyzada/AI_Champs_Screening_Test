# Text data Normalization Project

I divided the work in 4 Tasks to be finished. These Tasks are described below-
1. Download 50 public profile PDFs of your connections (randomly) from LinkedIn.
2. Extract text from the above PDFs and store them in a CSV.
3. For every profile data (text), find out the most frequent words and essential words used. It shouldn’t contain stop words (like is, the, an, etc.).
4. Create two web APIs using flask/Django or another framework of your choice.
  * The first web API should take a PDF file as input and return the text in it in JSON format.
  * The second web API should take text data as input and return the most frequent words and important words (as mentioned in 3) in JSON format.

## TASK 1.

51 LinkedIn Profiles in the Task 1 Folder in .pdf format. These were manually collected from LinkedIn and no bot/scrapper was used in the collection process.

## TASK 2.

The Files added were-
* PDFConverter.py
* Task2.csv
* trail1.csv
* trial2.csv
* trial3.csv

Among these files the **final submissions are _PDF Converter.py_  and _Task2.csv_.**
The other files are the files created while debugging my code.

## TASK 3.

The Files added were-
* CSV Cleaner.ipynb
* Task3.csv
* cleantrail1.csv
* tfidf.csv

Among these files the **final submissions are _CSV Cleaner.ipynb_  and _Task3.csv_.**
The other files are the files created while debugging my code. The  _tfidf.csv_ file is a .csv file that has the values of tfidf for each word in the dataset. This was created while I was experimenting with ways to find out the most essential words. I kept it since it was useful data and also used it to cross verify the essential words I found.

## TASK 4.

Added part (a) of Task 4 on 28/08/20 to the repository. the app.py file is the main file. The work flow of the code is such that it takes the file uploaded, saves it in the Static Folder and processes it. Once the process of conversion to json is finished, it saves it in a variable. Now the Static folder is cleaned so that in the next run of the code we have a clean work space. It finally returns the variable storing the json file to the user. The added folders are-

* Flask API 1

It contains templates folder and the requirements.txt file. Please install the requirements before running the code.  It also contains the main app.py file which is the driver code. For running the file create a virtual environment in VS Code. Also add a Static folder in the Flask API 1 Folder.( It was not uploading on github as it was an emplty folder) This is used for storing the file before processing it and is cleaned after the processing is finished. Run the file using _python app.py_ command.
