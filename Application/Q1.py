from Question import Question
import mysql.connector
import os.path

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