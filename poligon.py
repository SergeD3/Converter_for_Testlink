import os


def get_path(x):
    try:
        i = 0
        ex = x
        file_list = []
        only_name = []
        dict_path = {}
        for file in os.listdir(ex):
            if file.endswith(".csv"):
                file_list.insert(i-1, os.path.join(ex, file))
                only_name.insert(i-1, file)
                dict_path = {'path': file_list, 'name': only_name}
            i += 1
        return dict_path
    except Exception as rx:
        print(rx)


def get_names(y):
    try:
        i = 0
        ns1 = []
        ff = get_path(y)
        for m in range(len(ff['name'])):
            i += 1
            ret_name = ff.get('name')
            ns = str(ret_name[i-1])
            ns1.insert(i, '.'.join(ns.split('.')[:-1]))  # обрезаем у каждого name
            # расширение .csv и собираем строку обратно
        return ns1
    except Exception as ex:
        print(ex)
