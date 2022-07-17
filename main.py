if __name__ == "__main__":
    import csv
    import xml.etree.ElementTree as ET
    from poligon import get_path, get_names
    from pathlib import Path

    dirName = 'revision_second_team'  # name of the directory where the checklists.csv are located
    fullPath = Path(Path.home(), 'Desktop', 'Работка', 'Работа-отчёты', 'CML_lab', 'testcases_CRP', 'scripts', dirName)
    xmlFile = Path(Path.home(), 'Desktop', 'Работка', 'Работа-отчёты', 'CML_lab', 'testcases_CRP', 'converted_scripts',
                   dirName)

    i = 0  # counter
    re = '\n'  # delimiter
    csvFile = get_path(fullPath)
    filename = get_names(fullPath)

    while i < len(filename):  # this loop iterates through all the files in the directory
        csv_file1 = csvFile['path'][i]  # add filename
        xml_file1 = str(filename[i])
        p = ET.Element('testsuite')
        a = 0
        xmlFileName1 = xml_file1 + '.xml'
        xmlPath = Path(xmlFile, xmlFileName1)

        with open(csv_file1, 'r', newline='', encoding='utf-8') as rf, open(xmlPath, 'w', newline='', encoding='utf-8') as wf:
            reader = csv.DictReader(rf, delimiter=",")

            for row in reader:  # this loop iterates through the lines in the i file
                numb = row['number']
                ind = row['indent']
                txt = row['text']
                nts = row['notes']
                a += 1
                comment = ' | <strong>comment:</strong> ' + txt + f'|{a}|'

                if int(ind) <= 1:
                    p.set('name', xml_file1)  # set name for
                    el1 = ET.SubElement(p, 'testsuite' + re)
                    el3 = ET.SubElement(el1, 'details')
                    el1.set('name', txt)
                    el3.text = '<strong>Desc:</strong> ' + txt + ' | ' + nts + comment  # in case the value is too
                    # long for field name test_link

                elif int(ind) > 1:
                    el2 = ET.SubElement(el1, 'testcase' + re)
                    el2.set('name', txt)
#                    el2.set('internalid', ind)
#                    subel0 = ET.SubElement(el2, 'externalid')
                    subel1 = ET.SubElement(el2, 'summary')
                    subel1.text = '<strong>Desc:</strong> ' + txt + nts + comment  # in case the value is too
                    # long for field name test_link

            ET.ElementTree(p).write(xmlPath, encoding="UTF-8", xml_declaration=True)
        i += 1
