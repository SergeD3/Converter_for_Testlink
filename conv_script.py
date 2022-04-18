import csv
import xml.etree.ElementTree as ET
from poligon import *

dirName = 'general-regression-actual-versions'
fName = 'reg-approvals'
pastiter = []
suite_num = []
p = ET.Element('testsuite')
re = '\n'
csvFile = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/' + fName + '.csv'
xmlFile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + fName + '.xml'


with open(csvFile, 'r', newline='', encoding='utf-8') as rf, open(xmlFile, 'w', newline='', encoding='utf-8') as wf:
    reader = csv.DictReader(rf, delimiter=",")
    i = 0
    for row in reader:
        i += 1
        numb = row['number']
        ind = row['indent']
        txt = row['text']
        nts = row['notes']

        if int(ind) == 1:
            p.set('name', fName)
            el1 = ET.SubElement(p, 'testsuite' + re)
            el1.set('name', txt)
            el1.text = re

        elif int(ind) > 1:
            el2 = ET.SubElement(el1, 'testcase' + re)
            el2.set('name', txt)
#           subel0 = ET.SubElement(el2, 'externalid')
            subel1 = ET.SubElement(el2, 'summary')
            subel2 = ET.SubElement(el2, 'importance')

#            subel0.text = numb
            subel1.text = nts
            subel2.text = "Medium"

ET.ElementTree(p).write(xmlFile, encoding="UTF-8", xml_declaration=True)