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

        process = CrawlerProcess(settings)
        process.crawl(AfajofSpider)
        process.start()

        
        
        now = datetime.now().strftime("%m%d%Y_%H%M%S")
        home = os.environ['HOME']
        cwd = os.getcwd()
        #arr = os.listdir('/tmp/usercode/scrapy-cloud-function-python/conferenceCalendar')
        return_dict["print"]=cwd
        #subprocess.call(["mv", "/tmp/afajof_calendar.xlsx","/tmp/temp-"+now+".xlsx"])

        return_dict["filename"]="temp-"+now+".xlsx"
        #return_dict["temp"]=home+"/scrapy-cloud-function-python/afajof_calendar.xlsx"
        
        #os.system("gsutil cp $HOME/scrapy-cloud-function-python/{filename} gs://afajof_calendar/{filename}".format(filename="temp-"+now+".xlsx"))
        
        #upload("/tmp/temp-"+now+".xlsx"],"temp-"+now+".xlsx")

        #arr = os.listdir(os.path.abspath('.'))
        return_dict["print1"]=os.path.abspath(__file__)


        queue.put(None)
    except Exception as e:
        queue.put(e)

