import csv
import xml.etree.ElementTree as ET

fName = 'smoke'
dirName = 'smoke'
i = '\n'
csvFile = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/' + fName + '.csv'
xmlFile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + fName + '.xml'
p = ET.Element('testsuite')


with open(csvFile, 'r', newline='', encoding='utf-8') as rf, open(xmlFile, 'w', newline='', encoding='utf-8') as wf:
    reader = csv.DictReader(rf, delimiter=",")
    for row in reader:
        numb = row['number']
        ind = row['indent']
        txt = row['text']
        nts = row['notes']
        if int(ind) == 1:
            el1 = ET.SubElement(p, 'testcase' + i)
            subel0 = ET.SubElement(el1, 'externalid')
            subel1 = ET.SubElement(el1, 'summary')
            subel2 = ET.SubElement(el1, 'importance')

            el1.set('name', txt)
            subel0.text = numb + i
            subel1.text = nts + i
            subel2.text = "Medium" + i
            p.set('name', fName)
            el1.text = i
        elif int(ind) > 1:
            p1 = ET.SubElement(p, 'testsuite' + i)
            el1 = ET.SubElement(p1, 'testcase' + i)
            subel0 = ET.SubElement(el1, 'externalid')
            subel1 = ET.SubElement(el1, 'summary')
            subel2 = ET.SubElement(el1, 'importance')

            el1.set('name', txt)
            subel0.text = numb + i
            subel1.text = nts + i
            subel2.text = "Medium" + i
            p.set('name', fName)
            p1.set('name', txt)
            el1.text = i


ET.ElementTree(p).write(xmlFile, encoding="UTF-8", xml_declaration=True)