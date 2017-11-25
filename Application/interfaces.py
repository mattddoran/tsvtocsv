class Visualization():
    #should return an object
    def createImage(self):
        raise NotImplementedError("Not implemented")

class Analysis():
    #should return an object
    def analyzeData(self):
        raise NotImplementedError("Not implemented")

class Query():
    #should return a data type
    def query(self):
        raise NotImplementedError("Not implemented")

    #should return a list
    def process(self):
        raise NotImplementedError("Not implemented")