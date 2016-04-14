#!/usr/bin/env python
#coding:utf8
import sys,re
import requests
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )

# appName="记健康"
# versionREsting='\d{1,2}\.\d{1,2}\.\d{1,2}'

# 应用名字，此处以微信举例
appName="微信"
# 应用版本号（6.3.15.49）的正则表达式
versionREsting='\d{1,2}\.\d{1,2}\.\d{1,2}.\d{1,2}'

def getUrlContent(appSearchUrl):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    htmlContent=requests.get(appSearchUrl,headers=headers).text
    return htmlContent

def huawei(appName):
    # 各应用商店内对某应用的搜索页
    appSearchUrl="http://appstore.huawei.com/search/"+appName
    # 获取搜索页HTML的内容
    searchHtmlContent=getUrlContent(appSearchUrl)
    # 将HTML传入BeautifulSoup的构造方法
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    # 使用BeautifulSoup的select方法找到该应用的网址
    appExactUrl=htmlBeautifulSoup.select('.game-info-ico')[0].a['href']
    # 获取应用详情页HTML的内容，并传入BeautifulSoupr的构造方法
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    # 获取版本号相关的字符串
    versionString=appExactUrl_bs.select('.ul-li-detail')[3].text
    # 使用正则处理，得到准确版本号
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def anzhuoMarket(appName):
    appSearchUrl="http://apk.hiapk.com/search?key="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.list_title')[0].a['href']
    appExactUrl=r"http://apk.hiapk.com"+appExactUrl
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('#appSoftName')[0].text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def anzhiMarket(appName):
    appSearchUrl="http://www.anzhi.com/search.php?keyword="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.app_icon')[0].a['href']
    appExactUrl=r"http://www.anzhi.com"+appExactUrl
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('.app_detail_version')[0].text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def yingyonghui(appName):
    appSearchUrl="http://www.appchina.com/sou/"+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.app-info')[0].h1.a['href']
    appExactUrl=r"http://www.appchina.com"+appExactUrl
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('.app-setup')[0]['meta-versionname']
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def nduoMarket(appName):
    appSearchUrl="http://www.nduoa.com/search?sk=a25b4bbacbb702d81d4df8c701c74a93&q="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.name')[10].a['href']
    appExactUrl=r"http://www.nduoa.com"+appExactUrl
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('.version')[0].text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def xiaomi(appName):
    appSearchUrl="http://app.mi.com/search?keywords="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.applist')[0].a['href']
    appExactUrl=r"http://app.mi.com"+appExactUrl
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('.details')[0].ul.li.next_sibling.next_sibling.next_sibling.text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def wandoujia(appName):
    appSearchUrl="http://www.wandoujia.com/search?key="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.i-source')[0]['data-pn']
    appExactUrl=r"http://www.wandoujia.com/apps/"+appExactUrl
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.find_all('dd')[2].next_sibling.next_sibling.next_sibling.next_sibling.text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def sougou(appName):
    appSearchUrl="http://zhushou.sogou.com/apps/search.html?key="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.list')[0].a['href']
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('.info')[0].tr.td.next_sibling.next_sibling.text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def mumayi(appName):
    appSearchUrl="http://s.mumayi.com/index.php?q="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.applist')[0].a['href']
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('.iappname')[0].text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def market360(appName):
    appSearchUrl="http://zhushou.360.cn/search/index/?kw="+appName
    searchHtmlContent=getUrlContent(appSearchUrl)
    htmlBeautifulSoup=BeautifulSoup(searchHtmlContent,'html.parser')
    appExactUrl=htmlBeautifulSoup.select('.title')[0].next_sibling.next_sibling.next_sibling.next_sibling.li.dl.dt.a['href']
    appExactUrl=r"http://zhushou.360.cn/"+appExactUrl
    appHtmlContent=getUrlContent(appExactUrl)
    appExactUrl_bs=BeautifulSoup(appHtmlContent,'html.parser')
    versionString=appExactUrl_bs.select('.base-info')[0].tr.next_sibling.next_sibling.td.text
    exactVersion= re.search(versionREsting,versionString).group()
    return exactVersion

def meizu(appName):
    pass

def zhushou91(appName):
    pass

def tencent(appName):
    pass

def youyiMarket(appName):
    pass

def baidu(appName):
    # 搜索结果有广告嫌疑
    pass
