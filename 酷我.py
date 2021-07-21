import json

import requests
from bs4 import BeautifulSoup
import re

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}
#单独获取音乐下载地址
def  getmusic(musicid):
    url=f'http://www.kuwo.cn/play_detail/{musicid}'
    musicurl=f'http://www.kuwo.cn/url?format=mp3&rid={musicid}&response=url&type=convert_url3&br=320mp3&from=web&t=1614087330073&httpsStatus=1'
    response=requests.get(url=musicurl,headers=header).text
    response_tit=requests.get(url=url,headers=header).text
    bftit=BeautifulSoup(response_tit,'lxml')
    title = bftit.title.string
    jstxt=json.loads(response)
    print(title+jstxt['url'])
    #下载歌曲到本地
    # kuwo_mp3=requests.get(url=jstxt['url'],headers=header).content
    # mp3_path=f'E:\items\vscode\酷我音乐下载\{title}'+'.mp3'
    # with open(mp3_path,'wb') as fp:
    #     fp.write(kuwo_mp3)
    # fp.close()
    # print(title,'下载成功')

#批量下载音乐地址
if __name__ == '__main__':
    print('输入歌曲的rid：音乐地址的后几位数字')
    getmusic(input())