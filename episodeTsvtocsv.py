# Matthew Doran
# tsv to csv script
#

def main():

	out1 = open("episodeBasic.txt", "a")

	with open("episodeTest.txt", "r") as f:
		for line in f.readlines()[1:]:
			# convert entire line to csv
			line = line.replace("\t",",")
			out1.write(line)

		out1.close()

main()