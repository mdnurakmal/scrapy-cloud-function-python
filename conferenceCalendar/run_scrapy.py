from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from datetime import datetime
from spiders.afajofspiders import AfajofSpider
from upload import upload
import os
from os import path
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

