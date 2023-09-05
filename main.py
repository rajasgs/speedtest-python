
'''
Created on 

@author: Raja CSP Raman

source:
    https://github.com/RohanDas28/Speedtest-Python

    https://pypi.org/project/speedtest-cli/

    https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d

    https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python

    https://stackoverflow.com/questions/3961581/in-python-how-to-display-current-time-in-readable-format

    https://stackoverflow.com/questions/24678308/how-to-find-location-with-ip-address-in-python

    https://stackoverflow.com/questions/4528099/convert-json-string-to-dict-using-python

    https://github.com/sivel/speedtest-cli
'''


import speedtest #pip install speedtest-cli
import time
from datetime import datetime
import re
import json
# from urllib2 import urlopen
from urllib.request import urlopen
from json import load
import json

s = speedtest.Speedtest()

def get_ip_info( addr = ''):
    
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'

    res = urlopen(url)
    #response from url(if res==None then check connection)

    # print(res)
    
    data = load(res)
    #will load the json response into data
    # print(data)
    
    # for attr in data.keys():
    #     #will print the data line by line
    #     print(attr,' '*13+'\t->\t',data[attr])

    # print[(load(res))]

    # cdata = json.loads(data)
    # print(cdata['org'])

    # print(type(data))
    # print(data['org'])

    return data['org']

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

def get_date_time():

    c_date              = datetime.today().strftime('%Y-%m-%d')
    now                 = datetime.now()
    c_time              = now.strftime("%H:%M")

    return c_date, c_time

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
    ping = s.results.ping #Ping the server
    time.sleep(1)

    # print("Downloading...")
    download = s.download() #Download test
    time.sleep(1)

    # print("Uploading...")
    upload = s.upload() #Upload test
    time.sleep(1)

    speedtest_result    = ""
    isp_provider        = get_ip_info()
    c_date, c_time      = get_date_time()
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

    c_date, c_time      = get_date_time()
    # print(c_date)
    # print(c_time)

    # c_ip = get_ip_details()
    # print(c_ip)

    # ip_info()

if __name__ == '__main__':
    startpy()