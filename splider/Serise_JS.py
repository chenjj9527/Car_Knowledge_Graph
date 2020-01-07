from requests_html import HTMLSession
from requests_html import HTML
import requests
import time
import json
import random
import sys
import os
import csv

urlroot = "https://car.autohome.com.cn"
#url = 'https://car.autohome.com.cn/price/brand-33.html'

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
# 品牌列表
def get_bank():
    current_dir = os.path.abspath('.')
    print(current_dir)
    file_name1 = os.path.join(current_dir, "data\\type.csv")
    file_name2 = os.path.join(current_dir, "data\\bank.csv")
    #
    with open(file_name1, 'wt',newline='')  as csvfile1:
        #header = ['bank','Type','Count']
        writer = csv.writer(csvfile1)
        #writer.writerow(header)
        # 读取并获得所有URL地址，同时记录品牌名称
        with open(file_name2, 'r') as csvfile2:
            reader = csv.reader(csvfile2)
            for row in reader:
                # 随机浏览器 User-Agent
                headers = {"User-Agent": random.choice(USER_AGENTS)}
                session = HTMLSession()

                # 01:读取整行
                column1 = row[0]    # 读取第1列
                column3 = row[2]    #读取第2列
                # 逐个URL进行爬取
                response = session.get(column3, headers=headers)
                response.html.render()
                print("URL=",column3)

                banks = response.html.find('.cartree ul li dd a')
                for bank in banks:
                    bk = bank.text
                    #逆序查找：车系
                    start = bk.rfind("(")
                    end = bk.rfind(")")
                    bank1 = bk[0:start]
                    Num = bk[(start + 1):end]

                    url2 = urlroot + bank.attrs.get("href", None)
                    print(column1+" "+bank1 + " " +Num,url2)

                    save2csv(writer,column1, bank1.rstrip(), Num,url2)
                    csvfile1.flush()
                print(banks)
                time.sleep(1)
#写入CSV文件
def save2csv(writer,bank,type,num,url):
        #header = ['bank','num' 'url']
        #writer.writerow(header)
        csvrow1 = []
        csvrow1.append(bank)
        csvrow1.append(type)
        csvrow1.append(num)
        csvrow1.append(url)
        try:
            writer.writerow(csvrow1)
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
if __name__ == '__main__':
    #get_url()
    get_bank()
    print("处理结束")


