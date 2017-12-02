from interfaces import Visualization, Analysis, Query
import mysql.connector

#Inherits these three classes as interfaces
class Question(Visualization,Analysis,Query):

    def __init__(self, title, data):
        self.id = title
        self.data = data

    def displayImage(self):
        print ("Matt is so cool")

    def displayAnalysis(self):
        print ("Movies are hip")

    def userFilter(self):
        print ("Treat your self")

    @staticmethod
    def runQuery(query):
        cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
        cursor = cnx.cursor(buffered=True)
        cursor.execute(query)
        data = cursor
        print 0
        for (genre, year, count) in cursor:
            # print isTitle, a
             print("{},{},{}".format(genre,year,count))
        print 1
        for (genre, year, count) in data:
            # print isTitle, a
             print("{},{},{}".format(genre,year,count))
        cursor.close()
        cnx.close()
        print 2
        for (genre, year, count) in data:
            # print isTitle, a
             print("{},{},{}".format(genre,year,count))
        return cursor
