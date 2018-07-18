### A questionnaire website app by django

部署地址:
http://goqing123.com.cn:8000

本项目是一个在线问卷调查的网页APP。技术架构为：用户访问页面时，Nginx将处理前端的静态文件请求，而动态请求则通过uwsgi传递给django进行处理，然后django再调用后台数据库MariaDB的提取数据，然后通过其自带的模版引擎渲染除Html的主体内容框架。为了美化页面，使用了bootstarp的css库。另外使用Echarts这一js库把数据用精美的图表进行了展示。

### To-do list
* make the page more beautiful
* try redis
* add more polls type.
* check same ip.
* use spider to collect polls from other site.
* try docker
* use vue to spilt frontend and backend.
