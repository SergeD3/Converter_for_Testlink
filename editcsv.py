# import csv
# from poligon import getpath, getnames
#
# dirName = 'completed-regression-test-runs'  # name of the directory where the checklists.csv are located
# full_path = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/'  # full path to the
# # directory with checklists
#
# i = 0  # counter
# csvFile = getpath(full_path)
# filename = getnames(full_path)
#
# # while i < len(filename):  # this loop iterates through all the files in the directory
#     csvfile1 = csvFile['path'][i]
#     with open(csvfile1, 'r', newline='', encoding='utf-8') as rf, open(csvfile1, 'w', newline='', encoding='utf-8') as wf:
#         reader1 = csv.reader(rf, delimiter=",")
#         for row1 in reader1:
#             if row1.strip("\n") != "nickname_to_delete":
#
#     i += 1
#
# # , open(csvfile1, 'w', newline='', encoding='utf-8') as wf: