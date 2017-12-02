# Matthew Doran
# helps populate metadata with titleids

def main():

	out = open("metadataBasicWTitleId.csv", "w")

	titleDict = {}
	with open("titleBasic.csv", "r") as f:
		for line in f.readlines():
			line = line.split(",")
			if len(line) > 3:
				tid = line[0]
				tid = tid[2:]
				title = line[2]
				titleDict[title] = tid
		# print(str(titleDict))

	with open("metadataBasic.csv", "r") as f:
		for line in f.readlines():
			columns = line.split(",")
			title = columns[4]
			try:
				newLine = titleDict[title.rstrip()] + "," + columns[3] + "," +  columns[5] + "," + columns[10] # tconst, gross, cast likes, budget
				print(newLine)
				out.write("{}\n".format(newLine))
				
			except KeyError:
				pass

		out.close()


main()