from Question import Question
import mysql.connector

class Q4(Question):
    @staticmethod
    def query():
        cnx = mysql.connector.connect(user='root', password='Rrevolution@1', host='127.0.0.1', database='mydb2', buffered='true')

        cursor = cnx.cursor()
        #
        query = ("SELECT primaryTitle,originalTitle "
                 "FROM title "
                 "WHERE idTitle = 9;")
        cursor.execute(query)
        for (isTitle, a) in cursor:
            print isTitle


        query =(
        "select mydb2.genres.genre, count(*) as 'Number of Titles', sum(mydb2.rating.numVotes) as 'Sum of votes for all Titles in this Genre'"
        "from mydb2.genres cross join mydb2.titlegenres cross join mydb2.title cross join mydb2.rating"
        "where mydb2.genres.idGenre = mydb2.titlegenres.Genres_idGenre and mydb2.title.idTitle = mydb2.titlegenres.Title_idTitle and mydb2.rating.Title_idTitle = mydb2.title.idTitle and mydb2.rating.averageRating < 2 and mydb2.rating.numVotes > 10"
        "group by mydb2.genres.idGenre order by sum(rating.numVotes) Desc;")

        # cursor.execute()

        cursor.execute(query)
        #
        # list = []
        # num = 0
        # print 'executed'
        # for (isTitle, a) in cursor:
        #     # print isTitle, a
        #     # print("{}".format(isTitle))
        #     num += 1
        #     if (num % 100000 == 0):
        #         print num
        #         list.append(isTitle)
        # print list
        # cursor.close()

        cnx.close()