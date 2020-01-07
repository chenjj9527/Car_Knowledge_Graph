# 实例
from requests_html import HTMLSession
from requests_html import HTML
import requests
import time
import json
import random

session = HTMLSession()
#urlroot = 'https://car.autohome.com.cn/'
url = 'https://www.autohome.com.cn/4392/'

def getInstance():
    response = session.get(url)
    response.html.render()

    cars = response.html.find('.spec-wrap dl dd div.spec-name p a')
    for car in cars:
        print(car.text)
    #print(cars)
#写入CSV文件
def save2csc(writer,bank,num,url):
        header = ['','car' 'url']
        #writer.writerow(header)
        csvrow1 = []
        csvrow1.append(bank)
        csvrow1.append(num)
        csvrow1.append(url)
        writer.writerow(csvrow1)
if __name__ == '__main__':
    print("开始处理")
    getInstance()
    print("处理结束")


