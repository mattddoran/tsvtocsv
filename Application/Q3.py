from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt
import numpy as np

class Q3(Question):
    @staticmethod
    def query():
        fname = "query3.csv"
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
        l1 = collections.defaultdict(list)
        with open(csv, 'r') as f:
            for line in f.readlines():
                data = line.split(',')
                l1[data[0]].append((data[1],data[2],data[3].rstrip()))
        pilotAndSeasonsRan = collections.defaultdict(list)
        for show in l1.keys():
            l1[show].sort(key = lambda tup: tup[0]) #sort episodes by season
            if len(l1[show]) > 20:
                first = None
                curr = None
                nOfSeasons = 1
                for episode in l1[show]:
                    if first == None:
                        first = episode
                    prev = curr
                    curr = episode
                    if prev != None and prev[0] != curr[0]:
                        nOfSeasons += 1.0
                if nOfSeasons < 13:
                    pilotAndSeasonsRan[show].append([first[2],nOfSeasons])
        normalized = collections.defaultdict(int)
        # for show in pilotAndSeasonsRan.keys(): # normalize
        #     print show[0]
        #     print show[1]
        #     print round(float(pilotAndSeasonsRan[show][0][0]),0)
        #     print int(pilotAndSeasonsRan[show][0][1])
        #     normalized[round(float(pilotAndSeasonsRan[show][0][0]),0)] += round(float(pilotAndSeasonsRan[show][0][1]),0)

        # print normalized

        # for show in pilotAndSeasonsRan.keys():
        #     #print int(pilotAndSeasonsRan[show][0][1])
        #     #print normalized[int(pilotAndSeasonsRan[show][0][1])]-1

        #     pilotAndSeasonsRan[show][0][1] = round(pilotAndSeasonsRan[show][0][1]/normalized[round(float(pilotAndSeasonsRan[show][0][0]),0)],4)
        return pilotAndSeasonsRan


    @staticmethod
    def visualize(csv):
        data = Q3.process(csv)
        x = []
        y = []
        for show in data.keys():
            if len(data[show][0]) > 1:
                x.append(float(data[show][0][0]))
                y.append(int(data[show][0][1])) 
        heatmap, xedges, yedges = np.histogram2d(x, y, bins=12, normed=True)
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

        plt.clf()
        plt.imshow(heatmap.T, extent=extent, origin='lower')
        plt.xlabel("Pilot Episode Rating")
        plt.ylabel("Number of Seasons Aired")
        plt.show()








