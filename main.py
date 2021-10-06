from conferenceCalendar.spiders.afajofspiders import AfajofSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from conferenceCalendar.upload import upload
from datetime import datetime
import shlex 
import subprocess
import os
from os import path
from multiprocessing import Process, Queue , Manager


def hello_http(request):
    def script(queue,return_dict):
        try:

            settings = get_project_settings()

            process = CrawlerProcess(settings)
            process.crawl(AfajofSpider)
            process.start()

           
         
            now = datetime.now().strftime("%m%d%Y_%H%M%S")
            home = os.environ['HOME']
            cwd = os.getcwd()
            arr = os.listdir('.')
            return_dict["print"]=arr
            #subprocess.call(["mv", "/tmp/afajof_calendar.xlsx","/tmp/temp-"+now+".xlsx"])

            return_dict["filename"]="temp-"+now+".xlsx"
            #return_dict["temp"]=home+"/scrapy-cloud-function-python/afajof_calendar.xlsx"
         
            #os.system("gsutil cp $HOME/scrapy-cloud-function-python/{filename} gs://afajof_calendar/{filename}".format(filename="temp-"+now+".xlsx"))
            
            #upload("/tmp/temp-"+now+".xlsx"],"temp-"+now+".xlsx")

            arr = os.listdir(os.path.abspath('/conferenceCalendar'))
            return_dict["print1"]=arr


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

    print(return_dict["print"])
    print(return_dict["print1"])

    return 'https://storage.cloud.google.com/afajof_calendar/' + return_dict["filename"]



if __name__ == "__main__":
    hello_http(None)

