# Matthew Doran
# create dictionary of all genres

def main():

	out = open("genres.csv", "a")
	with open("titleGenre.csv", "r") as f:
		genreDict = {}
		i = 1
		for line in f.readlines():
			print(line)
			genres = line.split(",")
			genres = genres[1:]
			genres[len(genres)-1] = genres[len(genres)-1][:-1] # shave off newline
			for genre in genres:
				if genre not in genreDict:
					genreDict[genre] = i
					i += 1
			print genreDict

		out.write(str(genreDict))
		out.close()
main()