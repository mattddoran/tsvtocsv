# Carl Fee
# tsv to csv script
#

def main():

        out1 = open("Cast_has_Person.csv", "w")
        inc = 0
        with open("BIG_FILE_cast.tsv", "r") as f:

                for line in f.readlines()[1:]:
                        # convert entire line minus professions/titles to csv
                        line1 = line.split("\t")
                        line1[0] = line1[0][2:]
                        out1.write("{},{},{},{},\\N\n".format(line1[0],line1[1],line1[2],line1[3]))

                        # nconst + professions
                        line2 = line.split("\t")
                        out2.write(line2[0]+",")
                        out2.write(line2[4]+"\n")
                        inc+=1
                        #if(inc > 100000):
                                #break

                out1.close()
                out2.close()

main()
