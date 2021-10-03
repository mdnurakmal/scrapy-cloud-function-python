from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from flask import escape

def hello_http(request):

    settings = get_project_settings()
    settings.setdict({
        'LOG_LEVEL': 'ERROR',
        'LOG_ENABLED': True,
    })
    process = CrawlerProcess(settings)
    process.crawl(AfajofSpider)
    process.start()

    return 'Hello {}!'.format(escape("Word"))


