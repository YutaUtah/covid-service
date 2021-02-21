import logging
import sys
import os

from functions.get_data_prefectures import get_simple_json
from functions.json_utils import json_read, json_write

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.ERROR, format=formatter)


from functions.get_data_prefectures import get_requests

if __name__ == '__main__':

    try:
        body = get_requests('https://covid19-japan-web-api.now.sh/api/v1/prefectures')

    except Exception as e:
        sys.exit(logging.error('%s', 'Failed to call API'))

    overall_stats = {}
    for i in range(len(body)):
        get_simple_json(body[i], overall_stats)

    print(overall_stats)

    # directory = os.path.dirname(__file__)
    # print(directory)
    # save_dir = os.path.join(directory, 'saves')
    # print(save_dir)
    # if not os.path.isdir(save_dir):
    #     os.makedirs(save_dir)
    #
    # save_file_path = os.path.join(save_dir, 'save.json')
    #
    #
    # if os.path.isfile(save_file_path):
    #     old_body = json_read(save_file_path)
    #     # old_day = old_body['date']
    #     # difference = body['positive'] - old_body['positive']
    # else:
    #     old_day = None
    #     difference = 0

    # if day != old_day:
    #     if os.path.isfile(daily_infections):
    #         daily = json_read(daily_infections)
    #     else:
    #         daily = []
    #
    #     day_obj = datetime.datetime.strptime(str(day), r'%Y%m%d')
    #     daily.append({
    #         'date': day,
    #         'positive': difference
    #     })
    #
    #


