from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error
import numpy as np

# Based on previous ratings of a TV series, can we accurately predict what the series
# finale rating will be?

class Q1(Question):

    def query(self):
        if os.path.isfile(self.queryFile):
            print 'already ran query'
        else:
            print 'need to run query'
            query =(
            "select mydb2.episode.idParent, mydb2.episode.season, mydb2.episode.number, mydb2.rating.averageRating "
            "from mydb2.episode cross join mydb2.title cross join mydb2.rating "
            "where mydb2.episode.Title_idTitle = mydb2.title.idTitle "
            "and mydb2.rating.Title_idTitle = mydb2.title.idTitle;"
            )
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query)

            out = open(self.queryFile, "w")
            for (idParent, season, episode, rating) in cursor:
                # convert entire line to csv
                out.write("{},{},{},{}\n".format(idParent, season, episode, rating))

            out.close()

    def process(self): # process csv from query and return data ready to be visualized
        shows = collections.defaultdict(list)
        with open(self.queryFile, "r") as f: #open csv populated from query
            for line in f.readlines(): #line by line
                data = line.split(",")
                if data[1] != "None": #ignore shows that don't include episode or season number
                    shows[data[0]].append((data[1],data[2],data[3].rstrip()))
            f.close()
        avgAndFinale = collections.defaultdict(list)
        for show in shows.keys(): #iterate over each tconst
            total = 0
            eps = 0
            finale = None
            for episode in shows[show]: #iterate over each episode in a show
                finale = episode
                total += float(episode[2]) #running total of episode ratings
                eps += 1.0
            if round(total/eps, 2) != float(finale[2]): #filter out single episode tv series
                avgAndFinale[show] = (round(total/eps, 2), float(finale[2])) #record tuple(average ep rating, finale rating)
        return avgAndFinale

    def visualize(self): # Create scatterplot of all of the shows and display pearson coefficient line
        avgAndFinale = self.process()
        x = []
        y = []
        for show in avgAndFinale.keys(): #populate lists for scatterplot
            x.append(avgAndFinale[show][0]) 
            y.append(avgAndFinale[show][1])

        plt.scatter(x,y, marker=".") # scatterplot
        plt.xlabel("Average Episode Rating")
        plt.ylabel("Series Finale Rating")
        p = pearsonr(x,y) # Pearson' coefficient
        print p[0]
        xT = []
        yT = []
        for i in x:
            xT.append([i])
        for i in y:
            yT.append([i])  
        regr = linear_model.LinearRegression()
        regr.fit(xT,yT) #fit linear regression line
        y_pred = regr.predict(xT) #predict y values to draw regression line
        print "linear regression coefficients: " + str(regr.coef_)
        print "linear regression y-intercept: " + str(regr.intercept_)
        print "mean squared error: " + str(mean_squared_error(y,y_pred)) #mean squared error

        
        plt.plot(x, y_pred, color="red") # Pearson's coefficient line
        plt.show()








