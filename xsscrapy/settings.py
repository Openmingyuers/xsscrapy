#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# Uncomment below in order to disallow redirects
#REDIRECT_ENABLED = False

# Uncomment this to liite the spider's output
#LOG_LEVEL = 'INFO'

BOT_NAME = 'xsscrapy'

SPIDER_MODULES = ['xsscrapy.spiders']
NEWSPIDER_MODULE = 'xsscrapy.spiders'

# 100 (first): Make sure there's no duplicate requests that have some value changed
# 200 (second): Make sure there's a random working User-Agent header set if that value's not injected with the test string
DOWNLOADER_MIDDLEWARES = {'xsscrapy.middlewares.InjectedDupeFilter': 100,
                          'xsscrapy.middlewares.RandomUserAgentMiddleware': 200}

COOKIES_ENABLED = True
#COOKIES_DEBUG = True

# Prevent duplicate link crawling
# Bloom filters are way more memory efficient than just a hash lookup
DUPEFILTER_CLASS = 'xsscrapy.bloomfilters.BloomURLDupeFilter'
#DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'

ITEM_PIPELINES = {'xsscrapy.pipelines.XSSCharFinder':100}

#FEED_FORMAT = 'csv'
#FEED_URI = 'vulnerable-urls.txt'

CONCURRENT_REQUESTS = 12

