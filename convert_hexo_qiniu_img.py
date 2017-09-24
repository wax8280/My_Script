# coding:utf-8
"""
我的博客使用hexo的一个七牛插件，其图片的模板与md写的不一样。

qiniu:{% qnimg ./922-1.jpg title:"Rollei 35T" %}
md:![Rollei 35T](./922-1.jpg)

本脚本用于两者之间的转换。
python convert_hexo_qiniq_img.py qiniu "c:\folder"
"""
if __name__ == '__main__':
    import os
    import re
    from string import Template
    import sys

    if len(sys.argv) < 3:
        print (u"参数错误")
        exit(0)

    rootdir = sys.argv[2]
    conv_type=sys.argv[1]

    TO_QINIU = 'qiniu'
    TO_MD = 'md'

    to_rootdir = os.path.join(rootdir, 'target')
    if not os.path.exists(rootdir):
        print (u'无效的目录')
        exit(0)

    if not os.path.exists(to_rootdir):
        os.mkdir(to_rootdir)

    md_template = Template('![$title]($path)\n')
    qiniu_template = Template('{% qnimg $path title:"$title" %}\n')

    md_pattern = '!\[(.*?)\]\((.*?)\)$'
    qiniu_title_pattern = '\{%\s+qnimg\s+(.*?)\s+title:"*(.*?)"*\s+%\}'
    qiniu_pattern = '\{%\s+qnimg\s+(.*?)\s+%\}'

    for i in os.listdir(rootdir):
        if not os.path.isdir(os.path.join(rootdir, i)):
            # 寻找所有md文件
            if i.lower().endswith('md'):
                buff = []

                with open(os.path.join(rootdir, i)) as f:
                    for l in f.readlines():
                        if conv_type == TO_QINIU:
                            a = re.match(md_pattern, l)
                            if a:
                                _path = a.group(2)
                                _title = a.group(1)
                        elif conv_type == TO_MD:
                            a = re.match(qiniu_title_pattern, l)
                            if a:
                                _path = a.group(1).replace('"', '')
                                _title = a.group(2)
                            if not a:
                                a = re.match(qiniu_pattern, l)
                                if a:
                                    _path = a.group(1).replace('"', '')
                                    _title = ''
                        if a:
                            if conv_type == TO_QINIU:
                                buff.append(qiniu_template.substitute(path=_path, title=_title))
                            elif conv_type == TO_MD:
                                buff.append(md_template.substitute(path=_path, title=_title))
                        else:
                            buff.append(l)

                with open(os.path.join(to_rootdir, i), 'w') as f:
                    f.write(''.join(buff))
