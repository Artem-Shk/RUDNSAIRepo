import time
from .terminalcolors import bcolors

def speedtest(function):
    def speedometr(*args, **kwargs):
        
        t1 = time.time()
        res = function(*args, **kwargs)
        t2 = time.time()
        
        print(
            f"{bcolors.OKBLUE}{function.__name__}(){bcolors.ENDC} done!\tresult speed: {bcolors.BOLD}{bcolors.OKGREEN}{t2-t1}{bcolors.ENDC}"
        )
        return res
    return speedometr
    
