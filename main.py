import logging
import sys
import os

from utils.get_data_prefectures import get_simple_json
from utils.json_utils import json_read, json_write
from DButils.mongo import update_mongodb, show_content

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.ERROR, format=formatter)


from utils.get_data_prefectures import get_requests

if __name__ == '__main__':

    try:
        body = get_requests('https://covid19-japan-web-api.now.sh/api/v1/prefectures')

    except Exception as e:
        sys.exit(logging.error('%s', 'Failed to call API'))


    directory = os.path.dirname(__file__)

    save_dir = os.path.join(directory, 'saves')

    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    daily_infections = os.path.join(save_dir, 'daily.json')
    save_file_path = os.path.join(save_dir, 'latest.json')
    myDict = {}
    daily_stats = get_simple_json(body)

    if os.path.isfile(save_file_path):
        old_body = json_read(save_file_path)
        old_day = old_body['date']
        if daily_stats['date'] != old_day:
            pass
    # for loop 書かないと
    #     difference = body['positive'] - old_body['positive']
    else:
        pass
        # old_day = None
        # difference = 0

    json_write(daily_stats, save_file_path)
    update_mongodb(daily_stats)
    show_content()


