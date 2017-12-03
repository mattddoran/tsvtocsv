from Question import Question
import mysql.connector
import os.path


class Q5(Question):
    @staticmethod
    def query():
        fname = "query4.csv"
        if os.path.isfile(fname):
            print 'already ran query'
        else:
            print 'need to run query'
            query = (
                "select mydb2.genres.genre, mydb2.title.startYear, count(*) as 'Number of Titles' "
                "from mydb2.genres cross join mydb2.titlegenres cross join mydb2.title cross join mydb2.rating "
                "where mydb2.genres.idGenre = mydb2.titlegenres.Genres_idGenre and mydb2.title.idTitle = mydb2.titlegenres.Title_idTitle "
                "and mydb2.rating.Title_idTitle = mydb2.title.idTitle "
                "group by mydb2.genres.idGenre, mydb2.title.startYear;")
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query)

            out = open(fname, "w")
            for (genre, year, count) in cursor:
                # convert entire line to csv
                out.write("{},{},{}\n".format(genre, year, count))

            out.close()
        print 'Finished'