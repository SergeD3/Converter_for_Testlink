import os


def getpath(x):
    i = 0
    filelist = []
    onlyname = []
    dictpath = {}
    for file in os.listdir(x):
        if file.endswith(".csv"):
            filelist.insert(i-1, os.path.join(x, file))
            onlyname.insert(i-1, file)
            dictpath = {'path': filelist, 'name': onlyname}
        i += 1
    return dictpath


def getnames(y):
    i = 0
    ns1 = []
    ff = getpath(y)
    for m in range(len(ff['name'])):
        i += 1
        retname = ff.get('name')
        ns = str(retname[i-1])
        ns1.insert(i, '.'.join(ns.split('.')[:-1])) # обрезаем у каждого name расширение .csv и собираем строку обратно
    return ns1