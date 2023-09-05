
'''
Created on 

@author: Raja CSP Raman

source:
    https://github.com/RohanDas28/Speedtest-Python

    https://pypi.org/project/speedtest-cli/

    https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d
'''


import speedtest #pip install speedtest-cli
import time

s = speedtest.Speedtest()

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print ('%r  %2.2f seconds' % \
                  (method.__name__, (te - ts)))
        return result
    return timed

@timeit
def get_custom_metrics():

    print("Loading Servers")
    s.get_servers() #Getting the servers

    # print("Connecting to the Best Server")
    bestServer = s.get_best_server() #Choosing the best server
    print(f"Connected to {bestServer['host']} located in {bestServer['country']} ")
    time.sleep(1)

    # print("Starting Speed Test...")
    time.sleep(2)

    # print("Pinging The Server...") 
    ping= s.results.ping #Ping the server
    time.sleep(1)

    # print("Downloading...")
    download = s.download() #Download test
    time.sleep(1)

    # print("Uploading...")
    upload = s.upload() #Upload test
    time.sleep(1)

    speedtest_result    = "<will_come>"
    isp_provider        = "Railtel"
    c_date              = "Sep 05, 2023"
    c_time              = "5 am IST"
    c_ip                = f"{download /1024/1024:.2f} Mbit/s, {upload /1024/1024:.2f} Mbit/s"

    c_msg = f"""{speedtest_result}
        {isp_provider}
        {c_date}, {c_time}
        {c_ip}
        """

    print(c_msg)


def get_speed_metrics():

    print("Loading Servers")
    s.get_servers() #Getting the servers

    print("Connecting to the Best Server")
    bestServer = s.get_best_server() #Choosing the best server
    print(f"Connected to {bestServer['host']} located in {bestServer['country']} ")
    time.sleep(1)

    print("Starting Speed Test...")
    time.sleep(2)

    print("Pinging The Server...") 
    ping= s.results.ping #Ping the server
    time.sleep(1)

    print("Downloading...")
    download = s.download() #Download test
    time.sleep(1)

    print("Uploading...")
    upload = s.upload() #Upload test
    time.sleep(1)

    def border_msg(msg): #For the border message
        row = len(msg)
        h = ''.join(['+'] + ['-' *row] + ['+'])
        result= h + '\n'"|"+msg+"|"'\n' + h
        print(result)

    print("*************RESULTS*************")
    border_msg(f"Ping: {ping:.2f} ms")
    border_msg(f"Download Speed: {download /1024/1024:.2f} Mbit/s")
    border_msg(f"Upload Speed: {upload /1024/1024:.2f} Mbit/s")
    print("************THANKYOU************")

def startpy():

    # print("Tact101")

    # get_speed_metrics()

    get_custom_metrics()
    

if __name__ == '__main__':
    startpy()