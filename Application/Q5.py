from Question import Question
import mysql.connector
import os.path


class Q5(Question):
    @staticmethod
    def query():
        fname = "test.py"
        if os.path.isfile(fname):
            print 'exists'
        else:
            print 'not exsist'