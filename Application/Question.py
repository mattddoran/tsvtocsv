from interfaces import Visualization, Analysis, Query

class Question(Visualization,Analysis,Query):

    def __init__(self, title):
        self.id = title

    def doSome(self):
        print "sup"