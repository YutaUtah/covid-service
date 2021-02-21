import json

def json_write(body, save_file_path):
    '''
    save json file
    Args:
        body: Json content
        save_dir: directory to save
    '''
    with open(save_file_path, mode='w') as contents:
        json.dump(body, contents, indent=4, ensure_ascii=False)


def json_read(save_file_path: str):
    '''
    read json file
    Args:
        save_file_path: directory to save
    Returns:
        json content
    '''
    with open(save_file_path, mode='r') as contents:
        body = json.load(contents)

    return body
