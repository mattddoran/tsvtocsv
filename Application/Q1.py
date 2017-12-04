from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import numpy as np

class Q1(Question):
    @staticmethod
    def query():
        fname = "query1.csv"
        if os.path.isfile(fname):
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

            out = open(fname, "w")
            for (idParent, season, episode, rating) in cursor:
                # convert entire line to csv
                out.write("{},{},{},{}\n".format(idParent, season, episode, rating))

            out.close()

    @staticmethod
    def process(csv): # process csv from query and return data ready to be visualized
        shows = collections.defaultdict(list)
        with open(csv, "r") as f: #open csv populated from query
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

    @staticmethod
    def visualize(csv): # Create scatterplot of all of the shows and display pearson coefficient line
        avgAndFinale = Q1.process(csv)
        x = []
        y = []
        for show in avgAndFinale.keys(): #populate lists for scatterplot
            x.append(avgAndFinale[show][0]) 
            y.append(avgAndFinale[show][1])

        plt.scatter(x,y, marker=".") # scatterplot
        plt.xlabel("Average Episode Rating")
        plt.ylabel("Season Finale Rating")
        p = pearsonr(x,y) # Pearson' coefficient
        line = np.arange(10)

        plt.plot(line * p[0]+1, color="red") # Pearson's coefficient line
        plt.show()








