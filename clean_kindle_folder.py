# coding:utf-8
"""
当你在Kindle上删除书本时，Kindle并不会自动清理记录阅读进度等信息的文件。
本剧本用于自动清理这些没用的文件，以提高Kindle的运行速度。
python clean_kindle_folder.py "e:\fdocuments"
"""
if __name__ == '__main__':
    import os
    import shutil
    import sys

    if len(sys.argv) < 2:
        print (u"请填写Kindle的'documents'文件夹路径")
        exit(0)

    rootdir = sys.argv[1]
    book_list = []
    dir_list = []
    del_dir_list = []
    # 排除字典文件夹
    exist_book_dir_list = ['dictionaries']
    # 书的种类
    book_type = ['mobi', 'pdf', 'txt', 'azw', 'azw3', 'kfx', 'pobi']

    try:
        dir_gen = os.listdir(rootdir)
    except:
        print(u"非法目录")
        exit(0)

    for i in os.listdir(rootdir):
        if os.path.isdir(os.path.join(rootdir, i)):
            dir_list.append(os.path.join(rootdir, i))
        else:
            for t in book_type:
                if i.lower().endswith(t):
                    book_list.append(i[:len(i) - len(t) - 1])

    for each_dir in dir_list:
        for each_book in book_list:
            if each_book in each_dir:
                exist_book_dir_list.append(each_dir)

    del_dir_list = set(dir_list) - set(exist_book_dir_list)

    if del_dir_list:
        print (u"即将要删除的目录。确认删除请键入'y'")
        for i in del_dir_list:
            print (i)

        if raw_input() == 'y':
            for i in del_dir_list:
                shutil.rmtree(i)
                print (u'正在删除 {}'.format(i.decode('gbk').encode('utf-8')))
    else:
        print (u'您的目录是干净的')
