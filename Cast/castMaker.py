# Carl Fee
# tsv to csv script
#

def main():

        out1 = open("Cast_has_Person.csv", "w")
        out2 = open("Cast.csv", "w")
        with open("BIG_FILE_cast.tsv", "r") as f:
                iDWriter = 6
                iDDirector = 7
                for line in f.readlines()[1:]:
                        line1 = line.split("\t")
                        castID = line1[0][2:]
                        out2.write("{}\n".format(castID))
                        directors = line1[1].split(",")
                        writers = line1[2].split(",")
                        for director in directors:
                                num = len(director)
                                director = director[2:]
                                if num > 2:
                                        out1.write("{},{},{}\n".format(castID,director,iDDirector))
                        for writer in writers:
                                num = len(writer) - 1
                                writer = writer[2:num]
                                if num > 2:
                                        out1.write("{},{},{}\n".format(castID,writer,iDWriter))


                out1.close()

main()
