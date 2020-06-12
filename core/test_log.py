import unittest
import config.conf_directory

def log_run():

    test_dir = config.conf_directory.test_dir

    log_dir = config.conf_directory.log_dir

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    # 写入测试日志
    with open(log_dir + '/Testlog.txt', 'a') as g:
        runner = unittest.TextTestRunner(stream=g,
                                        verbosity=2)
        runner.run(discover)
        g.close()