# cs5293sp21-project0

 ALIYA SHAIKH
 EMAIL: aliyashaikh02@ou.edu

The https://www.normanok.gov/public-safety/police-department/crime-prevention-data/daily-activity-reports website contains three types of summaries: arrests, incidents, and case summaries. The aim of this project is to build a function that collects only the incidents.

### PACKAGES REQUIRED:
1. urllib
2. PyPDF2
3. tempfile
4. sqlite3
5. argparse
6. re

### STEPS TO RUN:


### PROJECT DESCRIPTION:

The code structure is as follows:
```
cs5293sp21-project0/
├── COLLABORATORS
├── LICENSE
├── requirements.txt
├── README
├── project0
│   ├── __init__.py
│   └── main.py
│   └── ...
├── docs/
├── setup.cfg
├── setup.py
└── tests
    ├── test_createdb.py
    └── test_status.py
    └── ... 
```    
### DESCRIPTION:

##### 1. main.py
The main function of the project is written in main.py file. The code should take a url from the command line and perform each operation. After the code is installed, you should be able to run the code using the command below.
`pipenv run python project0/main.py --incidents <url>`
With the use of argparse, the url given in the command line will be passed to main function. All the functions defined in project0.py are then imported in main.py.

##### 2. Downloading the data:
The function fetchincidents() in project0.py uses the python urllib.request library to grab the pdf from the given url.
The data that is then downloaded from the file is saved into a temporary file. This temporary file is then used in the next method for extraction.

##### Extracting the Data:
For this, we use the function extractincidents() in project0.py. 
The function extractincidents() reads data and extracts the incidents. The information extracted consists of Date/Time, Incident Number, Location, Nature and Incident ORI.
For the extraction of data from the pdf file,we use the PyPdf2.PdfFileReader. This allows us to extract pages from the pdf file and search for the rows. Then we extract each row from the pdf file and add it to a list which is initially empty.
Initially tried different ways to extract the data but the final results were not how they should be.
Then by making use of regular expressions, data extraction became relatively easier and cleaner.
Made use of '\n' to split the data initially. Also, many locations had addresses i.e data on multiple lines which had to be converted to a single line. This was done by replacing '\n' with ' '. 
Also, the pdf pages had headers and footers and extra spaces which had to be removed as well. Using the pop() function made it easier to get rid of them.

##### Creating the database:
The createdb() function in project0.py file creates an SQLite database file named normanpd.db and inserts a table with the following columns: incident_time, incident_number, incident_location, nature, incident_ori.

##### Inserting data into the database:
The function populatedb(db, incidents) takes data extracted by the extractincidents() function and adds it to the normanpd.db database.

##### Displaying the data:
The status() function displays the nature of the incidents and their count. i.e the number of times they have occured. 

### TESTS:

##### 1. test
