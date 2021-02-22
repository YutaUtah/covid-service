import logging
import sys
import os

from utils.clean_json import get_requests, get_json_by_prefecture, get_json_total_stats
from utils.json_utils import json_write
from DButils.mongo import update_mongodb, show_content, delete_all_stack_mongodb
from constants import Const

formatter = '%(levelname)s : %(asctime)s : %(message)s'
logging.basicConfig(level=logging.INFO, format=formatter)


if __name__ == '__main__':
    try:
        by_prefecture_request = get_requests(Const.BY_PREFECTURE_API)
        total_stats_request = get_requests(Const.TOTAL_STATS_API)
    except Exception as e:
        sys.exit(logging.error('%s', 'failed to call API'))


    directory = os.path.dirname(__file__)

    save_dir = os.path.join(directory, 'saves')

    if not os.path.isdir(save_dir):
        logging.info('%s', 'creating folder at {}'.format(save_dir))
        os.makedirs(save_dir)

    save_file_path_by_prefecture = os.path.join(save_dir, 'latest_by_prefecture.json')
    save_file_path_total_stats = os.path.join(save_dir, 'latest_total_stats.json')

    daily_stats_by_prefecture = get_json_by_prefecture(by_prefecture_request)
    total_stats = get_json_total_stats(total_stats_request)

    json_write(daily_stats_by_prefecture, save_file_path_by_prefecture)
    json_write(total_stats, save_file_path_total_stats)

    update_mongodb(daily_stats_by_prefecture)
    update_mongodb(total_stats)

    # delete_all_stack_mongodb()
    # show_content(total_stats)






