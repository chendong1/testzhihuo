import os,sys

BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__) ) )

sys.path.append(BASE_DIR)
from core.test_log import log_run
from core.test_discover import discover_run


if __name__=='__main__':

    discover_run()

    log_run()


