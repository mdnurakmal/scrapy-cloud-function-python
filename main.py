from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from conferenceCalendar.upload import upload
from datetime import datetime
import shlex 
import subprocess
import os

from multiprocessing import Process, Queue , Manager


def hello_http(request):
    def script(queue,return_dict):
        try:
            settings = get_project_settings()
            settings.setdict({
            'LOG_LEVEL': 'ERROR',
            'LOG_ENABLED': True,
            })
            process = CrawlerProcess(settings)
            process.crawl(AfajofSpider)
            process.start()

         
            queue.put(None)
        except Exception as e:
            queue.put(e)

    queue = Queue()
    # wrap the spider in a child process
    manager = Manager()
    return_dict = manager.dict()
    main_process = Process(target=script, args=(queue,return_dict))
    main_process.start() # start the process
    main_process.join() # block until the spider finishes
    result = queue.get() # check the process did not return an error

    if result is not None:
        raise result

       
    now = datetime.now().strftime("%m%d%Y_%H%M%S")
    home = os.environ['HOME']

    #subprocess.call(["mv", home+"/scrapy-cloud-function-python/afajof_calendar.xlsx",home+"/scrapy-cloud-function-python/"+"temp-"+now+".xlsx"])

    return_dict["filename"]="temp-"+now+".xlsx"
    #os.system("gsutil cp $HOME/scrapy-cloud-function-python/{filename} gs://afajof_calendar/{filename}".format(filename="temp-"+now+".xlsx"))
    upload(home+"/scrapy-cloud-function-python/afajof_calendar.xlsx")

    return 'https://storage.cloud.google.com/afajof_calendar/' + return_dict["filename"]



if __name__ == "__main__":
    hello_http(None)

