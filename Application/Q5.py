from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


class Q5(Question):
    @staticmethod
    def query():
        fname1 = "query51.csv"
        if os.path.isfile(fname1):
            print 'already ran query 1'
        else:
            print 'need to run query 1'
            query1 = ("select Title_idTitle, gross, castTotalFBLikes,budget "
                      "from title cross join metadata "
                      "where startYear > 1950 and idTitle = Title_idTitle;")
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query1)

            out = open(fname1, "w")
            for (id, gross, castLikes, budget) in cursor:
                # convert entire line to csv
                out.write("{},{},{},{}\n".format(id, gross, castLikes, budget))

            out.close()
        fname2 = "query5_2.csv"
        if os.path.isfile(fname2):
            print 'already ran query 2'
        else:
            print 'need to run query 2'
            query = (
                "select cast_has_person_with_profession.Person_idPerson, mydb2.title.startYear, rating.averageRating, mydb2.title.idTitle "
                "from mydb2.cast_has_person_with_profession cross join mydb2.title cross join mydb2.rating "
                "where mydb2.cast_has_person_with_profession.Cast_idCast = mydb2.title.idTitle and Professions_idProfession = 7 "
                "and mydb2.rating.Title_idTitle = mydb2.title.idTitle;"
            )
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query)

            out = open(fname2, "w")
            for (personID, year, rating, idTitle) in cursor:
                # convert entire line to csv
                out.write("{},{},{},{}\n".format(personID, year, rating, idTitle))

            out.close()
        print 'Finished'

    @staticmethod
    def process(csv):
        i = []  #index
        x = []  # budget 3
        y = []  # cast like 2
        z = []  # gross 1
        with open(csv, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                if len(data) == 4 and data[1] != "None" and data[2] != "None" and int(data[2]) < 200000 and data[3] != "None" and int(data[3]) < 300000000:
                    i.append(int(data[0]))
                    z.append(int(data[1]))
                    y.append(int(data[2]))
                    x.append(int(data[3]))
            f.close()
        return i,x,y,z

    @staticmethod
    def visualize(csv):
        i, x, y, z = Q5.process(csv)
        i_2, x_1, z_1 = Q5.processDir(csv)
        gross_d = []
        budget_d = []
        for inc in range(0,len(i_2)):
            idT = i_2[inc]
            for jinc in range(0,len(i)):
                if(i[jinc] == idT):
                    gross_d.append(z[jinc])
                    
                    break
        print len(gross_d), "should be", len(i_2)
        plt.scatter(x_1, gross_d, marker=".")
        plt.xlabel("director xp")
        plt.ylabel("gross")
        plt.show()
        plt.scatter(x_1, z_1, marker=".")
        plt.xlabel("director xp")
        plt.ylabel("rating")
        plt.show()
        print "carl1", len(x)
        print "carl2", len(x_1)
        x = stats.zscore(np.array(x))
        y = stats.zscore(np.array(y))
        #z = stats.zscore(np.array(z))
        sumx_y = []
        for i in range(0,len(x)):
            sumx_y.append(x[i] + y[i])
        plt.scatter(sumx_y, z, marker=".")
        plt.xlabel("budget and likes")
        plt.ylabel("gross")
        plt.show()
        plt.scatter(x, z, marker=".")
        plt.xlabel("budget")
        plt.ylabel("gross")
        plt.show()
        plt.scatter(y, z, marker=".")
        plt.xlabel("cast likes")
        plt.ylabel("gross")
        plt.show()


    @staticmethod
    def processDir(csv):
        relevantIds = set()
        with open(csv, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                if len(data) == 4 and data[1] != "None" and data[2] != "None" and int(data[2]) < 200000 and data[3] != "None" and int(data[3]) < 300000000:
                    relevantIds.add(int(data[0]))
            f.close()
        directorShows = collections.defaultdict(list)
        with open("query5_2.csv", "r") as f:
            for line in f.readlines():
                data = line.split(",")
                #print int(data[3]) in relevantIds
                if data[1] != "None" and data[2] != "None":
                    # id: [year, rating]
                    #print "here"
                    directorShows[data[0]].append((data[1],data[2],data[3].rstrip()))
            f.close()
        i = []
        x = []
        y = []
        for director in directorShows.keys():
            directorShows[director].sort(key=lambda tup: tup[0])  # sort by year to rank
            count = 0
            # print director

            for info in directorShows[director]:
                # print count, info[0], info[1]
                if int(info[2]) in relevantIds:
                    i.append(int(info[2]))
                    x.append(count)
                    y.append(float(info[1]))  # rating of the show
                count += 1
        return i, x, y


