import scrapy
import os
import requests
from urllib.parse import urlparse

from scrapy import Request, Selector

class Hanime1Spider(scrapy.Spider):
    name = "hanime1"
    allowed_domains = ["hanime1.me"]
    start_urls = ["https://hanime1.me/search?genre=%E8%A3%8F%E7%95%AA"]

    def start_requests(self):
        for page in range(1,71):
            url =self.start_urls[0]+f"&page={page}"
            yield Request(url=url,
                     callback=self.parse)

    def parse(self, response,**kewargs):

        links = response.css('#home-rows-wrapper > div.home-rows-videos-wrapper > a::attr(href)').extract()
        
        for link in links:
            if('hanime' in link):
                # print(link)
                yield Request(url=link,
                              callback=self.parse_anime)

    def parse_anime(self,response):
        # 提取所有视频源链接
        video = response.css("video source::attr(src)").extract()
        url = None
        if video:
            print("找到视频源链接:")
            if(len(video[2])>2):
                print(video[2])
                url = video[2]
            elif( len(video[1])>1):
                print(video[1])
                url = video[1]
            else:
                print(video[0])
                url = video[0]




        else:
            print("未找到视频源链接")
            
        # 如果找到了视频链接，下载视频
        if url:
            self.download_video(url)
            
    def download_video(self, video_url):

        # 创建dianying文件夹
        download_dir = "dianying"#下载目录的名称
        if not os.path.exists("D:\\"+download_dir):#判断D盘下是否存在这个文件夹
            os.makedirs("D:\\"+download_dir)#如果不存在则创建文件夹

        # 从URL中提取文件名
        parsed_url = urlparse(video_url)#提取文件路径名如https://www.example.com/video.mp4，path会提取为/video.mp4，层级更多的话会一并 提取出来

        filename = os.path.basename(parsed_url.path)#这个函数用来提取path之中最底下的那个文件名，如/video.mp4，则提取出来video.mp4

        # 完整的文件路径
        file_path = os.path.join("D:\\",download_dir, filename)#这里进行了拼接，得到完整路径
        
        print(f"开始下载: {video_url}")
        print(f"保存到: {file_path}")
        
        try:
            # 下载视频
            response = requests.get(video_url, stream=True)#用requests库下载视频，并保存返回值到response变量中
            response.raise_for_status()
            
            # 写入文件
            with open(file_path, 'wb') as f:
                f.write(response.content)#这里写入response.content
                        
            print(f"下载完成: {filename}")
            
        except Exception as e:
            print(f"下载失败: {e}")
