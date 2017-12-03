from Question import Question
import mysql.connector
import os.path


class Q5(Question):
    @staticmethod
    def query():
        fname1 = "query5_1.csv"
        if os.path.isfile(fname1):
            print 'already ran query 1'
        else:
            print 'need to run query 1'
            query1 = ("select * from metadata")
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query1)

            out = open(fname1, "w")
            for (id, gross, castLikes, budget) in cursor:
                # convert entire line to csv
                out.write("{},{},{}\n".format(id, gross, castLikes, budget))

            out.close()
        fname2 = "query5_2.csv"
        if os.path.isfile(fname2):
            print 'already ran query 2'
        else:
            print 'need to run query 2'
            query = (
                "select cast_has_person_with_profession.Person_idPerson, mydb2.title.startYear, rating.averageRating "
                "from mydb2.cast_has_person_with_profession cross join mydb2.title cross join mydb2.rating "
                "where mydb2.cast_has_person_with_profession.Cast_idCast = mydb2.title.idTitle and Professions_idProfession = 7 "
                "and mydb2.rating.Title_idTitle = mydb2.title.idTitle;"
            )
            cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2')
            cursor = cnx.cursor(buffered=True)
            cursor.execute(query)

            out = open(fname2, "w")
            for (personID, year, rating) in cursor:
                # convert entire line to csv
                out.write("{},{},{}\n".format(personID, year, rating))

            out.close()
        print 'Finished'