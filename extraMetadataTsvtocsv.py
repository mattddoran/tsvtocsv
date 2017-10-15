# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("extraMetadataBasic.csv", "a")

	with open("extraMetadataTest.txt", "r") as f:
		for line in f.readlines()[1:]:
			# extract metadata fields (rank, title, description, votes, metascore)
			line = line.split("\",")
			rankTitle = line[0]
			rankTitle = rankTitle.split(",")
			description = line[1]
			description = description.split(",\"")
			description = description[0]
			description = description.split(".,")
			description = description[0]
			description = description.replace("\"","")
			out1.write("\\n,{},{},{}\n".format(rankTitle[0],rankTitle[1], description))

		out1.close()


main()