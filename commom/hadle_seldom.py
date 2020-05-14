from seldom import json_to_list

from commom.handle_path import DATA_DIR, CASE_DIR, CONF_DIR, DIRVE_DIR


def json_to_lsit(file, key):
    return json_to_list(file=DATA_DIR + "//" + file, key=key)




