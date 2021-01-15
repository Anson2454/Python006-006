from django.test import TestCase

# Create your tests here.
import requests
import json
from fake_useragent import UserAgent
from pathlib import Path
from lxml import etree
import re
from loguru import logger


def get_comments():
    comments_list=[]
    urls = tuple((f'https://movie.douban.com/subject/1292052/comments?start={pageNo * 20}&limit=20&status=P&sort=new_score') for pageNo in range (1))
    # url = 'https://movie.douban.com/subject/1292052/comments?start=40&limit=20&status=P&sort=new_score'
    for url in urls:
        header ={'User-Agent':UserAgent().random} 
        try:
            r = requests.get(url,headers=header)
            selector = etree.HTML(r.text)
        except Exception as e:
            logger.error(f'请求错误: {e}')
        movie_name = selector.xpath('//*[@id="content"]/h1/text()')[0].split(' ')[0]
        nicknames = selector.xpath('//*[@id="comments"]/div/div[@class="comment"]/h3/span[@class="comment-info"]/a/text()')
        contents = selector.xpath('//*[@id="comments"]/div/div[@class="comment"]/p/span/text()')
        stars = selector.xpath('//*[@id="comments"]/div/div[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@class')
        comment_date = selector.xpath('//*[@id="comments"]/div/div[@class="comment"]/h3/span[@class="comment-info"]/span[@class="comment-time "]/@title')
        for i in list(zip(nicknames,contents,stars,comment_date)):
            stars = re.split('([0-9]+)',i[2])[1]
            # print(stars)
            comment_dict={'movie_name':movie_name,'nickname':i[0],'content':i[1],'stars':stars,'comment_date':i[3]}
            comments_list.append(comment_dict)
            # Comment.objects.create()
            
    # print(len(comments_list))
    return comments_list
        

if __name__ == "__main__":
#    print(get_comments()) 
    pass
  