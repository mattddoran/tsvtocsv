from interfaces import Visualization, Analysis, Query
import mysql.connector

#All the questions inherit from this interface
class Question():

    def __init__(self, queryFile):
        self.queryFile = queryFile

    #should call process to get data and generate the visualization
    def visualize(self):
        raise NotImplementedError("Not implemented")

    #should return a list of lists
    def query(self):
        raise NotImplementedError("Not implemented")

    #should return data particularly organized to question
    def process(self):
        raise NotImplementedError("Not implemented")