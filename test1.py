import csv
import xml.etree.ElementTree as ET

csvFile = 'smoke.csv'
xmlFile = 'smoke_new.xml'
p = ET.Element('testcases')


with open(csvFile, 'r', newline='', encoding='utf-8') as rf, open(xmlFile, 'w', newline='', encoding='utf-8') as wf:
    reader = csv.DictReader(rf, delimiter=",")
    for row in reader:
        text_read = row['text']
        el1 = ET.SubElement(p, 'testcase')
        subel1 = ET.SubElement(el1, 'summary')
        subel2 = ET.SubElement(el1, 'importance')

        p.text = '\n'
        el1.set('name', text_read)
        subel1.text = row['notes'] + '\n'
        subel2.text = "Medium" + '\n'


ET.ElementTree(p).write(xmlFile, encoding="UTF-8", xml_declaration=True)