import logging
#logging.basicConfig(filename="kanna.log",level=logging.DEBUG,format="%(lineno)d:%(asctime)s:%(message)s:%(levelname)s:%(filename)s")
logging.basicConfig(filename="kanna.log",level=logging.DEBUG,format="%(lineno)d:%(asctime)s:%(filename)s:%(message)s:%(message)s")
"""
there are different types of levels
1)DEBUG
2)INFO
3)WARNING
4)ERROR
5)CRITICAL
"""
def addit(a,b):
    return a+b
obj=addit(40,50)
logging.debug(obj)
logging.critical(obj)
logging.warning(obj)
logging.info(obj)


