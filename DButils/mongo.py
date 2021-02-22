from pymongo import MongoClient
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']
db_stacks = db.stacks


def update_one_stack_mongodb(stack):
    db_stacks.insert_one(stack)


def delete_one_stack_mongodb(db_stacks):
    for stack in db_stacks.find():
        print(stack['_id'])
        print(stack['stats'][-1]['date'])



def delete_all_stack_mongodb(db_stacks):
    for stack in db_stacks.find():
        db_stacks.delete_one(stack)
        print(stack)


def show_content(db_stacks):
    for stack in db_stacks.find():
        print(stack)

def db_instantiate(json_dir, db_name):
    save_dir = os.path.join(os.path.dirname('covidAPI'), 'saves')
    save_file_path = os.path.join(save_dir, json_dir)
    db = client[db_name]
    db_stacks = db.stacks

    return db_stacks, save_file_path


def update_mongodb(json):
    if len(json.keys()) == 2:
        db_stacks, save_file_path = db_instantiate('latest_by_prefecture.json', 'prefecture_database')
        if not os.path.isfile(save_file_path):
            logger.error('no file is found')
        else:
            if db_stacks.find_one({'date': json['date']}):
                logger.info('latest prefecture data already exists')
                pass
            else:
                db_stacks.insert_one(json).inserted_id
        print('prefecture_database: ')
        show_content(db_stacks)

    elif len(json.keys()) == 1:
        db_stacks, save_file_path = db_instantiate('latest_total_stats.json', 'total_stats_database')
        if not os.path.isfile(save_file_path):
            logger.error('no file is found')
        else:
            if db_stacks.find_one({}, {'date': json['stats'][-1]['date']}) is None:
                logger.info('latest total stats data already exists')
                pass
            else:
                db_stacks.delete_many({})
                db_stacks.insert_one(json).inserted_id

        print('total stats database: ')
        show_content(db_stacks)
    logging.info('database is updated')
    return db_stacks




# delete_all_stack_mongodb()
# show_content(db_stacks_by_prefecture)
# show_content(db_stacks_total_stats)
