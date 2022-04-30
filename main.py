if __name__ == "__main__":
    import csv
    import xml.etree.ElementTree as ET
    from poligon import getpath, getnames

    dirName = 'completed-regression-test-runs'  # name of the directory where the checklists.csv are located
    full_path = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/'  # full path to the
    # directory with checklists

    i = 0  # counter
    re = '\n'  # delimiter
    csvFile = getpath(full_path)
    filename = getnames(full_path)

    while i < len(filename):  # this loop iterates through all the files in the directory
        csvfile1 = csvFile['path'][i]  # add filename
        xmlfile1 = str(filename[i])
        p = ET.Element('testsuite')
        a = 0
        xmlfile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + xmlfile1 + '.xml'
        with open(csvfile1, 'r', newline='', encoding='utf-8') as rf, open(xmlfile, 'w', newline='', encoding='utf-8') as wf:
            reader = csv.DictReader(rf, delimiter=",")

            for row in reader:  # this loop iterates through the lines in the i file
                numb = row['number']
                ind = row['indent']
                txt = row['text']
                nts = row['notes']
                a += 1
                comment = ' | <strong>comment:</strong> ' + row['comment'] + f'|{a}|'

                if int(ind) <= 1:
                    p.set('name', xmlfile1)  # set name for
                    el1 = ET.SubElement(p, 'testsuite' + re)
                    el3 = ET.SubElement(el1, 'details')
                    el1.set('name', txt)
                    el3.text = '<strong>Desc:</strong> ' + txt + ' | ' + nts + comment  # in case the value is too
                    # long for field name testlink

                elif int(ind) > 1:
                    el2 = ET.SubElement(el1, 'testcase' + re)
                    el2.set('name', txt)
#                    el2.set('internalid', ind)
#                    subel0 = ET.SubElement(el2, 'externalid')
                    subel1 = ET.SubElement(el2, 'summary')
                    subel1.text = '<strong>Desc:</strong> ' + txt + nts + comment  # in case the value is too
                    # long for field name testlink

            ET.ElementTree(p).write(xmlfile, encoding="UTF-8", xml_declaration=True)
        i += 1
