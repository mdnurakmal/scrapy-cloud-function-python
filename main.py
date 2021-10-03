from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from flask import escape
from datetime import datetime
import shlex 
import subprocess
import os

from multiprocessing import Process, Queue
from ... import MySpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def hello_http(event, context):
    def script(queue):
        try:
            settings = get_project_settings()
            settings.setdict({
            'LOG_LEVEL': 'ERROR',
            'LOG_ENABLED': True,
            })
            process = CrawlerProcess(settings)
            process.crawl(MySpider)
            process.start()

            
            now = datetime.now().strftime("%m%d%Y_%H%M%S")
            home = os.environ['HOME']

            subprocess.call(["mv", home+"/scrapy-cloud-function-python/afajof_calendar.xlsx",home+"/scrapy-cloud-function-python/"+"temp-"+now+".xlsx"])


            os.system("gsutil cp $HOME/scrapy-cloud-function-python/{0} gs://afajof_calendar".format("temp-"+now+".xlsx"))

            queue.put(None)
        except Exception as e:
            queue.put(e)

    queue = Queue()
    # wrap the spider in a child process

    main_process = Process(target=script, args=(queue,))
    main_process.start() # start the process
    main_process.join() # block until the spider finishes
    result = queue.get() # check the process did not return an error

    if result is not None:
        raise result

    return 'ok'
