from datetime import datetime, timedelta
import pandas as pd
import time
import re
import urllib
import urllib.request as request
from bs4 import BeautifulSoup
import csv


def get_data():

    end_date = datetime.strptime(time.strftime("%y%m%d"), '%y%m%d')
    begin_date = datetime.strptime('170701', '%y%m%d')
    base_link = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_'

    while(begin_date < end_date):

        link = '{0}{1}.txt'.format(base_link, begin_date.strftime("%y%m%d"))
        print ("Retrieving data from {}...".format(link))
        response = urllib.request.urlopen(link)
        html = response.read()
        with open('{0}.csv'.format(begin_date.strftime("%y%m%d")), 'wb') as f:
                f.write(html) 
        begin_date = begin_date + timedelta(days=7)
