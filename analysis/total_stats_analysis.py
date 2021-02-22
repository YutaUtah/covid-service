import datetime
import logging
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def convert_total_stats_to_df(db_stacks):
    data = db_stacks.find()[0]
    data = data['stats']

    temp_data_list = []
    df = pd.DataFrame(columns=['date', 'pcr_cases', 'positive', 'severe', 'death', 'deaths_rate'])

    for i in range(len(data)):
        s_datetime = datetime.datetime.strptime(str(data[i]['date']), '%Y%m%d')
        data[i]['date'] = s_datetime
        temp_data_list.append(data[i])

    df = df.append(temp_data_list, ignore_index=True)
    logger.info('df is created')
    return df

