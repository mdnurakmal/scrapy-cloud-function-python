from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from datetime import datetime
from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from conferenceCalendar.upload import upload
import os
from os import path
def script(queue,return_dict):
    try:

        settings_file_path = 'conferenceCalendar.settings' # The path seen from root, ie. from main.py
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        settings = get_project_settings()

        now = datetime.now().strftime("%m%d%Y_%H%M%S")

        return_dict["filename"]="temp-"+now+".xlsx"

        process = CrawlerProcess(settings)
        process.crawl(AfajofSpider)
        process.start()

        upload("/tmp/afajof_calendar.xlsx"],"temp-"+now+".xlsx")

        arr = os.listdir('/tmp')
        return_dict["print1"]=arr


        queue.put(None)
    except Exception as e:
        queue.put(e)

