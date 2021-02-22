import logging
import sys
import os

from utils.get_data_prefectures import get_requests, get_simple_json
from utils.json_utils import json_write
from DButils.mongo import update_mongodb, show_content

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.ERROR, format=formatter)


if __name__ == '__main__':

    try:
        body = get_requests('https://covid19-japan-web-api.now.sh/api/v1/prefectures')

    except Exception as e:
        sys.exit(logging.error('%s', 'failed to call API'))


    directory = os.path.dirname(__file__)

    save_dir = os.path.join(directory, 'saves')

    if not os.path.isdir(save_dir):
        logging.info('%s', 'creating folder at {}'.format(save_dir))
        os.makedirs(save_dir)

    save_file_path = os.path.join(save_dir, 'latest.json')
    daily_stats = get_simple_json(body)

    json_write(daily_stats, save_file_path)
    update_mongodb(daily_stats)
    show_content()


