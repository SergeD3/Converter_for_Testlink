if __name__ == "__main__":
    import csv
    import xml.etree.ElementTree as ET
    from poligon import getpath, getnames

    dirName = 'completed-new-feature-test-runs'  # name of the directory where the checklists.csv are located
    full_path = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/'  # full path to the
    # directory with checklists

    i = 0  # counter
    re = '\n'  # delimiter
    csvFile = getpath(full_path)
    filename = getnames(full_path)

    while i < len(filename):  # this loop iterates through all the files in the directory
        csvfile1 = csvFile['path'][i]
        xmlfile1 = str(filename[i])
        p = ET.Element('testsuite')
        xmlfile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + xmlfile1 + '.xml'
        with open(csvfile1, 'r', newline='', encoding='utf-8') as rf, open(xmlfile, 'w', newline='', encoding='utf-8') as wf:
            reader = csv.DictReader(rf, delimiter=",")

            for row in reader:  # this loop iterates through the lines in the i file
                numb = row['number']
                ind = row['indent']
                txt = row['text']
                nts = row['notes']
                if int(ind) <= 1:
                    p.set('name', xmlfile1)
                    el1 = ET.SubElement(p, 'testsuite' + re)
                    el1.set('name', txt)

                elif int(ind) > 1:
                    el2 = ET.SubElement(el1, 'testcase' + re)
                    el2.set('name', txt)
#                    el2.set('internalid', ind)
                    subel0 = ET.SubElement(el2, 'externalid')
                    subel1 = ET.SubElement(el2, 'summary')
#                    subel0.text = numb
                    subel1.text = nts

            ET.ElementTree(p).write(xmlfile, encoding="UTF-8", xml_declaration=True)
        i += 1
