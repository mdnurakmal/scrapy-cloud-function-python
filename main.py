from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from flask import escape
from datetime import datetime

import subprocess
import os
def hello_http(request):


    # process = CrawlerProcess()
    # process.crawl(AfajofSpider)
    # process.start()

    now = datetime.now()
    e = 'touch ' + shlex.quote(now)
    subprocess.run(e, stdout=subprocess.PIPE, shell=True)
    c = 'gsutil cp $HOME/scrapy-cloud-function-python/afajof_calendar.xlsx gs://afajof_calendar'

    subprocess.run(c, stdout=subprocess.PIPE, shell=True)

    return 'Hello {}!'.format(escape("Word"))


if __name__ == "__main__":
    hello_http(None)