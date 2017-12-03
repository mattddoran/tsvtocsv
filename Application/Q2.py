from Question import Question
import mysql.connector
import os.path
import collections
# import matplotlib.pyplot as plt

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
        print 'Finished'

    @staticmethod
    def process(csv):
        directorShows = collections.defaultdict(list)
        with open(csv, "r") as f:
            for line in f.readlines():
                data = line.split(",")
                if data[1] != "None" or data[2] != "None":
                    #id: [year, rating]
                    directorShows[data[0]].append((data[1],data[2].rstrip()))
            f.close()