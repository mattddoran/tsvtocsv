from interfaces import Visualization, Analysis, Query
import mysql.connector

#Inherits these three classes as interfaces
class Question(Visualization,Analysis,Query):

    def __init__(self, queryFile):
        self.queryFile = queryFile
