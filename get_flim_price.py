# coding:utf-8
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from queue import LifoQueue
from pyquery import PyQuery
import os
import re


def parser_web_page(name, path, d):
    with open(path, 'r', encoding='gb18030') as f:
        r = f.read()
    a = re.findall('img alt="(.*?)" src.*?c-price">(.*?) </sp', r, re.DOTALL)
    try:
        pass
    except:
        print(path)
    if name not in d:
        d.update({name: []})
    # r = [{'title': i('p.desc a').text(), 'price': i('.price').text()} for i in pq('.detail').items()]
    # for i in pq('.detail').items():
    #     print(i.text())
    d[name].extend(a)


if __name__ == '__main__':
    rootdir = 'D:\downloads\新建文件夹'

    name_l = ['上文', '乐玩', 'irohas', 'F212', '金厦']
    d = {}
    film = {
        '伊尔福': ['pan 400', 'pan 100', 'hp5', 'delta 100', 'delta 400', 'fp4', 'delta 3200', 'panf', 'xp2', 'sfx 200'],
        '乐凯': ['100'],
        '爱克发': ['apx 100', 'apx 400', 'vista 400', 'vista 200', 'ct100'],
        '柯达': ['tmax 100', 'tmax 400', 'tri-x 400', 'color plus 200', 'proimage', 'portra 400', 'portra 160',
               'ektar 100', 'ultramax 400', '金 200'],
        '禄来': ['rpx 100', 'rpx 400', 'retro 400', 'retro 80', 'rpx 25', 'ortho 25', 'superpan 200', 'infrared 400',
               'vario chrome', 'cr200', 'cn200'],
        '福马': ['r 100','pan 100', 'pan 400', 'pan 200', '320'],
        '富士': ['acros 100', 'provia 100f', 'c200', '业务 100', '业务 400', 'velvia 50', 'pro 400', 'rxp 400', 'pro 160',
               'natura 1600', 'premium 400', 'velvia 100', 'velvia 50', 'tra 400', 'venus 800','color 100'],
        'adox': ['silvermax 100'],
        'bergger': ['pancro 400'],
        'kentmere': ['100', '400'],
        '东方海鸥': ['400', '100']
    }

    exclude_kw=['傻瓜','一次相机','过期','盘片','分装','五卷']
    mustneed_kw=['135','120']

    for film_info in os.listdir(rootdir):
        if not os.path.isdir(os.path.join(rootdir, film_info)):
            for n in name_l:
                if n in film_info:
                    parser_web_page(n, os.path.join(rootdir, film_info), d)


    result={}
    for taobao_name, film_info_list in d.items():
        for film_info in film_info_list:
            title = film_info[0].lower()
            price=film_info[1]

            out=False
            for mkw in mustneed_kw:
                if mkw in title:
                    out=False
                    break
                else:
                    out=True

            for ekw in exclude_kw:
                if ekw in title:
                    out=True

            if not out:
                flag = False
                for film_fact in film.keys():
                    if film_fact in title:
                        for count, film_type in enumerate(film[film_fact]):
                            kw = film_type.split(' ')

                            c = 0
                            for each_kw in kw:
                                if each_kw in title:
                                    c += 1
                                if c == len(kw):
                                    flag = True

                            if flag is True:
                                if '135' in title:
                                    k=film_fact+' '+film_type+'(135)'
                                elif '120' in title:
                                    k=film_fact+' '+film_type+'(120)'

                                if '24' in title:
                                    k+=' 24'

                                if k not in result:
                                    result.update({k:[]})

                                result[k].append([taobao_name,price])
                                # print(title, film_fact, film_type)
                                break
                        if flag is False:
                            print('not find', title)

    for k,v in result.items():
        print(k)
        print(v)

    print('pass')