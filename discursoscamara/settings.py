# Scrapy settings for discursoscamara project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'discursoscamara'

SPIDER_MODULES = ['discursoscamara.spiders']
NEWSPIDER_MODULE = 'discursoscamara.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'discursoscamara (+http://www.yourdomain.com)'
HTTPCACHE_ENABLED=1
LOG_LEVEL= 'INFO'
