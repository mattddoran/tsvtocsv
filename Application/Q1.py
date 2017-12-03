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
        print 'Finished'

    @staticmethod
    def process(csv):
        shows = collections.defaultdict(list)
        with open(csv, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                if data[1] != "None":
                    shows[data[0]].append((data[1],data[2],data[3].rstrip()))
            f.close()
        avgAndFinale = collections.defaultdict(list)
        for show in shows.keys():
            total = 0
            eps = 0
            finale = None
            for episode in shows[show]:
                finale = episode
                total += float(episode[2])
                eps += 1.0
            if round(total/eps, 2) != float(finale[2]):
                avgAndFinale[show] = (round(total/eps, 2), float(finale[2]))
        print avgAndFinale
        print len(avgAndFinale)
        return avgAndFinale

    @staticmethod
    def visualize(csv):
        avgAndFinale = Q1.process(csv)
        x = []
        y = []
        for show in avgAndFinale.keys():
            x.append(avgAndFinale[show][0])
            y.append(avgAndFinale[show][1])

        plt.scatter(x,y, marker=".")
        plt.xlabel("Average Episode Rating")
        plt.ylabel("Season Finale Rating")
        p = pearsonr(x,y)
        line = np.arange(10)

        plt.plot(line * p[0], color="red")
        plt.show()








