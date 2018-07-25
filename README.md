### A questionnaire website app by django

部署地址:

http://goqing123.com.cn:8000

本项目是一个在线问卷调查的网页APP。用户访问页面时，Nginx将处理前端的静态文件请求，而动态请求则通过uwsgi传递给django进行处理。接收到动态请求后，django调用后台数据库MariaDB或缓存数据库Redis提取数据，然后通过其自带的模版引擎渲染出Html的主体内容框架。

基本的技术架构如下所示：
The web client <-> Nginx <-> the socket <-> uWSGI <-> Django <-> Redis <-> MariaDB

前端正在逐步引入Vue框架，同时把后端重构为Restful API，前后端通过axios库传输数据。为了美化页面和用图表对数据进行展示，前端还使用了bootstarp，element-ui，Echarts等库。


### To-do list
* 主页需增加搜索栏，内页分页逻辑，已经一个根据问卷发布时间的过滤器
* add more polls type.
* check same ip.
* use spider to collect polls from other site.
* try docker

