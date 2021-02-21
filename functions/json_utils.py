import json

def json_write(body, save_file_path):
    '''
    Jsonファイルに保存する
    Args:
        body (Any): Jsonの内容
        save_dir (str): 保存するファイルパス
    '''
    with open(save_file_path, mode='w') as contents:
        json.dump(body, contents, indent=4, ensure_ascii=False)


def json_read(save_file_path: str):
    '''
    Jsonファイルを読み込む
    Args:
        save_file_path (str): 保存するファイルパス
    Returns:
        Any: Jsonの内容
    '''
    with open(save_file_path, mode='r') as contents:
        body = json.load(contents)

    return body
