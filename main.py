
from conferenceCalendar.run_scrapy import script

import shlex 
import subprocess

from multiprocessing import Process, Queue , Manager


def hello_http(request):
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


    print(return_dict["print1"])

    return 'https://storage.cloud.google.com/afajof_calendar/' + return_dict["filename"]



if __name__ == "__main__":
    hello_http(None)

