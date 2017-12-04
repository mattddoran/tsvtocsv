from Question import Question
import mysql.connector
import os.path
import collections
import matplotlib.pyplot as plt

# What are the trends of genres? What genres are currently getting produced more often
# than they used to be?

class Q4(Question):
    def query(self):
        if os.path.isfile(self.queryFile):
            print 'already ran query'
        else:
            print 'need to run query'
            query =(
            "select mydb2.genres.genre, mydb2.title.startYear, count(*) as 'Number of Titles' "
            "from mydb2.genres cross join mydb2.titlegenres cross join mydb2.title cross join mydb2.rating "
            "where mydb2.genres.idGenre = mydb2.titlegenres.Genres_idGenre and mydb2.title.idTitle = mydb2.titlegenres.Title_idTitle "
            "and mydb2.rating.Title_idTitle = mydb2.title.idTitle "
            "group by mydb2.genres.idGenre, mydb2.title.startYear;")
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query)

            out = open(self.queryFile, "w")
            for (genre, year, count) in cursor:
                # convert entire line to csv
                out.write("{},{},{}\n".format(genre, year, count))

            out.close()

    def process(self): #convert csv populated by query and return a list with coordinates ready to be plotted
        l1 = collections.defaultdict(list)
        with open(self.queryFile, 'r') as f: # open csv populated through query
            for line in f.readlines(): #line by line...
                data = line.split(',')
                if data[1] != "None": #Ignore years recorded as "None" and populate genre dictionary with year and number of titles
                    l1[data[0]].append((data[1], data[2].rstrip()))
                    #l1[data[0]].append(data[2].rstrip())
            f.close()
        popularGenres = collections.defaultdict(int)
        for genre in l1.keys(): # Record frequencies of each genre
            for year in l1[genre]:
                popularGenres[genre] += int(year[1])

        popularGenres = sorted(popularGenres.items(), key=lambda(k,v): v) #Sort by most popular genres
        #print popularGenres
        for genre in popularGenres[:20]: #remove 20 least popular genres
            del l1[genre[0]]

        return l1

    def visualize(self): #create line graph of all genres
        l1 = self.process()
        genres = []
        for genre in l1.keys():
            genres.append(genre) #record genre names for annotation
            x = []
            y = []
            for year in l1[genre]:
                if int(year[0]) < 2017 and int(year[0]) > 1960: #ignore 2017 as it only has a subset of data and discard genre data older than 1960
                    x.append(int(year[0]))
                    y.append(int(year[1]))
            plt.plot(x,y) # (Year, Number of Titles)
        plt.legend(genres, loc="upper left") # annotate genres being displayed

        plt.show()


