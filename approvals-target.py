import csv
import xml.etree.ElementTree as ET

fName = 'smoke'
dirName = 'smoke'
csvFile = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/' + fName + '.csv'
xmlFile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + fName + '.xml'
p = ET.Element('testsuite')
pastiter = []


def lstnmb(x, i):  # функция для сохранения предыдущего значения numb в цикле
    pastiter.insert(i, x)
    retpst = pastiter[i-2]
#    print('Old: ', retpst)
    return retpst


with open(csvFile, 'r', newline='', encoding='utf-8') as rf, open(xmlFile, 'w', newline='', encoding='utf-8') as wf:
    reader = csv.DictReader(rf, delimiter=",")
    i = 0
    for row in reader:
        i += 1
        numb = row['number']
        ind = row['indent']
        txt = row['text']
        nts = row['notes']
        print(numb)
        lstnmb(numb, i)

        # if ind == 1:
        #     el1 = ET.SubElement(p, 'testcase' + ind)
        #     subel0 = ET.SubElement(el1, 'externalid')
        #     subel1 = ET.SubElement(el1, 'summary')
        #     subel2 = ET.SubElement(el1, 'importance')
        #
        #     el1.set('name', txt)
        #     subel0.text = numb
        #     subel1.text = nts
        #     subel2.text = "Medium"
        #     p.set('name', fName)
        # elif ind > 1:
        #     el1 = ET.SubElement(p, 'testcase' + ind)
        #     subel0 = ET.SubElement(el1, 'externalid')
        #     subel1 = ET.SubElement(el1, 'summary')
        #     subel2 = ET.SubElement(el1, 'importance')
        #
        #     el1.set('name', txt)
        #     subel0.text = numb
        #     subel1.text = nts
        #     subel2.text = "Medium"
        #     p.set('name', fName)

# ET.ElementTree(p).write(xmlFile, encoding="UTF-8", xml_declaration=True)
