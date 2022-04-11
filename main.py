import csv
import xml.etree.ElementTree as ET
import fileinput
import pathlib

csvFile = 'smoke.csv'
xmlFile = 'smoke_new.xml'
li = []
p = ET.Element('testcases')


with open(csvFile, 'r', newline='', encoding='unicode') as rf, open(xmlFile, 'w', newline='', encoding='unicode') as wf:
    reader = csv.DictReader(rf, delimiter=",")
    writer = csv.writer(wf)
    wf.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    for row in reader:
        el1 = ET.SubElement(p, 'testcase')
        subel1 = ET.SubElement(el1, 'summary \n')
        subel2 = ET.SubElement(el1, 'importance \n')
        mydata = ET.tostring(p, encoding='utf-8')
#        mydata.encode('unicode')

        el1.text = row['text']
        subel1.text = row['notes']
        subel2.text = "Medium"
        myfile = open('smoke_new.xml', 'w')
        myfile.write(mydata)



# a = read()
# for i in range(len(li)):
#      print('i[0]', 'i[1]')

    # tstcases = ET.Element('testcases')
    # tstcase = ET.SubElement(tstcases, 'testcase')
    # tree = ET.ElementTree(tstcases)
    # wf.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")
    # for row in reader:
    #     wf.write("<testcases>" + '%s' + "</testcases>")






    # for row in reader:
    #     titles = [row['text'], row['notes']]
    #
    # with open("smoke_new.xml", 'a', newline='', encoding='utf-8') as csvfile:
    #     writer = csv.writer(csvfile, delimiter=",")
    #     writer.writerow(['<testcases>'])
    #     for u in titles:
    #         writer.writerow(u['text'], u['notes'])
    #     writer.writerow(['</testcases>'])