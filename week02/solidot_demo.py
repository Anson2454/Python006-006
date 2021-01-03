import requests
import json
import re
from lxml import etree
from fake_useragent import UserAgent
from pathlib import *

class GetNews:
    def __init__(self):
        ua=UserAgent()
        self.headers={'User-Agent': ua.random}
        
    

    def get_news(self):
        news_infos=[]
        url='https://www.solidot.org/'
        res = requests.get(url,headers=self.headers)
        selector = etree.HTML(res.text)
        news=selector.xpath("//div[@id='main']/div[@id='center']/div[@class='block_m']/div/div[2]/h2/a/text()")
        pub_time = selector.xpath("//*[@id='center']/div[@class='block_m']/div[@class='talk_time']/text()[3]")
        # content = selector.xpath("//*[@id='center']/div[@class='block_m']/div[@class='p_content']/div[@class='p_mainnew']/text()")
        news_info = dict(zip(news,pub_time))
        # print(movie_infos)
        for title in news_info:
            news_infos.append({'title':title,'publish_time':news_info[title]})
        return  news_infos


    def save_page(self,file):
        try:
            with open(file,'w',encoding='utf-8') as f:
                f.write(str(res))
        except FileNotFoundError as e:
            print(f'文件无法打开：{e}')
        except IOError as e:
            print(f'文件读写出错: {e}')
        except Exception as e:
            print(e)
    



if __name__ == "__main__":

    p=Path(__file__)  #获取当前文件绝对路径
    pyfile_path=p.resolve().parent #获取父目录
    # print(pyfile_path)

    # 定义需要保存的目标文件夹，不存在则新建
    result_path= pyfile_path.joinpath('pageResults') 
    # print(result_path)
    if not result_path.is_dir():
        Path.mkdir(result_path)
    page =result_path.joinpath('content.json') # 最终存放的文件绝对路径
    # print(page)
    news=GetNews()
    res=news.get_news()
    news.save_page(page)
   