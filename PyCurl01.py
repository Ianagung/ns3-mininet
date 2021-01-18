#!/usr/bin/env python
# coding: utf-8

# In[12]:


#!/usr/bin/python
# coding: UTF-8
import pycurl
import multitimer
import pandas as pd

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

df1 = pd.DataFrame({ "resp_time":[1.5,2,0.5]})
# Print df1 
print(df1, "\n")
# saving the dataframe
addr = 'http://pycurl.io/'    
filename = 'Curltes01.csv'
df1.to_csv(filename)
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, addr)
c.setopt(c.WRITEDATA, buffer)

def job():
    global filename
    global df1
    c.perform()

    #http_code = c.getinfo(pycurl.HTTP_CODE)
    #http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
    #http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
    #http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
    #http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    #http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)

    # HTTP response code, e.g. 200.
    print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
    # Elapsed time for the transfer.
    #print('Transfer Time: %f' % c.getinfo(c.CONNECT_TIME))
    # Elapsed time for the transfer.
    total_time = c.getinfo(c.TOTAL_TIME)
    print('Total Time: %f' % total_time)
    df2 = pd.DataFrame({"resp_time":[float(total_time)]})
    df1=df1.append(df2, ignore_index = True)
    #print(df1, "\n")
    # saving the dataframe 
    df1.to_csv(filename ,sep=';')

# This timer will run job() five times, one second apart
timer = multitimer.MultiTimer(interval=2, function=job, count=10)
# Also, this timer would run indefinitely...
timer.start()
# getinfo must be called before close.
#c.close()


# In[ ]:




