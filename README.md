### A questionnaire website app by django

部署地址:
http://goqing123.com.cn:8000

本项目是一个在线问卷调查的网页APP。用户访问页面时，Nginx将处理前端的静态文件请求，而动态请求则通过uwsgi传递给django进行处理。接收到动态请求后，django调用后台数据库MariaDB提取数据，然后通过其自带的模版引擎渲染出Html的主体内容框架。为了美化页面和用图表对数据进行展示，前端还使用了bootstarp与Echarts两个库。

基本的技术架构如下所示：
The web client <-> Nginx <-> the socket <-> uWSGI <-> Django

### To-do list
* make the page more beautiful
* try redis
* try ajax
* use vue to spilt frontend and backend.
* add more polls type.
* check same ip.
* use spider to collect polls from other site.
* try docker

