import os
import tarfile
from six.moves import urllib
import pandas as pd


def fetch_data(data_info: dict):
    data_path = data_info['data_path']
    data_file_name = data_info['data_file_name']
    data_url = data_info['data_url']
    if not os.path.isdir(data_path):
        os.makedirs(data_path)
    tgz_path = os.path.join(data_path, data_file_name)
    urllib.request.urlretrieve(data_url, tgz_path)
    data_tgz = tarfile.open(tgz_path)
    data_tgz.extractall(path=data_path)
    data_tgz.close()
    print('data_fetch done...')


def load_data(data_path, filename):
    csv_path = os.path.join(data_path, filename)
    return pd.read_csv(csv_path)
