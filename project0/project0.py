import urllib
import PyPDF2
import re
import tempfile
import sqlite3

def fetchincidents(url):
    #url = ("https://www.normanok.gov/sites/default/files/documents/"
    #"2021-03/2021-03-01_daily_incident_summary.pdf")
    
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()   
    fp= tempfile.TemporaryFile()
    fp.write(data)
    return fp

def extractincidents(fp):
    fp.seek(0)

    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pdfReader.getNumPages()

    page1 = pdfReader.getPage(0).extractText()
    print(page1)
    
    all_pages = []
    read_pdf = PyPDF2.PdfFileReader(fp)
    number_of_pages = read_pdf.getNumPages()
    for page_number in range(number_of_pages): 
        page = read_pdf.getPage(page_number).extractText().split("\n")  
        all_pages.append(page)
    all_pages=[]
    for x in range(pdfReader.getNumPages()):
        page=pdfReader.getPage(x).extractText()
        paged=re.sub(' \n', ' ',page)
        all_pages.append(paged)
        print(all_pages)
        
    ttl_dates=[]
    ttl_incd_num=[]
    ttl_loc=[]
    ttl_nature=[]
    ttl_incd_ori=[]
    date=[]
    incd_num=[]
    location=[]
    nature=[]
    incd_org=[]
    
    for count, value in enumerate(all_pages):
        g=value.split("\n")
        date=g[0::5]
        incd_num=g[1::5]
        location=g[2::5]
        nature=g[3::5]
        incd_ori=g[4::5]
        date.pop(-1)
        if count==0:
            incd_num.pop(-1)
            location.pop(-1)
        if count==len(all_pages)-1:
            incd_num.pop(-1)

        ttl_dates.extend(date)
        ttl_incd_num.extend(incd_num)
        ttl_loc.extend(location)
        ttl_nature.extend(nature)
        ttl_incd_ori.extend(incd_ori)
    incident_list=[]
    for i in range(len(ttl_incd_num)):
        incident_list.append([ttl_dates[i],ttl_incd_num[i],ttl_loc[i],ttl_nature[i],ttl_incd_ori[i]])
    return incident_list

def createdb():
    dbname= 'normanpd.db'
    database= sqlite3.connect(dbname)
    db = database.cursor()
    db.execute(" DROP TABLE IF EXISTS incidents")
    db.execute(""" CREATE TABLE IF NOT EXISTS incidents
                    (incident_time TEXT,
                    incident_number TEXT,
                    incident_location TEXT,
                    nature TEXT,
                    incident_ori TEXT);""")
    database.commit()
    database.close()
    return dbname

def populatedb(db, incidents):
    database = sqlite3.connect(db)
    db=database.cursor()
    for i in range(1,len(incidents)):
        db.execute("INSERT INTO incidents (incident_time, incident_number, incident_location, nature, incident_ori)"
              " VALUES (?, ?, ?, ?, ?)",
            (incidents[i][0],incidents[i][1],incidents[i][2],incidents[i][3],incidents[i][4]))
        db.execute("select * from incidents")
    database.commit()
    return 0

def status(db):
    database= sqlite3.connect(db)
    db= database.cursor()
    final_output=db.execute(""" SELECT `nature`, count(*) FROM `incidents`
              GROUP BY `nature` """)
    for val in final_output:
        print(f'{val[0]}|{val[1]}')
        return final_output
