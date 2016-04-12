抓取各安卓应用商店某指定应用的版本号，使用requests模块获得HTML内容，BeautifulSoup解析，再配以正则表达式得到版本号

### 原理
* 根据应用名字获取各商店该应用的搜索页内容
*  使用BeautifulSoup构造方法，获得该应用的网址
*  对该应用的网址再次使用BeautifulSoup构造方法，取得包含有版本号信息的字符串
*  正则表达式处理，得到精确版本号

### 已包含应用商店
* [小米](http://app.mi.com/)
*  [华为](http://appstore.huawei.com/)
*  [豌豆荚](http://www.wandoujia.com/apps)
*  [搜狗手机助手](http://zhushou.sogou.com/apps/)
*  [应用汇](http://www.appchina.com/)
*  [n多网](http://www.nduoa.com/)
*  [安卓市场](http://apk.hiapk.com/)
* [安智市场](http://www.anzhi.com/)

