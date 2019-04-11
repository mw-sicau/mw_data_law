# -*- coding: utf-8 -*-

# Scrapy settings for lianjia_info project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjia_info'

SPIDER_MODULES = ['lianjia_info.spiders']
NEWSPIDER_MODULE = 'lianjia_info.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'lianjia_info (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    'Cookia':'TY_SESSION_ID=9408d320-0316-40aa-8a93-df3b34605af8; lianjia_uuid=3dcdebe7-4d17-4699-afa5-d183eafc8651; _smt_uid=5cab52d0.26a6883a; UM_distinctid=169fd3b7e7c3d-012a2f805a0a8b-e323069-144000-169fd3b7e7d124; _jzqy=1.1554731729.1554731729.1.jzqsr=baidu|jzqct=lianjia.-; _ga=GA1.2.1273763883.1554731733; gr_user_id=186d8b3a-f646-407d-ad02-d0a4c8c6ac7c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22169fd3b820129f-0e51c7c0139552-e323069-1327104-169fd3b820241b%22%2C%22%24device_id%22%3A%22169fd3b820129f-0e51c7c0139552-e323069-1327104-169fd3b820241b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22sousuo%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; select_city=510100; _jzqckmp=1; _gid=GA1.2.1898490692.1554942844; _jzqx=1.1554737228.1554960070.3.jzqsr=cd%2Elianjia%2Ecom|jzqct=/.jzqsr=cd%2Elianjia%2Ecom|jzqct=/ershoufang/106102109571%2Ehtml; lianjia_ssid=702198fe-8ca9-4d93-8901-7e5f129ae136; CNZZDATA1255633284=860930664-1554727992-https%253A%252F%252Fwww.lianjia.com%252F%7C1554981840; CNZZDATA1253492306=168976354-1554731433-https%253A%252F%252Fwww.lianjia.com%252F%7C1554982770; CNZZDATA1254525948=1659732917-1554731571-https%253A%252F%252Fwww.lianjia.com%252F%7C1554985412; CNZZDATA1255604082=295719053-1554731692-https%253A%252F%252Fwww.lianjia.com%252F%7C1554985540; gr_session_id_a1a50f141657a94e=db0ee942-27a5-4c70-a2b7-b6eaad3cbcf1; gr_session_id_a1a50f141657a94e_db0ee942-27a5-4c70-a2b7-b6eaad3cbcf1=true; all-lj=26155dc0ee17bc7dec4aa8e464d36efd; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1554942841,1554980687,1554985001,1554987248; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1554987248; _qzja=1.1154655786.1554731802251.1554985001149.1554987248283.1554986600124.1554987248283.0.0.0.91.14; _qzjc=1; _qzjto=48.6.0; _jzqa=1.3356696418354281500.1554731729.1554985001.1554987248.14; _jzqc=1; _jzqb=1.1.10.1554987248.1; _qzjb=1.1554980687146.21.0.0.0; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'lianjia_info.middlewares.LianjiaInfoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'lianjia_info.middlewares.LianjiaInfoSpiderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'lianjia_info.pipelines.LianjiaInfoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
