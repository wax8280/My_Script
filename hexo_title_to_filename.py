# coding:utf-8
"""
从hexo的post里面提取出title作为文件名

python hexo_title_to_filename.py "c:\folder"
"""
if __name__ == '__main__':
    import re
    import os
    import sys

    if len(sys.argv) < 2:
        rootdir=os.getcwd()
    else:
        rootdir = sys.argv[1]

    to_rootdir = os.path.join(rootdir, 'target')
    if not os.path.exists(rootdir):
        print (u'无效的目录')
        exit(0)

    if not os.path.exists(to_rootdir):
        os.mkdir(to_rootdir)

    for i in os.listdir(rootdir):
        if not os.path.isdir(os.path.join(rootdir, i)):
            # 寻找所有md文件
            if i.lower().endswith('md'):
                buff = []
                filename = i.replace('.md', '')
                create_data = ''

                with open(os.path.join(rootdir, i)) as f:
                    for l in f.readlines():
                        a = re.match('title: (.*?)\n', l)
                        d = re.match('date: (.*?) ', l)
                        if a:
                            filename = a.group(1)

                        if d:
                            create_data = d.group(1)

                        buff.append(l)

                dir = os.path.join(to_rootdir, filename + '.md').decode('utf-8').encode('gbk')
                if os.path.exists(dir):
                    dir = os.path.join(to_rootdir, filename + ' ' + create_data + '.md').decode('utf-8').encode('gbk')
                with open(dir, 'w') as f:
                    f.write(''.join(buff))
