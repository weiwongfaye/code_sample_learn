"""
Author: Jack Wang
Email: weiwongfaye@gmail.com
"""

import logging
import datetime as dt


class MyFormatter(logging.Formatter):
    """Overwrite the millsecond format to start with . instead of ,"""
    converter=dt.datetime.fromtimestamp
    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s.%03d" % (t, record.msecs)
        return s


class LoggerAdapter(object):
    """Return a python logging object"""
    def __init__(self, log_level,log_path=None):
        self.log_level = log_level
        self.log_path = log_path
        'By default user streamHandler, otherwise use file instead'
        if self.log_path is not None:
            hdlr = logging.FileHandler(self.log_path,'w+')
        else:
            hdlr = logging.StreamHandler()
        self.hdlr = hdlr

    def getLogger(self,logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.log_level)
        formatter = MyFormatter("%(asctime)s %(levelname)s %(message)s")
        self.hdlr.setFormatter(formatter)
        logger.addHandler(self.hdlr)
        return logger

if __name__ == '__main__':


    logAdapter = LoggerAdapter('DEBUG')
    mylogger = logAdapter.getLogger('test_console')
    mylogger.debug("test debug message in console")


    logAdapter = LoggerAdapter('DEBUG','HAAHA.LOG')
    mylogger = logAdapter.getLogger('test_file')
    mylogger.debug("test debug message in file")
