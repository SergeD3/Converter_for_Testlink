import os
from pathlib import *


fName = 'smoke'
dirName = 'smoke'
csvFile = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/' + fName + '.csv'
xmlFile = 'C:/Users/Серж/Desktop/testcases_CRP/converted_scripts/' + dirName + '/' + fName + '.xml'

csv_path = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/general-regression-actual-versions/'
filelist = []
nameslist = []


def getpath(csv_path):
    for root, dirs, files in os.walk(csv_path):
        for file in files:
            filelist.append(os.path.join(root, file))
    for name in filelist:
        nameslist = name
        return nameslist


# def lstnmb(x, i):   функция для сохранения значения numb == 1 из цикла
#     pastiter.insert(i, x)