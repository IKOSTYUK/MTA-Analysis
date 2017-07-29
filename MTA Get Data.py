def get_data():

    end_date = datetime.strptime(time.strftime("%y%m%d"), '%y%m%d')
    begin_date = datetime.strptime('170506', '%y%m%d')
    base_link = 'http://web.mta.info/developers/data/nyct/turnstile/turnstile_'

    while(begin_date < end_date):

        link = '{0}{1}.txt'.format(base_link, begin_date.strftime("%y%m%d"))
        print ("Retrieving data from...")
        try:
            new_df = pd.read_csv(link)
            df = df.append(new_df, ignore_index=True)
        except:
            df = pd.read_csv(link)
        begin_date = begin_date + timedelta(days=7)

    return df
