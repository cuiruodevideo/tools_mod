#!/usr/bin/env python
# encoding: utf-8

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename='killlog.txt',
                    filemode='a')


def log_mod(func):
    def log():
        try:
            func()
        except Exception, e:
            logging.error(str(e) +'  func_name  ' + func.__name__)
            print "check log"
            print e
    return log
