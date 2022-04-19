import os


filelist = []
dirName = 'general-regression-actual-versions'
full_path = 'C:/Users/Серж/Desktop/testcases_CRP/scripts/' + dirName + '/'
ret = []
ff = {}


def getpath(x):
    i = 0
    for file in os.listdir(x):
        i += 1
        if file.endswith(".csv"):
            filelist.insert(i-1, os.path.join(x, file))
            ret.insert(i, file)
        _try = {'name': ret, 'path': filelist}
    return _try


def getnames():
    i = 0
    ff = getpath(full_path)
    for m in range(len(ff['name'])):
        i += 1
        retname = ff.get('name')
#        retpath = ff.get('path')
        ns = str(retname[i-1])
        ns1 = ns.rpartition('.')[0] # обрезаем у каждого name расширение .csv
        return ns1