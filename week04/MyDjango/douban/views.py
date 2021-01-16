from django.shortcuts import render ,HttpResponseRedirect

# Create your views here.
# from douban.models import Comment
from .models import Comment
from .models import Comment_test
import requests
from fake_useragent import UserAgent
from lxml import etree
import re
from loguru import logger


# def get_comments(request):
#     comments_list = []
#     urls = tuple(
#         (f'https://movie.douban.com/subject/1292052/comments?start={pageNo * 20}\
#          &limit=20&status=P&sort=new_score') for pageNo in range(10))
#     # url = 'https://movie.douban.com/subject/1292052/comments?start=40&limit=20&status=P&sort=new_score'
#     for url in urls:
#         header = {'User-Agent': UserAgent().random}
#         try:
#             r = requests.get(url, headers=header)
#             selector = etree.HTML(r.text)
#         except Exception as e:
#             logger.error(f'请求错误: {e}')
#         movie_name = selector.xpath('//*[@id="content"]/h1/text()')[0].split(' ')[0]
#         nicknames = selector.xpath(
#             '//*[@id="comments"]/div/div[@class="comment"]/h3/span[@class="comment-info"]/a/text()')
#         contents = selector.xpath('//*[@id="comments"]/div/div[@class="comment"]/p/span/text()')
#         stars = selector.xpath(
#             '//*[@id="comments"]/div/div[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@class')
#         comment_date = selector.xpath(
#             '//*[@id="comments"]/div/div[@class="comment"]/h3/span[@class="comment-info"]/span[@class="comment-time "]/@title')
#         for i in list(zip(nicknames, contents, stars, comment_date)):
#             if i[2].startswith('allstar'): 
#                 stars = re.split('([0-9]+)', i[2])[1]
#             else:
#                 logger.error(f'这条数据没有星级评分,昵称为{i[0]}')
#                 continue
#             # print(i)
#             stars = float(int(stars)/10)
#             comment_dict = {'movie_name': movie_name, 'nickname': i[0], 'content': i[1], 'stars': stars,
#                             'comment_date': i[3]}
#             comments_list.append(comment_dict)
            # Comment.objects.create(movie_name=movie_name, nickname=i[0], content=i[1], rate=stars,comment_date=i[3])
            # try:
            #     Comment_test.objects.create(movie_name=movie_name, nickname=i[0], content=i[1], rate=stars,comment_date=i[3])
            # except Exception as e:
            #     logger.error(f'插入数据库错误:{e},错误的nickname为{i[0]}')

def query_comments(request):
    # get_comments()
    queryset = Comment.objects.all() 
    conditions = {'rate__gt':3}   
    comments = queryset.filter(**conditions)
    return render(request,'index.html',locals())


def index(request):
    return  HttpResponseRedirect('/douban/movie')