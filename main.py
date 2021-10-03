from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from flask import escape
from datetime import datetime
import shlex 
import subprocess
import os
def hello_http(request):


    process = CrawlerProcess()
    process.crawl(AfajofSpider)
    process.start()

    now = datetime.now().strftime("%m%d%Y_%H%M%S")

    subprocess.call(["mv", os.environ['HOME']+"/scrapy-cloud-function-python/afajof_calendar.xlsx",os.environ['HOME']+"/scrapy-cloud-function-python/"+"temp-"+now+".xlsx"])


    os.system("gsutil cp $HOME/scrapy-cloud-function-python/{0} gs://afajof_calendar".format("temp-"+now))

    return 'Hello {}!'.format(escape("Word"))


if __name__ == "__main__":
    hello_http(None)