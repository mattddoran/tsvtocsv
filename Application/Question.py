from interfaces import Visualization, Analysis, Query

#Inherits these three classes as interfaces
class Question(Visualization,Analysis,Query):

    def __init__(self, title, data):
        self.id = title
        self.data = data

    def displayImage(self):
        print "Matt is so cool"

    def displayAnalysis(self):
        print "Movies are hip"
        
    def userFilter(self):
        print "Treat your self"