# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("titleBasic.txt", "a")
	out2 = open("titleGenre.txt", "a")

	with open("titleTest.txt", "r") as f:
		for line in f.readlines()[1:]:
			# convert entire line minus genres to csv
			line1 = line.split("\t")
			out1.write("{},{},{},{},{},{},{},{},\n".format(line1[0],line1[1],line1[2],line1[3],line1[4],line1[5],line1[6],line1[7]))

			# tconst + genres
			line2 = line.split("\t")
			out2.write(line2[0]+",")
			out2.write(line2[8])

		out1.close()
		out2.close()

main()