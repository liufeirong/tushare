# -*- coding:utf-8 -*- 
'''
Created on 2017/9/24
@author: Jimmy Liu
'''
import unittest
import tushare.stock.trading as fd
from tushare.util.conns import get_apis, close_apis

class Test(unittest.TestCase):

    def set_data(self):
        self.code = '600848'
        self.start = ''
        self.end = ''
        
    def test_bar_data(self):
        self.set_data()
        conn = get_apis()
        print(fd.bar(self.code, conn, self.start, self.end,freq='60min'))
        close_apis(conn)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
