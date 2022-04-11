import csv
import xml.etree.ElementTree as ET

csvFile = "C:/Users/Серж/Desktop/testcases_CRP/scripts/to-sort-out/approvals-target.csv"
xmlFile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/approvals-target/approvals_target.xml'
ind = '\n'
p = ET.Element('testsuite' + ind)
suiteName = 'approvals-target'


with open(csvFile, 'r', newline='', encoding='utf-8') as rf, open(xmlFile, 'w', newline='', encoding='utf-8') as wf:
    reader = csv.DictReader(rf, delimiter=",")
    for row in reader:
        text_read = row['text']
        notes_read = row['notes']

        el1 = ET.SubElement(p, 'testcase')
        subel1 = ET.SubElement(el1, 'summary')
        subel2 = ET.SubElement(el1, 'importance')

        el1.set('name', text_read)
        subel1.text = notes_read
        subel2.text = "Medium"
        p.set('name', suiteName)


ET.ElementTree(p).write(xmlFile, encoding="UTF-8", xml_declaration=True)