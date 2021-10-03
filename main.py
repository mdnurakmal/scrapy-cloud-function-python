from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from flask import escape
import subprocess
import os
def hello_http(request):


    # process = CrawlerProcess()
    # process.crawl(AfajofSpider)
    # process.start()
    e = 'touch temp'
    subprocess.run(e, stdout=subprocess.PIPE, shell=True)

    c = 'gsutil cp $HOME/scrapy-cloud-function-python/temp gs://afajof_calendar'

    #print(os.environ['HOME'])


    subprocess.run(c, stdout=subprocess.PIPE, shell=True)

    return 'Hello {}!'.format(escape("Word"))


if __name__ == "__main__":
    hello_http(None)