import os

# 获取项目所在的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 用例模块所在的目录路径
CASE_DIR = os.path.join(BASE_DIR, "test_dir")

# 用例数据所在的目录路径
DATA_DIR = os.path.join(BASE_DIR, "data")

# 配置文件所在的目录路径
CONF_DIR = os.path.join(BASE_DIR, "config")

# config.ini path
config_path = CONF_DIR + "//" + "config.ini"

# 测试报告所在的目录路径
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# drive path
DIRVE_DIR = os.path.join(BASE_DIR, "lib")

# chromedriver.exe path
chromedriver = DIRVE_DIR + "//" + "chromedriver.exe"

# geckodriver.exe path

geckodriver = DIRVE_DIR + "//" + "geckodriver.exe"

