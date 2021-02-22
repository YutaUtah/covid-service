import datetime
from pymongo import MongoClient
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)



client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']
db_stacks = db.stacks


def update_one_stack_mongodb(stack):
    db_stacks.insert_one(stack)


def delete_one_stack_mongodb(stack):
    db_stacks.delete_one(stack)


def delete_all_stack_mongodb(db_stacks):
    for stack in db_stacks.find():
        db_stacks.delete_one(stack)
        print(stack)


def show_content(db_stacks):
    for stack in db_stacks.find():
        print(stack)


def update_mongodb(json):
    if len(json.keys()) == 2:
        save_dir = os.path.join(os.path.dirname('covidAPI'), 'saves')
        save_file_path = os.path.join(save_dir, 'latest_by_prefecture.json')
        db = client['prefecture_database']
        db_stacks_by_prefecture = db.stacks
        if not os.path.isfile(save_file_path):
            logger.error('no file is found')
        else:
            if db_stacks_by_prefecture.find_one({'date': json['date']}):
                pass
            else:
                db_stacks_by_prefecture.insert_one(json).inserted_id
        print('prefecture_database: ')
        show_content(db_stacks_by_prefecture)

    elif len(json.keys()) == 1:
        save_dir = os.path.join(os.path.dirname('covidAPI'), 'saves')
        save_file_path = os.path.join(save_dir, 'latest_total_stats.json')
        db = client['total_stats_database']
        db_stacks_total_stats = db.stacks
        if not os.path.isfile(save_file_path):
            logger.error('no file is found')
        else:
            if db_stacks_total_stats.find_one({}, {'date': json['stats'][-1]['int_date']}):
                pass
            else:

                db_stacks_total_stats.insert_one(json).inserted_id
        print('total stats database: ')
        show_content(db_stacks_total_stats)




# delete_all_stack_mongodb()
# show_content(db_stacks_by_prefecture)
# show_content(db_stacks_total_stats)
