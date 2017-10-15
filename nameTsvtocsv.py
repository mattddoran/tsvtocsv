# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("nameBasic.csv", "a")
	out2 = open("nameProfession.csv", "a")

	with open("nameTest.txt", "r") as f:
		for line in f.readlines()[1:]:
			# convert entire line minus professions/titles to csv
			line1 = line.split("\t")
			out1.write("{},{},{},{}\n".format(line1[0],line1[1],line1[2],line1[3]))

			# nconst + professions
			line2 = line.split("\t")
			out2.write(line2[0]+",")
			out2.write(line2[4]+"\n")

		out1.close()
		out2.close()

main()