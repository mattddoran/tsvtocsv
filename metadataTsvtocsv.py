# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("metadataBasic.txt", "a")
	out2 = open("metadataKeyword.txt", "a")
	out3 = open("nameFBLikes.txt", "a")

	with open("metadataTest.txt", "r") as f:
		for line in f.readlines()[1:]:
			# extract metadata fields (color, directorfblikes, gross, title, castfblikes, imdblink, language, country, content-rating, budget, imdbscore, aspectratio, movielikes)
			line = line.split(",")
			keywords  = line[16]
			out1.write("\\n,{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(line[0],line[4],line[8],line[11],line[13],line[17],line[18],line[19],line[20],line[21],line[23],line[24],line[25]))

			# keywords
			out2.write("\\n,")
			keywords = keywords.replace("|",",")
			out2.write(keywords+"\n")

			# names and fb likes
			out3.write("{},{}\n".format(line[10],line[7])) # actor 1
			out3.write("{},{}\n".format(line[6],line[24])) # actor 2
			out3.write("{},{}\n".format(line[14],line[5])) # actor 3

		out1.close()
		out2.close()
		out3.close()

main()