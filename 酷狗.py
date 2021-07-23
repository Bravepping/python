import json
import os
import requests
from bs4 import BeautifulSoup
import re

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

def getkugou(urlhash,urlid):
    url=f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={urlhash}&dfid=4WGKSP1nYr0E0fcRQV3EbPqo&mid=71fef0038b7a801273d536d743cba0cf&platid=4&album_id={urlid}'
    response=requests.get(url=url,headers=header)
    #转为json对象
    music=response.json()
    #获取音乐名称与作者
    music_name=music['data']['audio_name']
    #获取音乐下载地址
    music_url=music['data']['play_url']
    print(music_name+'：'+music_url)
    #下载到本地
    responsedown=requests.get(url=music_url)
    musicfile=responsedown.content    
    #定义下载目录
    musicpath="E:\音乐下载\酷狗"
    folder=os.path.exists(musicpath)
    if not folder:
        os.makedirs(musicpath)        
        mp3_path=f'{musicpath}\{music_name}'+'.mp3'
        with open(mp3_path,'wb') as fp:
            fp.write(musicfile)
        fp.close()
        print(music_name,'下载成功_保存地址：'+musicpath)
    else:
        mp3_path=f'{musicpath}\{music_name}'+'.mp3'
        with open(mp3_path,'wb') as fp:
            fp.write(musicfile)
        fp.close()
        print(music_name,'下载成功_保存地址：'+musicpath)
    os.close
#酷狗音乐下载
if __name__ == '__main__':
    print('输入歌曲地址中的hash')
    urlhash=input()
    print('输入歌曲地址中的idalbum_id')
    urlid=input()
    getkugou(urlhash=urlhash,urlid=urlid)