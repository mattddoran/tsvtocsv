from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import scipy

# This question is about looking for the relationship of total cast likes, director experience, and budget on gross

# needs two files unlike the other questions (one for each query on the database)
# The reason we are not doing this in a cross join is because we needed to use all the data to rank the directros
# before they could be paired to the limited metadata
class Q5(Question):
    def __init__(self, queryFile1, queryFile2):
        self.queryFile1 = queryFile1
        self.queryFile2 = queryFile2

    #run the query and generate a file to be used by the other methods if the file does not already exsist
    def query(self):
        if os.path.isfile(self.queryFile1):
            print 'already ran query 1'
        else:
            print 'need to run query 1'
            query1 = ("select Title_idTitle, gross, castTotalFBLikes,budget "
                      "from title cross join metadata "
                      "where startYear > 1970 and idTitle = Title_idTitle;")
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query1)

            out = open(self.queryFile1, "w")
            for (id, gross, castLikes, budget) in cursor:
                # convert entire line to csv
                out.write("{},{},{},{}\n".format(id, gross, castLikes, budget))

            out.close()
        if os.path.isfile(self.queryFile2):
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

            out = open(self.queryFile2, "w")
            for (personID, year, rating, idTitle) in cursor:
                # convert entire line to csv
                out.write("{},{},{},{}\n".format(personID, year, rating, idTitle))

            out.close()

    # filter and generate lists of index i, budget x, cast y, and gross z after extracting data from the csv file
    def process(self):
        i = []  #index
        x = []  # budget 3
        y = []  # cast like 2
        z = []  # gross 1
        with open(self.queryFile1, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                #Make sure we are selecting relevant data
                #filter out a minimal amount of stray points with the magic numbers
                if len(data) == 4 and data[1] != "None" and data[2] != "None" and int(data[2]) < 200000 and data[3] != "None" and int(data[3]) < 300000000:
                    i.append(int(data[0]))
                    z.append(int(data[1]))
                    y.append(int(data[2]))
                    x.append(int(data[3]))
            f.close()
        return i,x,y,z

    # use the proccessed data to generate scatter plots based on different variables
    def visualize(self):
        i, x, y, z = self.process()
        i_2, x_1, z_1 = self.processDir()
        #these next two arrays will be populated in a way to match the director data
        gross_d = []
        budget_d = []
        # match all the datapoints that are in title and metadata so they can be plotted
        # The reason we are not doing this in a cross join is because we needed to use all the data to rank the directros
        # before they could be paired to the limited metadata
        for inc in range(0,len(i_2)):
            idT = i_2[inc]
            # linear search through the posible data points since they are not in order to match
            for jinc in range(0,len(i)):
                if(i[jinc] == idT):
                    gross_d.append(z[jinc])
                    budget_d.append(x[jinc])
                    break

        #Scatter One
        plt.scatter(x_1, gross_d, marker=".")
        plt.xlabel("Previos Films Directed by Movie Director")
        plt.ylabel("Gross Product $100 million")
        plt.title("1970 on Data")
        plt.show()

        #scatter two
        #convert to z-scores
        x = stats.zscore(np.array(x))
        y = stats.zscore(np.array(y))
        # add the two z scores
        sumx_y = []
        for i in range(0,len(x)):
            sumx_y.append(x[i] + y[i])
        plt.scatter(sumx_y, z, marker=".")
        plt.xlabel("Previos Films Directed by Movie Director")
        plt.xlabel("Budget Z-score + Total Cast Likes Z-score")
        plt.ylabel("Gross Product $100 million")
        plt.show()

        #scatter three
        plt.scatter(x, z, marker=".")
        plt.xlabel("Previos Films Directed by Movie Director")
        plt.xlabel("Budget Z-score")
        plt.ylabel("Gross Product $100 million")
        plt.show()

        #scatter four
        plt.scatter(y, z, marker=".")
        plt.xlabel("Previos Films Directed by Movie Director")
        plt.xlabel("Cast Likes Z-score")
        plt.ylabel("Gross Product $100 million")
        plt.show()

        #scatter five
        #convert to z
        gross_d = stats.zscore(np.array(gross_d))
        budget_d = stats.zscore(np.array(budget_d))
        x_1 = stats.zscore(np.array(x_1))
        sum_bd = []
        #add z scores
        for i in range(0,len(i_2)):
            sum_bd.append(budget_d[i] + x_1[i])
        plt.scatter(sum_bd, gross_d, marker=".")
        plt.xlabel("Previos Films Directed by Movie Director")
        plt.xlabel("Budget Z-score + Previos Films Directed by Movie Director")
        plt.ylabel("Gross Product $100 million")
        plt.show()

    # open the files generated by querying and create lists of title indexes i, movies directed x, and rating of the show y
    def processDir(self):
        # ids that correspond to metadata
        relevantIds = set()
        with open(self.queryFile1, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                # ids that correspond to metadata
                if len(data) == 4 and data[1] != "None" and data[2] != "None" and int(data[2]) < 200000 and data[3] != "None" and int(data[3]) < 300000000:
                    relevantIds.add(int(data[0]))
            f.close()

        # create a dictionary of the directors
        directorShows = collections.defaultdict(list)
        with open(self.queryFile2, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                #print int(data[3]) in relevantIds
                if data[1] != "None" and data[2] != "None":
                    # director id: [year, rating, title id]
                    directorShows[data[0]].append((data[1],data[2],data[3].rstrip()))
            f.close()
        i = []
        x = []
        y = []
        for director in directorShows.keys():
            directorShows[director].sort(key=lambda tup: tup[0])  # sort by year to rank
            # this count tracks how many movies the director has directed
            count = 0

            for info in directorShows[director]:
                # only add the director to the list if it will have matching metadata
                if int(info[2]) in relevantIds:
                    i.append(int(info[2]))
                    x.append(count) # this count tracks how many movies the director has directed
                    y.append(float(info[1]))  # rating of the show
                count += 1
        return i, x, y
