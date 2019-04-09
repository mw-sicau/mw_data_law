import re
import requests
from json import loads
from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败


drivers = webdriver.Chrome(options=chrome_options)
wb = Workbook()
ws = wb.worksheets[0]
ws.append(['行政区划', '地址', '小区名称', '户型', '面积', '所在楼层', '朝向', '最终价',
           '评估价', '成交时间', '报名人数', '设置提醒人数', '围观次数',
           '出价次数', '保证金', '加价幅度', '地理坐标', '交易状态', '房屋ID'])

Headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
    'Content-Type': 'application/json',
}

page_url = 'https://sf.taobao.com/item_list.htm?spm=a213w.7398504.pagination.2.63231b954JiSrp&category=50025969&auction_source=0&city=%B3%C9%B6%BC&sorder=2&st_param=-1&auction_start_seg=-1&page='
rqtSession = requests.Session()


def get_page(pageurl):
    r = rqtSession.get(
        pageurl,
        headers=Headers)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'lxml')
        return soup
    else:
        return 0


def get_detail(url):
    address = re.compile(r'(?<=】)\S+')
    district = re.compile(r'(?<=】)\S+[市区县]')
    floors = re.compile(r'-*\d+[层楼]')
    try:
        drivers.get(url)
        drivers.implicitly_wait(2)  # 等待2s
        element = drivers.find_element_by_xpath('//*[@id="J_DetailTabMenu"]/li[3]/a')
        ActionChains(drivers).move_to_element(element).click(element).perform()

        title = drivers.find_element_by_xpath('//*[@id="page"]/div[4]/div/div/h1').text
        district = district.search(title[:16]).group().title()
        address = address.search(title).group().title()
        floors = floors.search(title).group().title().replace('层', '楼')
        final_price = drivers.find_element_by_xpath('//*[@id="sf-price"]/div/p[1]/span/em').text
        security_deposit = drivers.find_element_by_xpath('//*[@id="J_HoverShow"]/tr[2]/td[1]/span[2]/span').text
        evaluation_price = drivers.find_element_by_xpath('//*[@id="J_HoverShow"]/tr[3]/td[1]/span[2]/span').text
        markups = drivers.find_element_by_xpath('//*[@id="J_HoverShow"]/tr[1]/td[2]/span[2]/span').text
        coordinate = drivers.find_element_by_xpath('//*[@id="J_Coordinate"]').get_attribute('value')
        end_time = drivers.find_element_by_xpath('//*[@id="page"]/div[4]/div/div/div[2]/ul/li[2]/span[2]').text
        try:
            community = drivers.find_element_by_xpath('//*[@id="J_ItemSummary"]/div/div[2]/div[2]/p[1]/span[2]').text
            house_type = drivers.find_element_by_xpath('//*[@id="J_ItemSummary"]/div/div[2]/div[2]/p[2]/span[2]').text
            area = drivers.find_element_by_xpath('//*[@id="J_ItemSummary"]/div/div[2]/div[2]/p[3]/span[2]').text
            # use = drivers.find_element_by_xpath('//*[@id="J_ItemSummary"]/div/div[2]/div[2]/p[4]/span[2]').text
            face = drivers.find_element_by_xpath('//*[@id="J_ItemSummary"]/div/div[2]/div[2]/p[5]/span[2]').text

        except:
            try:

                detail = drivers.find_element_by_xpath('//*[@id="J_desc"]/table/tbody').text
                if '面积'  in detail:
                    area = re.search(r'\d+(\.\d+)?[㎡平]', detail).group().replace('平','㎡')

            except:
                area = '未知'
            face = '未知'
            community = '未知'
            house_type = '未知'

        apply_count = drivers.find_element_by_xpath('//*[@id="page"]/div[4]/div/div/div[2]/div[3]/span[1]/em').text
        notiy_count = drivers.find_element_by_xpath('//*[@id="J_NotifyNum"]').text
        looker_count = drivers.find_element_by_xpath('//*[@id="J_Looker"]').text
        bid_count = drivers.find_element_by_xpath('//*[@id="J_DetailTabMenu"]/li[4]/a/span').text
        return [district, address, community, house_type, area, floors, face, final_price,
                evaluation_price, end_time, apply_count, notiy_count, looker_count,
                bid_count, security_deposit, markups, coordinate,
                ]
    except:
        print(url)
        return url


err_count = 0
house_count = 0
err_page_url = open('Error_page_url.txt', 'a+', encoding='utf-8')

try:
    for i in range(1, 151):
        try:
            soup = get_page(page_url + str(i))
            house_info = loads(soup.find(id='sf-item-list-data').text)['data']
            for house in house_info:
                info = get_detail('http:' + house['itemUrl'])
                if isinstance(info, list):
                    house_count += 1
                    info.append(house['status'])
                    info.append(house['id'])
                    print('正在爬取第%d页，已经爬取%d条数据，错误%d条:' % (i, house_count, err_count))
                    print(info)
                    ws.append(info)
                else:
                    err_count += 1
                    err_page_url.writelines(info + '\n')
        except:
            continue
finally:
    wb.save('房屋数据.xlsx')
    drivers.close()
    err_page_url.close()
