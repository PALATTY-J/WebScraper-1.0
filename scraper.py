import requests
import csv
from bs4 import BeautifulSoup

reqLinks=[]

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    for row in csv_reader:
        reqLinks = row


# req = requests.get('https://www.1mg.com/drugs/cipladine-ointment-137489')
# req = requests.get('https://www.1mg.com/drugs/ciplar-la-20-tablet-342850')

csvFile = open('data.csv','w')
row=["Name","Benifits","Manufacturer","Contains"]


writer = csv.writer(csvFile)
writer.writerow(row)

for rowItem in row:
    row[row.index(rowItem)]="No Data"  


for reqLink in reqLinks:
    req = requests.get(reqLink)
    soup = BeautifulSoup(req.content,"html.parser")
    row[0]=soup.title.get_text()
    print('Extracting Data From '+ soup.title.get_text())
    for fileObj in soup.findAll('script'):
        if ("\"benefits\":[{" in fileObj.get_text()):
            # print("IN Benifits")
            # fileText = open('data.json','wb')
            textFile = '{'+ fileObj.get_text().split("\"benefits\":[{")[1].split('}]}]}')[0] +'}]}'
            # fileText.write(textFile.encode('utf-8'))
            row[1]=textFile
        

        if ("\"header\":\"Manufacturer\"" in fileObj.get_text()):
            # print("IN Manufacturer")
            # fileText = open('data.txt','wb')
            textFile = fileObj.get_text().split("\"header\":\"Manufacturer\",")[1].split("</a>\"}")[0].split('>')[1]
            # fileText.write(textFile.encode('utf-8'))
            row[2]=textFile
        

        if ("\"header\":\"Contains\"" in fileObj.get_text()):
            # print("IN Contains")
            # fileText = open('data3.txt','wb')
            textFile = fileObj.get_text().split("\"header\":\"Contains\"")[1].split("</a>\"}")[0].split('>')[1]
            # fileText.write(textFile.encode('utf-8'))
            row[3]=textFile

    for rowItem in row:
        if rowItem == '':
            row[row.index(rowItem)]="No Data"  

    writer.writerow(row) 
    for rowItem in row:
        row[row.index(rowItem)]="No Data"  

       

# print(soup.prettify())
# print(soup.findAll('script')[2])

# res=soup.find("çlass='DrugOverview__content___22ZBX'")
# print(soup.html['id'])