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


def delete_all_stack_mongodb():
    for stack in db_stacks.find():
        db_stacks.delete_one(stack)

def update_mongodb(daily_json):
    save_dir = os.path.join(os.path.dirname('covidAPI'), 'saves')
    save_file_path = os.path.join(save_dir, 'latest.json')
    if not os.path.isfile(save_file_path):
        logger.error('no file is found')
    else:
        if db_stacks.find_one({'date': daily_json['date']}):
            pass
        else:
            db_stacks.insert_one(daily_json).inserted_id

def show_content():
    for stack in db_stacks.find():
        print(stack)

# show_content()
# delete_all_stack_mongodb()
# show_content()