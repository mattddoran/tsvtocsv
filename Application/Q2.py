from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt
import numpy as np

class Q2(Question):
    @staticmethod
    def query():
        fname = "query2.csv"
        if os.path.isfile(fname):
            print 'already ran query'
        else:
            print 'need to run query'
            query = (
                "select cast_has_person_with_profession.Person_idPerson, mydb2.title.startYear, rating.averageRating "
                "from mydb2.cast_has_person_with_profession cross join mydb2.title cross join mydb2.rating "
                "where mydb2.cast_has_person_with_profession.Cast_idCast = mydb2.title.idTitle and Professions_idProfession = 7 "
                "and mydb2.rating.Title_idTitle = mydb2.title.idTitle;"
            )
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query)

            out = open(fname, "w")
            for (personID, year, rating) in cursor:
                # convert entire line to csv
                out.write("{},{},{}\n".format(personID, year, rating))

            out.close()

    @staticmethod
    def process(csv):
        directorShows = collections.defaultdict(list)
        with open(csv, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                if data[1] != "None" and data[2] != "None":
                    #id: [year, rating]
                    directorShows[data[0]].append((data[1],data[2].rstrip()))
            f.close()

        x = []
        y = []
        for director in directorShows.keys():
            directorShows[director].sort(key=lambda tup: tup[0])  # sort by year to rank
            count = 0
            #print director

            for info in directorShows[director]:
                #print count, info[0], info[1]
                x.append(count)
                y.append(float(info[1])) #rating of the show
                count += 1
        return x, y

    @staticmethod
    def visualize(csv):
        x, y = Q2.process(csv)
        plt.scatter(x, y, marker=".")
        plt.xlabel("Previus Number of Movies Directed by Director")
        plt.ylabel("Average Movie Rating (0 - 10)")
        #line = scipy.stats.np.arange(10)

        #plt.plot(line * p[0], color="red")
        plt.show()

        # heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)
        # extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
        #
        # plt.clf()
        # plt.imshow(heatmap.T, extent=extent, origin='lower')
        # plt.xlabel("Previus Number of Movies Directed by Director")
        # plt.ylabel("Average Movie Rating")
        # plt.show()

