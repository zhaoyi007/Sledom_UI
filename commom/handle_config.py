import os
from configparser import ConfigParser

from commom.handle_path import CONF_DIR


class HandleConfig(ConfigParser):

    def __init__(self, filename):
        super().__init__()
        self.read(filename, encoding="utf-8")


conf = HandleConfig(os.path.join(CONF_DIR, "config.ini"))

URL = conf.get("env", "url")
