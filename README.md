## A Questionnaire Website APP by Django + Vue

部署地址:

新: http://goqing123.com.cn:8000 Django + Vue，前后端分离, 单页面应用。
旧: http://goqing123.com.cn:8000/polls 使用Django自带的模版引擎渲染得到页面。

本项目是一个在线问卷调查的网页APP。用户访问页面时，Nginx将直接处理前端传来的请求，其中静态文件请求将被转发到七牛云的CDN上，而动态请求则通过Uwsgi传递给Django进行处理。接收到动态请求后，Django调用后台数据库MariaDB或缓存数据库Redis提取数据，然后通过Django rest framework提供API接口把数据通过json传回前端，前端再通过各种JavaScript库渲染得到最终呈现给用户的页面。

基本的技术架构如下所示：

The web client <-> Nginx <-> the socket <-> uWSGI <-> Django <-> Redis <-> MariaDB

前端主要运用了Vue框架，通过Vue-cli和Webpack构建编译得到最终的html,css,javascipt文件。为了美化页面和用图表对数据进行展示，前端还使用了bootstarp，element-ui，Echarts等库。


### To-do list
* add more polls type.
* check same ip.
* use spider to collect polls from other site.
* try docker

