import os

import requests
from django.conf import settings


def download_file(url, filename):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'}
    r = requests.get(url, stream=True, verify=False, headers=headers)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)


def make_unique(original_list):
    unique_list = []
    [unique_list.append(obj) for obj in original_list if obj not in unique_list]
    return unique_list


def make_unique_by_key(original_list, key):
    unique_dict = {}
    for obj in original_list:
        if obj.get(key) not in unique_dict:
            unique_dict[obj.get(key)] = obj
    return list(unique_dict.values())


def make_sure_dirs_exist():
    for directory in (settings.TILDA_MEDIA_IMAGES, settings.TILDA_MEDIA_JS, settings.TILDA_MEDIA_CSS):
        if not directory:
            continue
        if not os.path.exists(directory):
            os.makedirs(directory)
