# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("ratingBasic.csv", "a")

	with open("BIG_FILE_rating.tsv", "r") as f:
		for line in f.readlines()[1:]:
			# convert entire line to csv
			line = line.replace("\t",",")
			line = line[2:]
			out1.write(line)

		out1.close()

main()
