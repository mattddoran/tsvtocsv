# Matthew Doran
# helps populate metadata with titleids

def main():

	out = open("metadataBasicWTitleId.csv", "a")

	titleDict = {}
	with open("titleBasic.csv", "r") as f:
		for line in f.readlines():
			line = line.split(",")
			tid = line[0]
			tid = tid[2:]
			title = line[2] + " "
			titleDict[title] = tid
		print(str(titleDict))

	with open("metadataBasic.csv", "r") as f:
		for line in f.readlines():
			columns = line.split(",")
			title = columns[4]
			try:
				newLine = titleDict[title] + line[2:]
				print(newLine)
				out.write("{}".format(newLine))
				
			except KeyError:
				pass

		out.close()


main()