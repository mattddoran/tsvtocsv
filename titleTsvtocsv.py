# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("titleBasic.csv", "w")
	out2 = open("titleGenre.csv", "w")

	with open("BIG_FILE_Title.tsv", "r") as f:
		inc = 0
		for line in f.readlines()[1:]:
			# convert entire line minus genres to csv
			line = line.replace(","," ")
			line1 = line.split("\t")
			line1[0] = line1[0][2:]
			out1.write("{},{},{},{},{},{},{},{}\n".format(line1[0],line1[1],line1[2],line1[3],line1[4],line1[5],line1[6],line1[7]))

			# tconst + genres
			line2 = line.split("\t")
			out2.write(line2[0]+",")
			out2.write(line2[8])
			inc+=1
			#if(inc > 100000):
				#break

		out1.close()
		out2.close()

main()
