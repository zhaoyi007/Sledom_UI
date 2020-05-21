import time

from commom.handle_path import REPORT_DIR


class Utility:
    def __init__(self):
        pass

    @classmethod
    def write_result(cls, case_name, params):
        test_time = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(REPORT_DIR+'/result.csv', mode='a+', encoding='utf-8') as file:
            file.write("%s,%s,%s,%s\n" % (test_time, case_name, str(params), "失败"))

    @classmethod
    def new_csv(cls):
        with open(REPORT_DIR+'/result.csv', mode='w+', encoding='utf-8') as file:
            file.truncate()
