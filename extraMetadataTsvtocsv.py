# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("extraMetadataBasic.txt", "a")

	with open("extraMetadataTest.txt", "r") as f:
		for line in f.readlines()[1:]:
			# extract metadata fields (rank, title, description, votes, metascore)
			line = line.split("\"")
			print(line)
			print("!!@!@!@!@!@!@!@!@!" + line[2])
			#out1.write("\\n,{},{},{},{},{}\n".format(line[0],line[1],line[3],line[9],line[11]))

		out1.close()


main()