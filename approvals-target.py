import csv
import xml.etree.ElementTree as ET

fName = 'target-library-20212-20213'
dirName = 'general-regression-actual-versions'
csvFile = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/' + fName + '.csv'
xmlFile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + fName + '.xml'
ind = '\n'


with open(csvFile, 'r', newline='', encoding='utf-8') as rf, open(xmlFile, 'w', newline='', encoding='utf-8') as wf:
    reader = csv.DictReader(rf, delimiter=",")