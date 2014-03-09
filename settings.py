# Scrapy settings for kerengga project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'kerengga'

SPIDER_MODULES = ['kerengga.spiders']
NEWSPIDER_MODULE = 'kerengga.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kerengga (+http://www.yourdomain.com)'

ITEM_PIPELINES = ['kerengga.pipelines.MysqlStorePipeline']
