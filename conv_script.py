import csv
import xml.etree.ElementTree as ET

fName = 'target-library-20212-20213'
dirName = 'general-regression-actual-versions'
csvFile = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/' + fName + '.csv'
xmlFile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + fName + '.xml'
p = ET.Element('testsuite')
ind = '\n'


with open(csvFile, 'r', newline='', encoding='utf-8') as rf, open(xmlFile, 'w', newline='', encoding='utf-8') as wf:
    reader = csv.DictReader(rf, delimiter=",")
    for row in reader:
        text_read = row['text']
        notes_read = row['notes']
        el1 = ET.SubElement(p, 'testcase' + ind)
        subel1 = ET.SubElement(el1, 'summary')
        subel2 = ET.SubElement(el1, 'importance')

        p.text = ind
        el1.set('name', text_read)
        subel1.text = row['notes']
        subel2.text = "Medium"
        p.set('name', fName)


ET.ElementTree(p).write(xmlFile, encoding="UTF-8", xml_declaration=True)