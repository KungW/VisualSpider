# VisualSpider：django建设爬虫可视化站点

- 工作原理：

slave机器不断产生log，每隔十分钟采一次点，每隔一小时上传一次，

web后端机器由脚本控制每小时索取一次log，图像随之动态更新。

后端框架采用django，前端绘图库：jquery.flot
 
- 数据log如下：

![](http://visualspider-visualspider.stor.sinaapp.com/log.png)

- 呈现效果如图：

![](http://visualspider-visualspider.stor.sinaapp.com/20160809055255.png)

- 站点部署于

http://1.visualspider.applinzi.com/scholar/show/

- 总结
 
实现了基本的可视化处理，虽然不落在控制台程序员的喜好范围内，

但对外展示工作时，需要一种更友好的表达。本项目仅作此理解。2016-8-9
