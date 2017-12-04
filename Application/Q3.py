from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt
import numpy as np

# Based off of a series pilot episode, can we visualize/predict what season the show 
# will air for?

class Q3(Question):
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

    def process(self): #process csv and return list ready to be plotted
        l1 = collections.defaultdict(list)
        with open(self.queryFile, 'r') as f: #open csv populated through query
            for line in f.readlines():
                data = line.split(',')
                l1[data[0]].append((data[1],data[2],data[3].rstrip())) #dictionary of tv show tconsts to a list of tuples (season, ep, rating)
        pilotAndSeasonsRan = collections.defaultdict(list)
        for show in l1.keys():
            l1[show].sort(key = lambda tup: tup[0]) #sort episodes by season
            if len(l1[show]) > 20: #only take in series with a substantial amount of episodes
                first = None
                curr = None
                nOfSeasons = 1
                for episode in l1[show]:
                    if first == None:
                        first = episode
                    prev = curr
                    curr = episode
                    if prev != None and prev[0] != curr[0]: #record number of seasons (when season number changes between tuples)
                        nOfSeasons += 1.0
                if nOfSeasons < 13: #exclude odd shows with 30+ seasons to visualize heatmap better
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

    def visualize(self): #Create a heatmap from the list generated from csv
        data = self.process()
        x = []
        y = []
        for show in data.keys():
            if len(data[show][0]) > 1: # filter out ratings less than 1
                x.append(float(data[show][0][0]))
                y.append(int(data[show][0][1])) 
        heatmap, xedges, yedges = np.histogram2d(x, y, bins=12) #generate a heatmap with bins the size of each season
        extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

        plt.clf()
        ax = plt.imshow(heatmap.T, extent=extent, origin='lower') #plot heatmap
        plt.colorbar() #show colorbar on the right side of the heatmap to contextualize colors
        plt.xlabel("Pilot Episode Rating")
        plt.ylabel("Number of Seasons Aired")
        plt.show()








