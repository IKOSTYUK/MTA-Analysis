# Scraping MTA Data and Saving as .csv Files

from datetime import datetime, timedelta
import pandas as pd
import time


def get_data():

    end_date = datetime.strptime(time.strftime("%y%m%d"), '%y%m%d')
    begin_date = datetime.strptime('170916', '%y%m%d')
    base_link = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_'

    while(begin_date < end_date):

        link = '{0}{1}.txt'.format(base_link, begin_date.strftime("%y%m%d"))
        print ("Retrieving data from...")
        df = pd.read_csv(link)
        df.to_csv('{0}.csv'.format(begin_date.strftime("%y%m%d")), index=False)
        
        begin_date = begin_date + timedelta(days=7)      

